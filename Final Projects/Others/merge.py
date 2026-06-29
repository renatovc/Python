from pypdf import PdfMerger

def combinar_documento(nombre_doc, nombre_apostilla, nombre_salida):
    merger = PdfMerger()
    # Añade primero el documento principal
    merger.append(nombre_doc)
    # Añade la apostilla como segunda página
    merger.append(nombre_apostilla)
    # Guarda el archivo final combinado
    merger.write(nombre_salida)
    merger.close()
    print(f"¡Archivo generado con éxito!: {nombre_salida}")

# Ejemplo de uso para tus notas:
combinar_documento(
    "Renato_Vasquez_High_School_Diploma.pdf", 
    "Renato_Vasquez_High_School_Diploma_Apostilla.pdf", 
    "Renato_Vasquez_Technical_Title_Certificate.pdf"
)