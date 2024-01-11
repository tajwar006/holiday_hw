import pygame
import random
pygame.init()

scrwid = 500
scrhi = 600








bscr = pygame.display.set_mode((scrwid, scrhi))
bscr.fill((30,30,30))
mscr = pygame.Rect((50, 50, 400, 450))
pygame.draw.rect(bscr, (250,250,250), mscr)
q=pygame.Rect((75,350, 30, 30))
pygame.draw.rect(bscr, (190,190,190), q)
w=pygame.Rect((75,350, 30, 30))
pygame.draw.rect(bscr, (190,190,190), w)
e=pygame.Rect((110,350, 30, 30))
pygame.draw.rect(bscr, (190,190,190), e)
r=pygame.Rect((145,350, 30, 30))
pygame.draw.rect(bscr, (190,190,190), r)
t=pygame.Rect((180,350, 30, 30))
pygame.draw.rect(bscr, (190,190,190), t)
y=pygame.Rect((215,350, 30, 30))
pygame.draw.rect(bscr, (190,190,190), y)
u=pygame.Rect((250,350, 30, 30))
pygame.draw.rect(bscr, (190,190,190), u)
i=pygame.Rect((285,350, 30, 30))
pygame.draw.rect(bscr, (190,190,190), i)
o=pygame.Rect((320,350, 30, 30))
pygame.draw.rect(bscr, (190,190,190), o)
p=pygame.Rect((355,350, 30, 30))
pygame.draw.rect(bscr, (190,190,190), p)
back=pygame.Rect((390,350, 50, 30))
pygame.draw.rect(bscr, (160,250,160), back)
a=pygame.Rect((75,350, 30, 30))
pygame.draw.rect(bscr, (190,190,190), a)
s=pygame.Rect((85,390, 30, 30))
pygame.draw.rect(bscr, (190,190,190), s)
d=pygame.Rect((120,390, 30, 30))
pygame.draw.rect(bscr, (190,190,190), d)
f=pygame.Rect((155,390, 30, 30))
pygame.draw.rect(bscr, (190,190,190), f)
g=pygame.Rect((190,390, 30, 30))
pygame.draw.rect(bscr, (190,190,190), g)
h=pygame.Rect((225,390, 30, 30))
pygame.draw.rect(bscr, (190,190,190), h)
j=pygame.Rect((260,390, 30, 30))
pygame.draw.rect(bscr, (190,190,190), j)
k=pygame.Rect((295,390, 30, 30))
pygame.draw.rect(bscr, (190,190,190), k)
l=pygame.Rect((330,390, 30, 30))
pygame.draw.rect(bscr, (190,190,190), l)
ent=pygame.Rect((366,390, 60, 30))
pygame.draw.rect(bscr, (160,250,190), ent)
z=pygame.Rect((120,430, 30, 30))
pygame.draw.rect(bscr, (190,190,190), z)
x=pygame.Rect((155,430, 30, 30))
pygame.draw.rect(bscr, (190,190,190), x)
c=pygame.Rect((190,430, 30, 30))
pygame.draw.rect(bscr, (190,190,190), c)
v=pygame.Rect((225,430, 30, 30))
pygame.draw.rect(bscr, (190,190,190), v)
b=pygame.Rect((260,430, 30, 30))
pygame.draw.rect(bscr, (190,190,190), b)
n=pygame.Rect((295,430, 30, 30))
pygame.draw.rect(bscr, (190,190,190), n)
m=pygame.Rect((330,430, 30, 30))
pygame.draw.rect(bscr, (190,190,190), m)
rg1=pygame.Rect((125,130, 250, 40))
pygame.draw.rect(bscr, (190,190,190), rg1)
rg1=pygame.Rect((125,180, 250, 40))
pygame.draw.rect(bscr, (190,190,190), rg1)
rg1=pygame.Rect((125,230, 250, 40))
pygame.draw.rect(bscr, (190,190,190), rg1)
rg1=pygame.Rect((125,280, 250, 40))

pygame.draw.rect(bscr, (190,190,190), rg1)
run = True
while run:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
 
	pygame.display.update()       
pygame.quit()
