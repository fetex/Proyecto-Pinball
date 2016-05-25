from tkinter import*
import time

###### VENTANA INICIAL :(VI)
vnt = Tk()
vnt.title("PINBALL EXTREME")
vnt.geometry("800x300")
vnt.resizable(width=False,height=False)
vnt.config(bg="gray")

fondo= PhotoImage(file="fondo.gif")
etimagen = Label(vnt,image=fondo).place(x=0,y=0)
imagen=PhotoImage(file="espacio.gif")

#### VENTANA DEL JUEGO
def nueva():
    global imagen
    v = Tk()
    v.title("PINBALL EXTREME")
    v.resizable(width=False,height=False)   
    c = Canvas(v,width=700,height=600) 
    c.pack()

    
    
    #### Area del juego
    c.create_line(10,10,690,10) ##line 1
    c.create_line(10,10,10,590)##line 2
    c.create_line(10,590,690,590)##lie 3
    c.create_line(690,10,690,590)#Line 4
    c.create_line(650,100,650,590)
    ### Creación Canica
    ball= { "dx": 5,"dy": -20, "obj":c.create_oval( 660, 550,680,570, fill= "yellow")}

    def moverBall1():
        '''Esta funcion es la encargada de producir el movimiento de la bola y colisones con objetos'''
    
        x1, y1, x2, y2 = c.coords(ball["obj"])
        x = (x1+x2)//2
        y = (y1+y2)//2        
        if x<10 or x>690:
            ball["dx"]*=-1
        if  y<10 or y>590:
            ball["dy"]*=-1

        if  ( 650 < x < 690 ) and ( y >= 100):
            ball["dx"]*=-1
            
        ##################################
        #### Colisiones entre objetos ####
        ##################################

        
        ###Colision primer obstaculo                  
        if ( 295 < x < 305 ) and ( 100 <= y <= 200 ):
            ball["dx"]*=-1.02
            
        if ( 95 <= y <= 105 ) and ( 200 <= x <= 300 ):
            ball["dy"]*=-1

        if ( 195 < x < 205 ) and ( 100 <= y <= 200 ):
            ball["dx"]*=-1

        if ( 195 <= y <= 205 ) and ( 200 <= x <= 300 ):
            ball["dy"]*=-1       
         
       ###Colision segundo obstaculo                  
        if ( 595 < x < 605 ) and ( 100 <= y <= 200 ):   
            ball["dx"]*=-1.02
            
        if ( 95 <= y <= 105 ) and ( 500 <= x <= 600 ):
            ball["dy"]*=-1

        if ( 495< x < 505 ) and (100 <= y <= 200):
             ball["dx"]*=-1

        if ( 195 <= y <= 205 ) and ( 500 <= x <= 600 ):
             ball["dy"]*=-1

        ###Colision tercer obstaculo
             
        if ( 105 < x < 115 ) and ( 300 <= y <= 400 ):   
            ball["dx"]*=-1
            
        if ( 295 <= y <= 305 ) and ( 10 <= x <= 110 ):
            ball["dy"]*=-1

        if ( 5 < x < 15 ) and ( 300 <= y <= 400 ):
            ball["dx"]*=-1

        if ( 395 <= y <= 405 ) and ( 10 <= x <= 110 ):
            ball["dy"]*=-1             

        ###Colision cuarto obstaculo

        if ( 545 < x < 555 ) and ( 350 <= y <= 450 ):   
            ball["dx"]*=-1

            
        if ( 345 <= y <= 355 ) and ( 450 <= x <= 550 ):
            ball["dy"]*=-1

        if ( 445 < x < 455 ) and ( 350 <= y <= 450 ):   
            ball["dx"]*=-1

        if ( 445 <= y <= 455 ) and ( 450 <= x <= 550 ):
            ball["dy"]*=-1
        ###Colision paletas

        if ( 525 <= y <= 535 ) and ( 100 <= x <= 210 ):
            ball["dy"]*=-1
        if ( 525 <= y <= 535 ) and ( 300 <= x <= 450 ):
            ball["dy"]*=-1
        
        ball["dy"] = ball["dy"] + 0.35
       
            
        

            
        c.move(ball["obj"], ball["dx"], ball["dy"])
        v.after(70, moverBall1)
        
    v.after(70, moverBall1)
#### Nombre Usuario 
   
    usuario = Label(v,text=str(nombre.get()),bg="green").place(x=135,y=20)
    et = Label(v,text="NOMBRE USUARIO",bg="red").place(x=20,y=20)
    
#### Obstaculos         
    c.create_polygon((200,100),(200,200),(300,200),(300,100),fill="red")##obstaculo 1
    c.create_polygon((500,100),(500,200),(600,200),(600,100),fill="gray")##obstaculo 2
    c.create_polygon((10,300),(10,400),(110,400),(110,300),fill="black")##obstaculo 3
    c.create_polygon((450,350),(450,450),(550,450),(550,350),fill="red")##obstaculo 4
        
    vnt.destroy()

#####Movimiento paletas
    def mover_pal(event):
        global pal1,pal2
        tecla1 = repr(event.char)
        tecla2 = repr(event.char)
        tecla3 = repr(event.char)
        if (tecla1=="'z'"):            
            c.delete(pal1)       
            pal1 = c.create_polygon((100,530),(100,550),(210,550),(210,530),fill="blue")
            c.update()
            c.delete(pal1)
          
            c.after(100)
            pal1= c.create_polygon((100,550),(100,570),(210,570),(210,550),fill="blue")

        if (tecla2 == "'c'"):
            c.delete(pal2)
            pal2 = c.create_polygon((300,530),(300,550),(450,550),(450,530),fill="blue")
            c.update()
            c.delete(pal2)
            c.after(100)
            pal2 = c.create_polygon((300,550),(300,570),(450,570),(450,550),fill="blue")
            
            
    global pal1
    global pal2
    c.bind("<Key>",mover_pal)
    c.focus_set()
    
    ## Paletas:
    pal1 = c.create_polygon((100,550),(100,570),(210,570),(210,550),fill="blue")
    pal2 = c.create_polygon((300,550),(300,570),(450,570),(450,550),fill="blue")
    
  
  
###### Botones ventana inicial
nombre= StringVar()
et = Label(vnt,text="Nombre de Usuario",bg="blue").place(x=10,y=240)
bnt = Button(vnt,text="Guardar usuario",command=nueva,bg="red").place(x=320,y=240)
cam= Entry(vnt,textvariable=nombre,width=20).place(x=140,y=240)

######Cuandricula de guia: encargada de facilitarme el diseño y ubicación de los obstaculos
##width=700
##    height=600
##    linea_distance = 100
##
##    def cuadricula(c, line_distance):
##        for x in range(line_distance,width,line_distance):
##            c.create_line(x, 0, x, height, fill="red")        
##        for y in range(line_distance,height,line_distance):c.create_line(0, y, width, y, fill="red")   
##
##  cuadricula(c,100)
vnt.mainloop()



