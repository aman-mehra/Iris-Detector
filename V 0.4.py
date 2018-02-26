from PIL import Image
import pygame
from math import fabs
import pylab
import numpy as np

white=(255,255,255)

im_arr=["iris.png","iris2.png","iris3.png","iris4.png"]
arr_ind=2

pygame.init()

display=pygame.display.set_mode((1300,750))

def identify(dim,ht,pix):
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
                    
        if ct>15 and float(ct)/(start-i)>0.21:
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
    return mp,r,rad1


#-----------------------------------------Display-----------------------------------
loop_ctrl=True
clock=pygame.time.Clock()
while loop_ctrl:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            loop_ctrl=False
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            arr_ind+=1
            arr_ind%=len(im_arr)

    display.fill(white)
    myimg=im_arr[arr_ind]
    bg = pygame.image.load(myimg)
    im = Image.open(myimg) #Can be many different formats.
    pix = im.load()
    dim,ht=im.size #Get the width and hight of the image for iterating over
    bg=pygame.transform.scale(bg,(dim/2,ht/2))
    display.blit(bg,(0,0))
    mp,r,rad1=identify(dim,ht,pix)
    
    #pygame.draw.circle(display,(255,0,0),(mp[0],int(ht/2)),int(r),6)
    #pygame.draw.circle(display,(255,255,255),(mp[0],int(ht/2)),rad1,6)
    pygame.draw.circle(display,(255,0,0),(mp[0]/2,int(ht/2)/2),int(r)/2,6)
    pygame.draw.circle(display,(255,255,255),(mp[0]/2,int(ht/2)/2),rad1/2,6)
    pygame.display.update()    
    clock.tick(100)

pygame.quit()
quit()
exit()




         
            
