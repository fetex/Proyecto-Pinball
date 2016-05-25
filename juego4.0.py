from tkinter import*
import time

###### VENTANA INICIAL :(VI)
vnt = Tk()
vnt.title("PINBALL EXTREME")
vnt.geometry("800x300")
vnt.resizable(width=False,height=False)
vnt.config(bg="gray")
##### Imagen de fondo del Menú 
fondo= PhotoImage(file="fondo.gif")
etimagen = Label(vnt,image=fondo).place(x=0,y=0)
imagen=PhotoImage(file="espacio.gif")

  ###Manual de usuario
def manual():
    ma = open ("Manual de Usuario.txt","a")
    ma.write("Pinball Extreme es un juego basado en una canica que colisona con unos obstaculos\n")
    ma.write("donde cada uno le brinda un puntaje, la paleta izquierda se mueve con la teclaz\n")
    ma.write("y la paleta derecha se mueve con la tecla v, el fin del juego es no dejar que llegue al la line limite")
    ma.close()
  
puntaje = 0
vidas = 3


#### VENTANA DEL JUEGO
def nueva():
    global puntaje
    global vidas
    global nombre
    global ball
    v = Tk()
    v.title("PINBALL EXTREME")
    v.resizable(width=False,height=False)   
    c = Canvas(v,width=700,height=600) 
    c.pack()
    #### Limites del juego
    c.create_line(10,10,10,590)
    c.create_line(650,100,650,590)
    c.create_line(10,570,650,570,fil="red")
    c.create_line(300,529,450,529,fill="white")
    c.create_line(100,530,270,530,fill="white")
    ### Creación Canica
    ball= { "dx": 5,"dy": -20, "obj":c.create_oval( 660, 550,680,570, fill= "yellow")}
    #### Variables Puntaje y Vidas: cantidad de bolas restante que posee el jugador 
    puntaje=0
    vidas= 3
        
    #####################################
    ### FUNCION GUARDAR PARTIDA #########
    #####################################
    def game_save():
        global ball
        juego = open("Partidad Guardada.txt","w")
        ball =  c.coords(ball["obj"])
        y = ",".join(str(i)for i in ball)
        juego.write(y + "\n")
        juego.write(str(puntaje) + "\n")
        juego.write(str(vidas) + "\n")
        juego.write(str(nombre.get()))
        juego.close()
    ######################################
    ###FUNCION ENCARGADA DE MOVER BOLA####
    ######################################
    def moverBall1():
        global puntaje
        global vidas
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

        if ( 5 < x < 15 ) and ( 10 <= y <= 590 ):
            ball["dx"]*=-1
            
        ##################################
        #### Colisiones entre objetos ####
        ##################################
   
        ###Colision primer obstaculo                  
        if ( 295 < x < 305 ) and ( 100 <= y <= 200 ):
            puntaje+=10
            ball["dx"]*=-1
            
        if ( 95 <= y <= 105 ) and ( 200 <= x <= 300 ):
            puntaje+=10
            ball["dy"]*=-1
            
        if ( 195 < x < 205 ) and ( 100 <= y <= 200 ):
            puntaje+=10
            ball["dx"]*=-1
           
        if ( 195 <= y <= 205 ) and ( 200 <= x <= 300 ):
            puntaje+=10
            ball["dy"]*=-1
                 
       ###Colision segundo obstaculo                  
        if ( 595 < x < 605 ) and ( 100 <= y <= 200 ):
            puntaje+=20
            ball["dx"]*=-1
             
        if ( 95 <= y <= 105 ) and ( 500 <= x <= 600 ):
            puntaje+=20
            ball["dy"]*=-1
        
        if ( 495< x < 505 ) and (100 <= y <= 200):
            puntaje+=20
            ball["dx"]*=-1
             
        if ( 195 <= y <= 205 ) and ( 500 <= x <= 600 ):
            puntaje+=20
            ball["dy"]*=-1
             
        ###Colision tercer obstaculo
             
        if ( 105 < x < 115 ) and ( 300 <= y <= 400 ):
            puntaje+=15
            ball["dx"]*=-1
            
        if ( 295 <= y <= 305 ) and ( 10 <= x <= 110 ):
            puntaje+=15         
            ball["dy"]*=-1

        if ( 5 < x < 15 ) and ( 300 <= y <= 400 ):
            puntaje+=15
            ball["dx"]*=-1

        if ( 395 <= y <= 405 ) and ( 10 <= x <= 110 ):
            puntaje+=15
            ball["dy"]*=-1             

        ###Colision cuarto obstaculo

        if ( 545 < x < 555 ) and ( 350 <= y <= 450 ):
            puntaje+=25
            ball["dx"]*=-1

            puntaje = puntaje +100
        if ( 345 <= y <= 355 ) and ( 450 <= x <= 550 ):
            puntaje+=25
            ball["dy"]*=-1

        if ( 445 < x < 455 ) and ( 350 <= y <= 450 ):
            puntaje+=25
            ball["dx"]*=-1

        if ( 445 <= y <= 455 ) and ( 450 <= x <= 550 ):
            puntaje+=25
            ball["dy"]*=-1

        ###Colision paletas
                
        #if  ( 525 <= y <= 535 ) and ( 100 <= x <= 270 ):
            ball["dy"]*=-1
            ball["dx"]*=-2
        #if  ( 525 <= y <= 535 ) and ( 300 <= x <= 470 ):
            ball["dy"]*=-1
        if ( 528 <= y <= 532 ) and ( 100 <= x <= 210 ):
            ball["dy"]*=-1
            
        if  ( 524<=y<534) and (300<=x<= 450):
            ball["dy"]*=-1
                    
        #### Disminución de vidas 
        if (565<=y<=575) and (10 <= x <= 650):
            vidas = vidas - 1

        #if puntaje == 20:
            #vidas = vidas + 1
  
        ball["dy"] = ball["dy"] + 0.35
   
        c.move(ball["obj"], ball["dx"], ball["dy"])
        v.after(70, moverBall1)

        ##### Indicador de Putaje 
        punt = Label(v,text="Puntos Obtenidos"+str(puntaje),bg="green",relief=SOLID).place(x=400,y=20)
        ##### Indicador de vidas
        vida = Label(v,text="Vidas restantes"+"-"+str(vidas),bg="green",relief=SOLID).place(x=400,y=40)
             
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
    ##################################
    #####Funcion Movimiento paletas###
    ##################################
    def mover_pal(event):
        '''Funcion encargada de dezplazar verticalmente las paletas'''
        global pal1,pal2
        tecla1 = repr(event.char)
        tecla2 = repr(event.char)
        ####### Paleta lado izquierdo#####
        if (tecla1=="'z'"):            
            c.delete(pal1)       
            pal1 = c.create_polygon((100,530),(100,550),(270,550),(270,530),fill="blue")
            c.update()
            c.delete(pal1)
          
            c.after(115)
            pal1= c.create_polygon((100,550),(100,570),(270,570),(270,550),fill="blue")
        ###### Paleta lado derecho#####
        if (tecla2 == "'v'"):
            c.delete(pal2)
            pal2 = c.create_polygon((300,530),(300,550),(470,550),(470,530),fill="blue")
            c.update()
            c.delete(pal2)
            c.after(115)
            pal2 = c.create_polygon((300,550),(300,570),(470,570),(470,550),fill="blue")
                     
    global pal1
    global pal2
    c.bind("<Key>",mover_pal)
    c.focus_set()
    
    ## Paletas:
    pal1 = c.create_polygon((100,550),(100,570),(270,570),(270,550),fill="blue")
    pal2 = c.create_polygon((300,550),(300,570),(470,570),(470,550),fill="blue")

    ##### BOTON GUARDAR PÁRTIDA
    guardar = Button(v,text="Guardar Partida",bg="red",command=game_save)
    guardar.pack()
     
###### Botones ventana inicial
nombre= StringVar()
et = Label(vnt,text="Nombre de Usuario",bg="blue").place(x=10,y=240)
bnt = Button(vnt,text="Guardar usuario",command=nueva,bg="red").place(x=320,y=240)
cam= Entry(vnt,textvariable=nombre,width=20).place(x=140,y=240)
manual = Button(vnt,text="Manual del Usuario",bg="green",command=manual).place(x=520,y=240)
##############################################################################################
######Cuandricula de guia: encargada de facilitarme el diseño y ubicación de los obstaculos###
##############################################################################################
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



