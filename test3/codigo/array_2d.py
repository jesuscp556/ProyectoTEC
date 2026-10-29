from numpy import *



def promedio(temp):
    return temp.sum()/len(temp)

img = Image.open("Images\Bosque.jpg")
width, height = img.size
width, height = int(width), int(height)

img_gray = zeros([width,height])


for i in range(width):
    for j in range(height):
        temp = array(img.getpixel([i,j]))
        img_gray[i,j] = promedio(temp)

img_gray_2 = Image.fromarray(img_gray.transpose())

plt.imshow(img_gray_2)
# plt.imshow(img_gray.transpose())
plt.show()