from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
w, h = A4
c = canvas.Canvas("Factura.pdf", pagesize=A4)
# Ubicar el logo en el extremo superior izquierdo.
img = ImageReader("Images/Icons/corazon.png")
# Obtener el ancho y alto de la imagen.
img_w, img_h = img.getSize()
# Crear texto
# c.drawImage(img, 0, h - img_h)
c.drawString(0,0,"Hola mundo")

c.save()