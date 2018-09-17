#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myFont = ImageFont.truetype("/Library/Fonts/Arial.ttf", size=80)
    width,height = img.size
    draw.text((width-90,0),'99',font=myFont,fill="#ff0000")
    img.save('output.jpg','jpeg')
    img.show()

if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)