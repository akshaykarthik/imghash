import hashlib
import sys
import Image
import ImageDraw

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        name = sys.argv[1]
    else:
        name = raw_input("Please enter the text you want to imghash: ")

    hash = hashlib.sha384(name.lower()).digest()
    image = Image.new('RGBA',(512,512))
    map = [(ord(r),ord(g),ord(b),255) for r,g,b in zip(hash[0::3], hash[1::3], hash[2::3])]

    ox = 0
    oy = 0
    mapk = 0
    for x in [128,256,384,512]:
        for y in [128,256,384,512]:
            image.paste(map[mapk],(ox,oy,x,y))
            mapk += 1
            oy = y
        ox = x
        oy = 0
    draw = ImageDraw.Draw(image)
    draw.text((10,10),name, fill=(0,0,0,255))

    del draw
    image.save(name+".png")
