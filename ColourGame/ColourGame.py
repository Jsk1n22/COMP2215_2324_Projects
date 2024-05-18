from machine import Pin,SPI,PWM
import framebuf
import time
import os
import random
import FONTS
from FONTS import *
from LCD_Class import LCD_1inch3

def character(asc,xt,yt,sz,r,g,b):  # Single character sz is size: 1 or 2
    cc = getColour(r,g,b)
    bg = 0xffff
    code = asc * 5    # 5 bytes per character
    for ii in range(5):
        line = FONT[code + ii]
        for yy in range(8):
            LCD.pixel(ii*sz+xt,yy*sz+yt,bg)
            if sz > 1:
                LCD.pixel(ii*sz+xt+1,yy*sz+yt,bg)
                LCD.pixel(ii*sz+xt,yy*sz+yt+1,bg)
                LCD.pixel(ii*sz+xt+1,yy*sz+yt+1,bg)
            if sz == 3:
                LCD.pixel(ii*sz+xt,  yy*sz+yt+2,bg)
                LCD.pixel(ii*sz+xt+1,yy*sz+yt+2,bg)
                LCD.pixel(ii*sz+xt+2,yy*sz+yt+2,bg)
                LCD.pixel(ii*sz+xt+2,yy*sz+yt,bg)
                LCD.pixel(ii*sz+xt+2,yy*sz+yt+1,bg)
                
            if (line >> yy) & 0x1:
                LCD.pixel(ii*sz+xt,yy*sz+yt,cc) 
                if sz > 1:
                    LCD.pixel(ii*sz+xt+1,yy*sz+yt,cc)
                    LCD.pixel(ii*sz+xt,yy*sz+yt+1,cc)
                    LCD.pixel(ii*sz+xt+1,yy*sz+yt+1,cc)
                if sz == 3:
                    LCD.pixel(ii*sz+xt,  yy*sz+yt+2,cc)
                    LCD.pixel(ii*sz+xt+1,yy*sz+yt+2,cc)
                    LCD.pixel(ii*sz+xt+2,yy*sz+yt+2,cc)
                    LCD.pixel(ii*sz+xt+2,yy*sz+yt,cc)
                    LCD.pixel(ii*sz+xt+2,yy*sz+yt+1,cc)
                                    
def prnt_st(asci,xx,yy,sz,r,g,b):  # Text string
    if sz == 1: move = 6
    if sz == 2: move = 11
    if sz == 3: move = 17 
    for letter in(asci):
        asci = ord(letter)
        character(asci,xx,yy,sz,r,g,b)
        xx = xx + move

def drawUI():
    #A
    LCD.fill_rect(208,15,30,30,LCD.red)
    LCD.rect(208,15,30,30,LCD.black)

    #B
    LCD.fill_rect(208,75,30,30,LCD.yellow)
    LCD.rect(208,75,30,30,LCD.black)

    #X
    LCD.fill_rect(208,135,30,30,LCD.green)
    LCD.rect(208,135,30,30,LCD.black)

    #Y
    LCD.fill_rect(208,195,30,30,LCD.blue)
    LCD.rect(208,195,30,30,LCD.black)

    #title
    LCD.fill_rect(0,0,150,35,LCD.white)
    LCD.rect(0,0,150,35,LCD.black)
    prnt_st("Score: "+str(score), 5,5,3, 255,0,0)

def newColour(oldColour):
    newColour = colours[random.randint(0,3)]
    while newColour==oldColour:
        newColour=colours[random.randint(0,3)]
    return newColour
LCD = LCD_1inch3()
LCD.fill(LCD.white)
LCD.show()

score=0
colour=LCD.white
colours=[LCD.red, LCD.yellow, LCD.green, LCD.blue]

keyA = Pin(15,Pin.IN,Pin.PULL_UP)
keyB = Pin(17,Pin.IN,Pin.PULL_UP)       
keyX = Pin(19 ,Pin.IN,Pin.PULL_UP)      
keyY= Pin(21 ,Pin.IN,Pin.PULL_UP)
up = Pin(2,Pin.IN,Pin.PULL_UP)
dowm = Pin(18,Pin.IN,Pin.PULL_UP)
left = Pin(16,Pin.IN,Pin.PULL_UP)
right = Pin(20,Pin.IN,Pin.PULL_UP)
ctrl = Pin(3,Pin.IN,Pin.PULL_UP)
prnt_st("Score: 0", 5,5,3, 255,0,0)

while(1):
    if keyA.value() == 0:
        if colour==LCD.red:
            score+=1
        colour=newColour(LCD.red)
        LCD.fill(colour)
            
    if(keyB.value() == 0):
        if colour==LCD.yellow:
            score+=1
        colour=newColour(LCD.yellow)
        LCD.fill(colour)   
            
    if(keyX.value() == 0):
        if colour==LCD.green:
            score+=1
        colour=newColour(LCD.green)
        LCD.fill(colour)
            
    if(keyY.value() == 0):
        if colour==LCD.blue:
            score+=1
        colour=newColour(LCD.blue)
        LCD.fill(colour)
    drawUI()
    LCD.show()
    