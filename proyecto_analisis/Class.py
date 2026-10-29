from PIL import Image
image = Image.open('Images/lake.jpg')
w, h = image.size
new_image = image.resize((round(w/3), round(h/3)))
new_image.save('Images/lake_resize.jpg')