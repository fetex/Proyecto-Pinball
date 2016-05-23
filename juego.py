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
    
##    etmagen = Label(v,image=(imagen)).place(x=0,y=0)
   
    #### Area del juego
    c.create_line(10,10,690,10) ##line 1
    c.create_line(10,10,10,590)##line 2
    c.create_line(10,590,690,590)##lie 3
    c.create_line(690,10,690,590)
    c.create_line(650,80,650,590)
    ### Creación Canica
    ball= { "dx": 4,"dy": 3, "obj":c.create_oval( 660, 550,680,570, fill= "yellow")}
    
   
    usuario = Label(v,text=str(nombre.get()),bg="green").place(x=135,y=20)
    et = Label(v,text="NOMBRE USUARIO",bg="red").place(x=20,y=20)
    
        
#### Obstaculos
    c.create_polygon(110,400,110,500,200,450,fill="orange")###Triangulo I.I
    c.create_polygon(590,400,590,500,510,450,fill="orange")###Triangulo I.D
    c.create_polygon(350,200,250,300,350,400,450,300,fill="blue")###Rombo
    c.create_polygon(110,100,110,200,200,150,fill="orange")###Triangulo S.I
    c.create_polygon(590,100,590,200,510,150,fill="orange")###Triangulo S.D
    vnt.destroy()

     
   


#####Movimiento paletas

    def mover_pal(event):
        global pal1,pal2
        tecla1 = repr(event.char)
        tecla2 = repr(event.char)
        if (tecla1=="'z'"):            
            c.delete(pal1)       
            pal1 = c.create_polygon((160,540),(160,570),(310,520),(310,510),fill="blue")
            c.update()
            c.delete(pal1)
          
            time.sleep(0.15)
            pal1= c.create_polygon((160,540),(160,570),(310,560),(310,550),fill="blue")

        if (tecla2 == "'c'"):
            c.delete(pal2)
            pal2 = c.create_polygon((540,540),(540,570),(390,520),(390,510),fill="blue")
            c.update()
            c.delete(pal2)
            time.sleep(0.15)
            pal2 = c.create_polygon((540,540),(540,570),(390,560),(390,550),fill="blue")
            

            
            

    global pal1
    global pal2
    c.bind("<Key>",mover_pal)
    c.bind()
    c.focus_set()
    ## Paletas:
    pal1 = c.create_polygon((160,540),(160,570),(310,560),(310,550),fill="blue")
    
    pal2 = c.create_polygon((540,540),(540,570),(390,560),(390,550),fill="blue")

    

        
    

###### Botones ventana inicial
nombre= StringVar()
et = Label(vnt,text="Nombre de Usuario",bg="blue").place(x=10,y=240)
bnt = Button(vnt,text="Guardar usuario",command=nueva,bg="red").place(x=320,y=240)
cam= Entry(vnt,textvariable=nombre,width=20).place(x=140,y=240)


'''    
    width=700
    height=600
    linea_distance = 100

#### Cuadricula
    def cuadricula(c, line_distance):
        for x in range(line_distance,width,line_distance):
            c.create_line(x, 0, x, height, fill="red")        
        for y in range(line_distance,height,line_distance):c.create_line(0, y, width, y, fill="red")
    cuadricula(c,100)
   '''
    

vnt.mainloop()



