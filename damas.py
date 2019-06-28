from Tkinter import *
principal = Tk() 
#casillas negras 32
#  12 fichas negras
#  12 fichas blancas 
#otros elementos 

#nota - esta pendiente restringir las comprobaciones a las dimensiones del tablero 
tablero = Canvas(principal,width=1200, height=800, bg= 'gray87')
tablero.pack(expand=YES, fill=BOTH)

def promover_a_reina(ficha):
    #coordenadas para evaluar extremos del talero
    coordenadas=tablero.coords(ficha)
    y2=coordenadas[2]
    y1=coordenadas[0]

    etiquetas=tablero.gettags(ficha)
    
    color=etiquetas[0]

    jerarquia=etiquetas[1]
    #evaluar extremos
    if color=='negra' and y2 > 700:
        tablero.itemconfig(ficha,fill="green")
        print ("promocion realizada!!")

    if color=='blanca' and y1 < 100:
        tablero.itemconfig(ficha,fill="green") 
        print ("promocion realizada!!")       

def comer_ficha(event):
    global puntaje_negras,puntaje_blancas
    #recoge el valor de la ficha sobre la que clickea el usuario
    seleccionada=event.widget.find_closest(event.x,event.y)[0]
    
    #obtener el color de la ficha
    etiquetas=tablero.gettags(seleccionada)
    color=etiquetas[0]
    

    #verifica si la ficha esta marcada de rojo
    marcado=tablero.itemcget(seleccionada, 'fill')
    
    print marcado

    if(marcado=='red'):

        if color == 'blanca' :
            puntaje_negras+=1
            tablero.itemconfig(57 , text='Jugador fichas negras: '+str(puntaje_negras))
            tablero.delete(seleccionada)

        if color == 'negra' :
            puntaje_blancas+=1
            tablero.itemconfig(58 , text='Jugador fichas blancas: '+str(puntaje_blancas))
            tablero.delete(seleccionada)

def crear_tablero():
#creacion de 32 casillas dentro del tablero    
    for x in range(32):
        tablero.create_rectangle(0,0,100,100, fill='gray32')
            
#mover casillas 
    for a in range(4):
        tablero.move(a+1,(a)*200,0)
    for b in range(4):
        tablero.move(b+5,(b+(b+1))*100,100)
    for a in range(4):        
        tablero.move(a+9,(a)*200,200)
    for b in range(4):
        tablero.move(b+13,(b+(b+1))*100,300)
    for a in range(4):        
        tablero.move(a+17,(a)*200,400)
    for b in range(4):
        tablero.move(b+21,(b+(b+1))*100,500)
    for a in range(4):        
        tablero.move(a+25,(a)*200,600)
    for b in range(4):
        tablero.move(b+29,(b+(b+1))*100,700)

def crear_marcador(numNeg, numBlnc):
	score_negro = tablero.create_text(850,50,text='Jugador fichas negras: '+str(puntaje_negras), fill='black', anchor = W, font=("Helvetica", "20"))
	score_blanco = tablero.create_text(850,750,text='Jugador fichas blancas: '+str(puntaje_blancas),fill='black', anchor = W, font=("Helvetica", "20"))
	text_turno = tablero.create_text(850,400, text='El turno es de: ',fill='black', anchor = W, font=("Helvetica", "25"))
	linea_aux = tablero.create_line(800,0,800,800)
	ficha_aux = tablero.create_oval(1100-35,350,1200-35,450)	  

def crear_fichas():
    #creacion   fichas negras
    for ficha in range(12):
        p_negra = tablero.create_oval(0,0,100,100, fill='black',tags=('negra','peon'))

 
        #colocar item en el tope de la pila de superposicion visual
        tablero.tag_raise(p_negra)

        #evento click izquierdo seleccionar ficha  
        tablero.tag_bind(p_negra, '<Button-1>', seleccionar_ficha)
        #evento click derecho comer ficha
        tablero.tag_bind(p_negra, '<Button-2>', comer_ficha)
    
    # creacion y posicionamiento fichas blancas

    for ficha in range(12):
        p_blanca = tablero.create_oval(0,0,100,100, fill='white',tags=('blanca','peon'))
  

        #colocar item en el tope de la pila de superposicion visual
        tablero.tag_raise(p_blanca)

        #evento click izquierdo del mouse  
        tablero.tag_bind(p_blanca, '<Button-1>', seleccionar_ficha)

        #evento click derecho comer ficha
        tablero.tag_bind(p_blanca, '<Button-2>', comer_ficha)

    #ordenamiento automatico 
    posicion_inicial_negras()
    posicion_inicial_blancas()

