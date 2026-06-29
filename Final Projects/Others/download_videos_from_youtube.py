import yt_dlp
import shutil

def verificar_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("⚠️  ffmpeg no está instalado o no se encuentra en el PATH.")
        print("Por favor, instala ffmpeg para poder combinar audio y video.")
        return False
    return True

def progress_hook(d):
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
        if total_bytes:
            progress = d['downloaded_bytes'] / total_bytes * 100
            print(f"\rDescargando: {progress:.2f}% completado", end='')
    elif d['status'] == 'finished':
        print("\n✅ ¡Descarga completada con éxito!")

def Download(link):
    if not verificar_ffmpeg():
        return

    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

    except Exception as e:
        print("\n❌ Hubo un error al descargar el video del URL proporcionado...")
        print(f"Error: {e}")

if __name__ == "__main__":
    link = input("Pega tu link de YouTube aquí: ")
    Download(link)
