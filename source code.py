import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# build a list of 9 images
images=[]
for i in range(1, 10):
    images.append(image)

# create a contact sheet from different brightnesses with black lines
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width * 3, first_image.height * 3 + 150))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x + first_image.width == contact_sheet.width:
        x = 0
        y = y + first_image.height + 50
    else:
        x = x + first_image.width

# Font
font = PIL.ImageFont.truetype(font = 'readonly/fanwood-webfont.ttf', size = 50)

#list of texts
texts = []
for ch in range(0, 3):
    for inten in [0.1, 0.5, 0.9]:
        texts.append('channel {} intensity {}'.format(ch, inten))

x = 15
y = 3 + first_image.height
for text in texts:
    # Paste text
    PIL.ImageDraw.ImageDraw(contact_sheet).text((x, y), text, font = font)
    if x + first_image.width - 15 == contact_sheet.width:
        y = y + first_image.height + 50
        x = 15
    else:
        x = x + first_image.width

# changing colors
x = 0
y = 0
intensity  = 0.1
num_pixels = contact_sheet.height * contact_sheet.width
for pixel in range(0,num_pixels):
    # get RGB of a pixel
    r, b, g = contact_sheet.getpixel((x,y))
    
    # choosing channel
    if y < first_image.height + 50:
        contact_sheet.putpixel((x,y),(int(intensity * r), b, g))
    elif y < (first_image.height + 50) * 2:
        contact_sheet.putpixel((x,y),(r, int(intensity * b), g))
    else:
        contact_sheet.putpixel((x,y),(r, b, int(intensity * g)))
    
    #updating coords
    if x + 1 == first_image.width:
        intensity = 0.5
        x += 1
    elif x + 1 == first_image.width * 2:
        intensity = 0.9
        x += 1
    elif x + 1 == first_image.width * 3:
        intensity = 0.1
        y += 1
        x = 0
    else:
        x += 1

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
