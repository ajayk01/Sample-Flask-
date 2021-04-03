import PIL
image = PIL.Image.open("geeks.jpg")
image1 = PIL.Image.open(r"C:\Users\snpaj\Desktop\sample_flask\image-temp\12-b-t.jpg")


width, height = image.size
print("Geeks",width, height)

width, height = image1.size

print(width, height)