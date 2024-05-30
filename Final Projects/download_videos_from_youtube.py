from pytube import YouTube
 
def Download(link):
  yt = YouTube(link)
  yt = yt.streams.get_highest_resolution()
  try:
    yt.download()
  except:
    print("Hubo un error al descargar el video del URL proporcionado...")
  print("¡Descarga completada con éxito!")
   
link = input("Pega tu link de youtube aquí: ")
 
Download(link)