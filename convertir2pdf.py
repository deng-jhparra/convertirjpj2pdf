# Convierte un conjunto de imagenes y son concatenado y convertido en un archivo pdf 
import os 
import img2pdf

directorio_raiz = 'C:\\convertir2pdf\\'
directorio_imagenes = directorio_raiz + 'imagenes\\'

imagenes_jpg = [archivo for archivo in os.listdir(directorio_imagenes) if archivo.endswith(".jpg")]
imagenes_jpg.sort()

for ind in  range(len(imagenes_jpg)):
    nombre = imagenes_jpg[ind]
    imagenes_jpg[ind] = directorio_imagenes + nombre

print(imagenes_jpg)

nombre_pdf = directorio_raiz + '\\trabajo.pdf' 
with open(nombre_pdf, 'wb') as documento:
	documento.write(img2pdf.convert(imagenes_jpg))