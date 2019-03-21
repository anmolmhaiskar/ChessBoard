import PIL
from PIL import Image

w,h=8,8
#im=Image.open("BlackKing.jpg")
img=Image.new("RGB",(w,h),"gray")
pixels=img.load()
string="abcdefgh"
y=0
pos={}
colour={}
for i in range(w):
    x=0
    for j in range(h):
        pos.update({string[j]+str((w-i)):(x,y)})
        colour.update({string[j]+str((w-i)):"gray"})
        x=x+70
        if(i+j)%2==0:
            colour.update({string[j]+str((w-i)):"white"})
            pixels[i,j]=(255,255,255)
    y=y+70

#print(pos)

print("Enter number of white pieces and their positions:")
whitepiececount=int(input())

whiteposition=""

img=img.resize((70*w,70*h),PIL.Image.NEAREST)
#print(whiteposition)

#x=Image.alpha_composite(Image.new("RGB",(2,2),colour[pos["a3"]]).convert("RGBA").resize((70, 70)),Image.open("WhiteN.png").convert("RGBA").resize((70,70)))
#img.paste(x,pos["a3"])


for i in range(whitepiececount):
    whiteposition=input()
    x=Image.alpha_composite(Image.new("RGB",(2,2),colour[whiteposition[1:]]).convert("RGBA").resize((70,70)),Image.open("White"+whiteposition[0:1]+".png").resize((70,70)))
    img.paste(x,pos[whiteposition[1:]])

print("Enter number of white pieces and their positions:")
blackpiececount=int(input())
blackposition=""

for i in range(blackpiececount):
    blackposition=input()
    x=Image.alpha_composite(Image.new("RGB",(2,2),colour[blackposition[1:]]).convert("RGBA").resize((70,70)),Image.open("Black"+blackposition[0:1]+".png").resize((70,70)))
    img.paste(x,pos[blackposition[1:]])


img.show()