from PIL import Image


def resize(img, new_width):
    width,height =  img.size
    ratio = height/width
    print(ratio)
    new_height = int(ratio * new_width)
    print(new_height)
    print(new_width)
    resized_image =  img.resize((new_width,new_height))
    print(new_width)
    return resized_image
 
img = Image.open("images/BEEF.jpg")

#print(img)
# we found img variable has some properites  such as size

#print(img.size) # return ( w:2940,h: 3920)

# so it has also  a methods such as 


#imgr = img.resize((100,100)) # resize((w,h))

im_resized = resize(img,200)

im_resized.show()