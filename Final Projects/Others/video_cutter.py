import os
import sys
import ffmpeg
from datetime import datetime, timedelta
import subprocess
import time
import re
import threading
from queue import Queue

def time_to_seconds(time_str):
    """
    Convierte una cadena de tiempo en formato HH:MM:SS o MM:SS a segundos
    """
    try:
        parts = time_str.split(':')
        if len(parts) == 3:  # HH:MM:SS
            hours, minutes, seconds = map(int, parts)
            return hours * 3600 + minutes * 60 + seconds
        elif len(parts) == 2:  # MM:SS
            minutes, seconds = map(int, parts)
            return minutes * 60 + seconds
        else:
            return int(time_str)  # Solo segundos
    except ValueError:
        print(f"Error: Formato de tiempo inválido: {time_str}")
        return None

def seconds_to_time(seconds):
    """
    Convierte segundos a formato HH:MM:SS
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def get_video_info(video_path):
    """
    Obtiene información básica del video usando ffmpeg
    """
    try:
        probe = ffmpeg.probe(video_path)
        
        # Buscar el stream de video principal
        video_stream = None
        for stream in probe['streams']:
            if stream['codec_type'] == 'video':
                video_stream = stream
                break
        
        if video_stream is None:
            print("Error: No se encontró stream de video en el archivo")
            return None
        
        # Intentar obtener duración del stream de video
        if 'duration' in video_stream:
            duration = float(video_stream['duration'])
        # Si no está en el stream, intentar obtenerla del formato
        elif 'format' in probe and 'duration' in probe['format']:
            duration = float(probe['format']['duration'])
        else:
            print("Error: No se pudo determinar la duración del video")
            return None
            
        return duration
        
    except KeyError as e:
        print(f"Error: Clave no encontrada en la información del video: {e}")
        return None
    except Exception as e:
        print(f"Error al cargar el video: {e}")
        return None

def show_progress_bar(current, total, prefix='', suffix='', length=40):
    """
    Muestra una barra de progreso en la consola
    """
    if total == 0:
        return
    filled_length = int(length * current // total)
    bar = '█' * filled_length + '░' * (length - filled_length)
    percent = 100 * (current / float(total))
    print(f'\r{prefix} |{bar}| {percent:.1f}% {suffix}', end='', flush=True)
    if current >= total:
        print()

def parse_time_from_ffmpeg(time_str):
    """
    Parsea el tiempo desde la salida de FFmpeg (formato HH:MM:SS.ss)
    """
    try:
        parts = time_str.split(':')
        if len(parts) == 3:
            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = float(parts[2])
            return hours * 3600 + minutes * 60 + seconds
    except:
        return 0

def process_video_with_progress(input_path, output_path, start_time, duration, segment_name):
    """
    Procesa un video con FFmpeg mostrando el progreso en tiempo real
    """
    # Construir comando FFmpeg
    cmd = [
        'ffmpeg',
        '-y',  # Sobrescribir archivos de salida
        '-ss', str(start_time),  # Tiempo de inicio
        '-i', input_path,  # Archivo de entrada
        '-t', str(duration),  # Duración del segmento
        '-c:v', 'libx264',  # Codec de video
        '-c:a', 'aac',  # Codec de audio
        '-preset', 'fast',  # Preset para balance velocidad/calidad
        '-progress', 'pipe:1',  # Reportar progreso a stdout
        '-loglevel', 'warning',  # Reducir verbosidad
        output_path
    ]
    
    # Variables para el progreso
    current_time = 0
    last_update = 0
    stderr_output = []
    
    try:
        # Ejecutar FFmpeg
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        
        # Thread para capturar stderr
        def read_stderr():
            for line in process.stderr:
                stderr_output.append(line)
        
        stderr_thread = threading.Thread(target=read_stderr)
        stderr_thread.daemon = True
        stderr_thread.start()
        
        # Leer la salida línea por línea
        for line in process.stdout:
            line = line.strip()
            
            # Buscar la línea con el tiempo actual
            if line.startswith('out_time_ms='):
                try:
                    # Convertir microsegundos a segundos
                    current_ms = int(line.split('=')[1])
                    current_time = current_ms / 1000000.0
                    
                    # Actualizar la barra de progreso (no más de 10 veces por segundo)
                    current_timestamp = time.time()
                    if current_timestamp - last_update > 0.1:
                        show_progress_bar(
                            current_time, 
                            duration, 
                            f'   🎬 {segment_name}',
                            f'({seconds_to_time(current_time)}/{seconds_to_time(duration)})',
                            40
                        )
                        last_update = current_timestamp
                except:
                    pass
        
        # Esperar a que termine el proceso
        process.wait()
        stderr_thread.join(timeout=1)
        
        # Mostrar progreso completo
        show_progress_bar(duration, duration, f'   🎬 {segment_name}', 'Completado', 40)
        
        # Verificar si el archivo se creó correctamente
        # Incluso si FFmpeg devuelve un código de error, si el archivo existe y tiene tamaño, lo consideramos exitoso
        if os.path.exists(output_path) and os.path.getsize(output_path) > 10240:  # Al menos 10KB
            return True, None
        
        # Si no se creó el archivo o es muy pequeño, entonces sí hay error
        error_msg = ''.join(stderr_output)
        return False, error_msg if error_msg else "El archivo no se creó o es demasiado pequeño"
        
    except Exception as e:
        return False, str(e)

def create_cut_segments(video_path, output_folder):
    """
    Función principal para crear los segmentos de video
    """
    # Verificar si el archivo existe
    if not os.path.exists(video_path):
        print(f"Error: El archivo {video_path} no existe.")
        return
    
    # Obtener información del video
    duration = get_video_info(video_path)
    if duration is None:
        return
    
    print(f"\n📹 Video cargado: {os.path.basename(video_path)}")
    print(f"⏱️  Duración total: {seconds_to_time(duration)}")
    
    # Crear carpeta específica para este video
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    video_output_folder = os.path.join(output_folder, video_name)
    print(f"📁 Los videos se guardarán en: {video_output_folder}")
    
    # Crear carpeta de salida si no existe
    os.makedirs(video_output_folder, exist_ok=True)
    
    segments = []
    
    # Preguntar cuántos ejercicios se van a procesar
    while True:
        try:
            num_exercises = input("\n🔢 ¿Cuántos ejercicios quieres separar? (número): ").strip()
            if num_exercises == "":
                print("⚠️  Debes ingresar un número válido.")
                continue
            num_exercises = int(num_exercises)
            if num_exercises <= 0:
                print("⚠️  El número debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("⚠️  Por favor ingresa un número válido.")
    
    print("\n" + "="*60)
    print("📚 CONFIGURACIÓN DE EJERCICIOS")
    print("="*60)
    print("Formatos de tiempo aceptados:")
    print("  • HH:MM:SS (ejemplo: 1:30:45)")
    print("  • MM:SS (ejemplo: 15:30)")
    print("  • Segundos (ejemplo: 900)")
    print("  • 'fin' o 'end' para el final del video")
    print(f"\nVas a configurar {num_exercises} ejercicio(s)")
    print("-"*60)
    
    for exercise_number in range(1, num_exercises + 1):
        print(f"\n🔹 EJERCICIO {exercise_number}")
        
        # Obtener tiempo de inicio
        while True:
            start_input = input(f"Tiempo de inicio del ejercicio {exercise_number}: ").strip()
            
            if start_input == "":
                print("⚠️  Debes ingresar un tiempo de inicio.")
                continue
            
            if start_input.lower() in ['fin', 'end']:
                start_time = duration
            else:
                start_time = time_to_seconds(start_input)
                if start_time is None:
                    continue
                if start_time > duration:
                    print(f"⚠️  El tiempo de inicio no puede ser mayor a la duración del video ({seconds_to_time(duration)})")
                    continue
            break
            
        # Obtener tiempo de fin
        while True:
            end_input = input(f"Tiempo de fin del ejercicio {exercise_number}: ").strip()
            
            if end_input.lower() in ['fin', 'end']:
                end_time = duration
            else:
                end_time = time_to_seconds(end_input)
                if end_time is None:
                    continue
                if end_time > duration:
                    print(f"⚠️  El tiempo de fin no puede ser mayor a la duración del video ({seconds_to_time(duration)})")
                    continue
                if end_time <= start_time:
                    print("⚠️  El tiempo de fin debe ser mayor al tiempo de inicio.")
                    continue
            break
        
        # Obtener nombre del ejercicio (opcional)
        exercise_name = input(f"Nombre del ejercicio {exercise_number} (opcional): ").strip()
        if not exercise_name:
            exercise_name = f"Ejercicio_{exercise_number}"
        
        # Sanitizar nombre del archivo
        exercise_name = "".join(c for c in exercise_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        exercise_name = exercise_name.replace(' ', '_')
        
        segments.append({
            'number': exercise_number,
            'name': exercise_name,
            'start': start_time,
            'end': end_time,
            'duration': end_time - start_time
        })
        
        print(f"✅ Ejercicio {exercise_number} configurado:")
        print(f"   📝 Nombre: {exercise_name}")
        print(f"   ⏰ Tiempo: {seconds_to_time(start_time)} - {seconds_to_time(end_time)}")
        print(f"   ⏱️  Duración: {seconds_to_time(end_time - start_time)}")
    
    if not segments:
        print("❌ No se configuraron ejercicios.")
        return
    
    # Mostrar resumen
    print("\n" + "="*60)
    print("📋 RESUMEN DE EJERCICIOS A PROCESAR")
    print("="*60)
    total_duration = 0
    for segment in segments:
        print(f"🔹 {segment['name']}")
        print(f"   ⏰ {seconds_to_time(segment['start'])} - {seconds_to_time(segment['end'])}")
        print(f"   ⏱️  Duración: {seconds_to_time(segment['duration'])}")
        total_duration += segment['duration']
    
    print(f"\n📊 Total de ejercicios: {len(segments)}")
    print(f"⏱️  Duración total de recortes: {seconds_to_time(total_duration)}")
    
    # Confirmar procesamiento
    confirm = input("\n¿Proceder con el corte de videos? (s/n): ").strip().lower()
    if confirm not in ['s', 'si', 'sí', 'y', 'yes']:
        print("❌ Operación cancelada.")
        return
    
    # Procesar videos
    print("\n" + "="*60)
    print("🎬 PROCESANDO VIDEOS")
    print("="*60)
    print(f"📊 Total de ejercicios a procesar: {len(segments)}")
    print("-"*60)
    
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    successful_cuts = 0
    
    for i, segment in enumerate(segments, 1):
        try:
            # Mostrar progreso general
            show_progress_bar(i-1, len(segments), f'🎬 Progreso general', f'({i-1}/{len(segments)} completados)', 50)
            
            print(f"\n🔄 Procesando {segment['name']} ({i}/{len(segments)})...")
            print(f"   ⏰ Desde {seconds_to_time(segment['start'])} hasta {seconds_to_time(segment['end'])}")
            
            # Crear nombre del archivo de salida
            output_filename = f"{base_name}_{segment['name']}.mp4"
            output_path = os.path.join(video_output_folder, output_filename)
            
            # Evitar sobrescribir archivos existentes
            counter = 1
            while os.path.exists(output_path):
                output_filename = f"{base_name}_{segment['name']}_{counter}.mp4"
                output_path = os.path.join(video_output_folder, output_filename)
                counter += 1
            
            print(f"   💾 Guardando como: {output_filename}")
            
            # Procesar el video con progreso
            success, error = process_video_with_progress(
                video_path, 
                output_path, 
                segment['start'], 
                segment['duration'],
                segment['name']
            )
            
            # Verificar si el archivo se creó exitosamente
            if os.path.exists(output_path) and os.path.getsize(output_path) > 10240:  # Al menos 10KB
                successful_cuts += 1
                file_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
                print(f"✅ {segment['name']} guardado exitosamente ({file_size:.1f} MB)")
            else:
                print(f"❌ Error procesando {segment['name']}")
                if error:
                    print(f"   📝 Detalles: {error[:200]}...")
                if os.path.exists(output_path):
                    size = os.path.getsize(output_path)
                    print(f"   📄 El archivo existe pero es muy pequeño ({size} bytes)")
                    
        except Exception as e:
            print(f"❌ Error general procesando {segment['name']}: {str(e)}")
    
    # Mostrar progreso final completado
    show_progress_bar(len(segments), len(segments), f'🎬 Progreso general', f'({len(segments)}/{len(segments)} completados)', 50)
    
    # Resumen final
    print("\n" + "="*60)
    print("🎉 PROCESO COMPLETADO")
    print("="*60)
    print(f"✅ Videos procesados exitosamente: {successful_cuts}/{len(segments)}")
    print(f"📁 Ubicación: {video_output_folder}")
    
    if successful_cuts < len(segments):
        print(f"⚠️  {len(segments) - successful_cuts} video(s) fallaron durante el procesamiento")

def check_ffmpeg():
    """
    Verifica que FFmpeg esté disponible y funcionando
    """
    try:
        # Intentar ejecutar ffmpeg para verificar que está disponible
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=10)
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
        return False

def main():
    print("🎬 CORTADOR DE VIDEOS DE EJERCICIOS")
    print("="*50)
    
    # Verificar si ffmpeg-python está instalado
    try:
        import ffmpeg
        print("✅ ffmpeg-python instalado correctamente")
    except ImportError:
        print("❌ Error: La librería 'ffmpeg-python' no está instalada.")
        print("Para instalarla, ejecuta: pip install ffmpeg-python")
        return
    
    # Verificar que FFmpeg esté disponible
    print("🔍 Verificando FFmpeg...")
    if not check_ffmpeg():
        print("❌ Error: FFmpeg no está disponible.")
        print("Necesitas instalar FFmpeg manualmente:")
        print("  Windows: https://ffmpeg.org/download.html")
        print("  macOS: brew install ffmpeg")
        print("  Linux: sudo apt install ffmpeg")
        return
    else:
        print("✅ FFmpeg disponible y funcionando")
    
    # Solicitar ruta del video
    while True:
        video_path = input("\n📹 Ingresa la ruta del video (MP4, MKV, AVI, MOV, etc.): ").strip().strip('"')
        
        if not video_path:
            print("⚠️  Debes ingresar una ruta de video.")
            continue
            
        if not os.path.exists(video_path):
            print(f"❌ Error: El archivo '{video_path}' no existe.")
            continue
            
        if not video_path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.m4v', '.webm')):
            print("⚠️  Advertencia: El archivo no tiene una extensión de video reconocida.")
            print("   Formatos soportados: MP4, MKV, AVI, MOV, FLV, WMV, M4V, WEBM")
            confirm = input("¿Continuar de todos modos? (s/n): ").strip().lower()
            if confirm not in ['s', 'si', 'sí', 'y', 'yes']:
                continue
        
        break
    
    # Solicitar carpeta de salida
    default_output = os.path.join(os.path.dirname(video_path), "ejercicios_separados")
    output_folder = input(f"\n📁 Carpeta de salida (Enter para usar '{default_output}'): ").strip().strip('"')
    
    if not output_folder:
        output_folder = default_output
    
    # Procesar el video
    create_cut_segments(video_path, output_folder)
    
    input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    main()