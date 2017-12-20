from PIL import Image
import pygame
from math import fabs

pygame.init()

display=pygame.display.set_mode((1300,750))

myimg="iris.png"

bg = pygame.image.load(myimg)

display.blit(bg,(0,0))

im = Image.open(myimg) #Can be many different formats.
pix = im.load()
dim,ht=im.size #Get the width and hight of the image for iterating over
#for i in range(dim):
 #   print str(i)+":"+ str(pix[i,int(ht/2)]) #Get the RGBA Value of the a pixel of an image
im.save(myimg)

ct=0
start=0
prev=0
l=[0,0,0]
ref=[]

#horizontally
for i in range(dim):
    l[0],l[1],l[2]=pix[i,int(ht/2)][0:3]
    
    if l[0]<12 and l[1]<12 and l[2]<12:
        ct+=1
        if prev==0:
            prev=1
            start=i
                
    if ct==20 and i-start<40:
        ref.append(start)
        start=0
        prev=0
        ct=0
        break
ct=0
prev=0
start=0
for i in range(dim-1,0,-1):
    l[0],l[1],l[2]=pix[i,int(ht/2)][0:3]
    
    if l[0]<12 and l[1]<12 and l[2]<12:
        ct+=1
        
        if prev==0:
            prev=1
            start=i
                
    if ct==20 and start-i<40:
        ref.append(start)
        start=0
        prev=0
        ct=0
        break


#print ref
mp=[0]
mp[0]=(ref[0]+ref[1])/2
rad1=mp[0]-ref[0]

reduction=0

o_ref=[]

while len(o_ref)!=2:

    o_ref=[]

    ct=0
    prev=0
    start=0
    f=[0,0,0]

    for i in range(0,mp[0]-int(rad1)-40):#mp[0]-int(rad1)-40,16,-1
        l[0],l[1],l[2]=pix[i,int(ht/2)][0:3]
        f[0],f[1],f[2]=pix[i+15,int(ht/2)][0:3]
        if (f[0]-l[0])+(f[1]-l[1])+(f[2]-l[2])<-500+reduction:
            o_ref.append(i)
            break
 

    ct=0
    prev=0
    start=0

    for i in range(dim-16,mp[0]+int(rad1)+40,-1):
        l[0],l[1],l[2]=pix[i,int(ht/2)][0:3]
        f[0],f[1],f[2]=pix[i-15,int(ht/2)][0:3]
        if (f[0]-l[0])+(f[1]-l[1])+(f[2]-l[2])<-500+reduction:
            o_ref.append(i)
            break
    reduction+=10

    
#print o_ref

r1=fabs(mp[0]-o_ref[0])
r2=fabs(mp[0]-o_ref[1])
r=min(r1,r2)
pygame.draw.circle(display,(255,0,0),(mp[0],int(ht/2)),int(r),6)
pygame.draw.circle(display,(255,255,255),(mp[0],int(ht/2)),rad1,6)
pygame.display.update()




         
            