def posicion_inicial_negras():
    for a in range(4):
        tablero.move(a+33,(a)*200,0)
    for b in range(4):
        tablero.move(b+37,(b+(b+1))*100,100)
    for a in range(4):
        tablero.move(a+41,(a)*200,200)

def posicion_inicial_blancas():
    for b in range(4):
        tablero.move(b+45,(b+(b+1))*100,500)
    for a in range(4):
        tablero.move(a+49,(a)*200,600)
    for b in range(4):
        tablero.move(b+53,(b+(b+1))*100,700)

def esta_en_casilla(x,y):
    for ficha in range(1,33):
        coords=tablero.coords(ficha)

        horizontal=x>=coords[0] and x<= coords[2]
        vertical=y>=coords[1] and y <= coords[3] 
        if(horizontal and vertical):
            return True
    return False    

#evalua si el punto pasado como parametro pertenece a una de las fichas

def esta_en_ficha(x,y):
    for ficha in range(32,57):
        coords=tablero.coords(ficha)

        horizontal=x>=coords[0] and x<= coords[2]
        vertical=y>=coords[1] and y <= coords[3]

        if(horizontal and vertical):
            return True
    return False

#prototipos de la evoolucion del metodo esta en ficha

def esta_en_ficha_negra(x,y):
    for ficha in range(32,45):
        coords=tablero.coords(ficha)

        horizontal=x>=coords[0] and x<= coords[2]
        vertical=y>=coords[1] and y <= coords[3]

        if(horizontal and vertical):
            return True
    return False

def esta_en_ficha_blanca(x,y):
    for ficha in range(45,57):
        coords=tablero.coords(ficha)

        horizontal=x>=coords[0] and x<= coords[2]
        vertical=y>=coords[1] and y <= coords[3]

        if(horizontal and vertical):
            return True
    return False

def repintar():
    global mi_ficha

    #negras
    for ficha in range(33,45):
        #excluye a la ficha que esta siendo manipulada, esta sera de color azul
        if ficha!=mi_ficha :
            tablero.itemconfig(ficha,fill="black")
    #blancas
    for ficha in range(45,57):
        if ficha!=mi_ficha :
            tablero.itemconfig(ficha,fill="white")
    #gris
    for casilla in range(1,32):
        tablero.itemconfig(casilla,fill="gray32")



def buscar_vacio(casilla,incremento):

    coordsFicha=tablero.coords(casilla)
    #coordenadas del punto referencial
    x=coordsFicha[0]+incremento[0]
    y=coordsFicha[1]+incremento[1]
    
    #verifica el punto referencial
    hay_casilla_vacia=not esta_en_ficha(x,y)

    if esta_en_casilla(x,y) and hay_casilla_vacia:
        return True

    return False
def es_oponente(elemento,target):
    #atributos de elemento
    etiquetas=tablero.gettags(elemento)
    color=etiquetas[0]

    #atributos de target
    etiquetas_target=tablero.gettags(target)
    
    color_target=etiquetas_target[0]
    
    if color!=color_target:
        return True

    return False

#colorea elementos 
def resaltar_ficha(elemento,incremento):
    coordsFicha=tablero.coords(elemento)

    x=coordsFicha[0]+incremento[0]
    y=coordsFicha[1]+incremento[1]
    
    if esta_en_ficha(x,y):
        target=tablero.find_closest(x,y)
        if es_oponente(elemento,target):
            tablero.itemconfig(target, fill="red")



