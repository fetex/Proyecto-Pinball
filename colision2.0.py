from tkinter import*
from math import*

###Ventana del juego 
ventana = Tk()
c = Canvas(ventana, width = 700, height=600)
c.pack()
###Obstaculos 
c.create_line(200, 0, 200, 400)##Linea del centro 
rombo=c.create_polygon((350,200),(250,300),(350,400),(450,300),fill="blue")###Rombo
triangulo = c.create_polygon(110,400,110,500,200,450,fill="orange")##triangulo 
#### pelota del pinball
ball = {"dx": 5, "dy":8, "obj":c.create_oval((190, 190), (210, 210), fill= "black")}
    
def moverBall():
    '''Este procedimiento hace que la pelota se mueva'''
    x1, y1, x2, y2 = c.coords(ball["obj"])
    x = (x1+x2)//2
    y = (y1+y2)//2
    dx = 4
    if x<10 or x>690:
        ball["dx"]*=-1
    if y<10 or y>590:
        ball["dy"]*=-1
    cor= c.coords(ball["obj"])
   
  ##centro de la pelota
    centro_ball = [((cor[0]+cor[2])/2),((cor[1]+cor[3])/2)]

    radio = 10
 
    diametro = fabs(cor[0] - cor[2])
    

    ##Distancias del Rombo 
    d1= (sqrt(((300-200)**2)+((250-350)**2)))
    d2= (sqrt(((350-250)**2)+((400-300)**2)))
    d3= (sqrt(((450-350)**2)+((300-400)**2)))
    d4= (sqrt(((350-450)**2)+((200-300)**2)))
    #d5= (sqrt(((400-0)**2)+((0-200)**2)))


    ##Distancia linea punto:
    dp1 = fabs(((300-200)*centro_ball[0])-((250-350)*centro_ball[1])+(250*200)-(300*350))//d1
    dp2 = fabs(((350-250)*centro_ball[0])-((400-300)*centro_ball[1])+(400*250)-(350*300))//d2
    dp3 = fabs(((450-350)*centro_ball[0])-((300-400)*centro_ball[1])+(300*350)-(450*400))//d3
    dp4 = fabs(((350-450)*centro_ball[0])-((200-300)*centro_ball[1])+(200*450)-(350*300))//d4
    #dp2 = fabs(((400-0)*centro_ball[0])-((0-200)*centro_ball[1])+(0*0)-(400*200))//d5
    corR= c.coords(rombo)


    #if(x < 250 or x > 350):
       
    

    ''''if (dp1<=diametro or dp2 >= diametro   ):'''
        
   if (dp1 == 0 or diametro == 0):
        print("jeex")
    
        ball["dx"]*=-1
        ball["dy"]*=-1
               
        #print("funciona")
    if (x < 350,200 < 250,300 or x > 350,400 > 450,300):
        x= 350,200
        y = 350,400
        #print("funciona2")
    elif(x < 250,300 < 350,200 or x > 450,300 > 350,400):
        x = 250,300
        y = 450,30
        #print("funciona3")"""'''
    

        
               
    c.move(ball["obj"], ball["dx"], ball["dy"])

    ventana.after(50, moverBall)





ventana.after(10, moverBall)
ventana.mainloop()
