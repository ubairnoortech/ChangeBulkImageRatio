from PIL import Image

img = Image.open("images/BEEF.jpg")

print(img)
# we found img variable has some properites  such as size

print(img.size) # return ( w:2940,h: 3920)

# so it has also  a methods such as 

imgr = img.resize((100,100)) # resize((w,h))
imgr.show()