#busca fichas adyacentes a la ficha enviada como parametro utilizando un punto referencial 
def buscar_ficha(mi_ficha,incremento):

    coordsFicha=tablero.coords(mi_ficha)
    #coordenadas del punto referencial
    x=coordsFicha[0]+incremento[0]
    y=coordsFicha[1]+incremento[1]
    
    #verifica si el punto referencial pertenece a una ficha 
    if esta_en_ficha(x,y):
        return True
    return False

def interacciones_cercanas(mi_ficha):
#incrementos dependiendo de la diagonal que se quiera evaluar
    superiorIzquierda=(-50,-50)
    superiorDerecha= (150,-50)
    inferiorIzquierda= (-50,+150)
    inferiorDerecha= (150,150)
 
    vacioSuperiorIzquierda=(-150,-150)
    vacioSuperiorDerecha= (250,-150)
    vacioInferiorIzquierda= (-150,+250)
    vacioInferiorDerecha= (250,250)
    
    
    #extraer atributos de la ficha para el analisis
    etiquetas=tablero.gettags(mi_ficha)

    jerarquia=etiquetas[1]
    
    color=etiquetas[0] 
    
    print str(etiquetas)

    #fichas negras solo pueden comer blancas y viceversa
    if color=='blanca':
    
        if buscar_ficha(mi_ficha,superiorIzquierda) and  buscar_vacio(mi_ficha,vacioSuperiorIzquierda):
            resaltar_ficha(mi_ficha,superiorIzquierda)        
            
        if buscar_ficha(mi_ficha,superiorDerecha) and  buscar_vacio(mi_ficha,vacioSuperiorDerecha):
            resaltar_ficha(mi_ficha,superiorDerecha)
    if color=='negra':        
        if buscar_ficha(mi_ficha,inferiorIzquierda) and  buscar_vacio(mi_ficha,vacioInferiorIzquierda):
            resaltar_ficha(mi_ficha,inferiorIzquierda)
            
        if buscar_ficha(mi_ficha,inferiorDerecha) and   buscar_vacio(mi_ficha,vacioInferiorDerecha):
            resaltar_ficha(mi_ficha,inferiorDerecha)
        
    
    
def seleccionar_ficha(event):

    #recoge el valor de la ficha sobre la que clickea el usuario
    seleccionada=event.widget.find_closest(event.x,event.y)[0]
    
    #obtener el color de la ficha
    etiquetas=tablero.gettags(seleccionada)
    color=etiquetas[0]
    jerarquia=etiquetas[1]

    #acciones de seleccion

    #accede a la variable global mi ficha
    global mi_ficha

    #reasignamos el valor de mi_ficha
    mi_ficha=seleccionada
    
	#acciones de soporte

    #limpiamos detecciones anteriores
    repintar()
    #buscamos posibles jugadas para la ficha
    interacciones_cercanas(mi_ficha)
    
    print " \n seleccionada: " + str(seleccionada) + " " + color + " " + jerarquia


    tablero.itemconfig(seleccionada,fill="blue") 

def moverFicha(event):
    repintar()
    
    if event.keysym == 'Up':
        tablero.move(mi_ficha, 0, -100)
        interacciones_cercanas(mi_ficha)

        promover_a_reina(mi_ficha)
    
    elif event.keysym == 'Down':
        tablero.move(mi_ficha, 0, 100)
        interacciones_cercanas(mi_ficha)

        promover_a_reina(mi_ficha)

    elif event.keysym == 'Left':
        tablero.move(mi_ficha, -100, 0)
        interacciones_cercanas(mi_ficha)
    
    elif event.keysym == 'Right':
        tablero.move(mi_ficha, 100, 0)
        interacciones_cercanas(mi_ficha)
   
#llamado a funciones
mi_ficha=56

puntaje_blancas=0
puntaje_negras=0
#asignacion de keybindings

tablero.bind_all('<KeyPress-Up>' , moverFicha)
tablero.bind_all('<KeyPress-Down>' , moverFicha)
tablero.bind_all('<KeyPress-Left>' , moverFicha)
tablero.bind_all('<KeyPress-Right>' , moverFicha)

#orden de llamado a funciones es importante no modificar
#1
crear_tablero()
#2
crear_fichas()
#3
crear_marcador(puntaje_negras, puntaje_blancas)

principal.mainloop()	





















