#!/usr/bin/env python

# CTF-BR Ranking-Interno
# Challenge: [Semana 2/10] - Cr4zy_h0rs3 / Creator: jh00nbr_ /  

from PIL import Image
import random


read = []
flag = "CTF-BR{XXXXXXXXXXXXXXXXX}"

for b in flag:
	read.append(ord(str(b)))


img = Image.open("original.png")
img_pix = img.convert("RGB")


for i in read:
    x = random.randint(0,266)
    y = random.randint(0,266)
    x1 = random.randint(0,266)
    y1 = random.randint(0,266)
    img_pix.putpixel((x,y),(int(i),int(x1),int(y1)))

    with open("0000000000.txt","a") as pixel:
    	pixel.write("("+str(x)+","+str(y)+')\n')


img_pix.save('encrypted.png')
