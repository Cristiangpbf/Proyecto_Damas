from tkinter import *

tk = Tk() 

canvas = Canvas(tk,width=1200, height=800, bg= 'gray87')
canvas.pack(expand=YES, fill=BOTH)

def crear_tablero():    
    for x in range(32):
        canvas.create_rectangle(0,0,100,100, fill='gray32')        
    for a in range(4):
        canvas.move(a+1,(a)*200,0)
    for b in range(4):
        canvas.move(b+5,(b+(b+1))*100,100)
    for a in range(4):        
        canvas.move(a+9,(a)*200,200)
    for b in range(4):
        canvas.move(b+13,(b+(b+1))*100,300)
    for a in range(4):        
        canvas.move(a+17,(a)*200,400)
    for b in range(4):
        canvas.move(b+21,(b+(b+1))*100,500)
    for a in range(4):        
        canvas.move(a+25,(a)*200,600)
    for b in range(4):
        canvas.move(b+29,(b+(b+1))*100,700)

def crear_fichas():
	#posicionamiento fichas negras
	for x in range(12):
		p_negra = canvas.create_oval(0,0,100,100, fill='black')
	for a in range(4):
		canvas.move(a+33,(a)*200,0)
	for b in range(4):
		canvas.move(b+37,(b+(b+1))*100,100)
	for a in range(4):
		canvas.move(a+41,(a)*200,200)

	#posicionamiento fichas negras
	for x in range(12):
		p_blanca = canvas.create_oval(0,0,100,100, fill='white')
	for b in range(4):
		canvas.move(b+45,(b+(b+1))*100,500)
	for a in range(4):
		canvas.move(a+49,(a)*200,600)
	for b in range(4):
		canvas.move(b+53,(b+(b+1))*100,700)

#################
puntNeg = 0
puntBlnc = 0
#################
	
def status(numNeg, numBlnc):
	score_negro = canvas.create_text(850,50,text='Jugador fichas negras: '+str(numNeg), fill='black', anchor = W, font=("Helvetica", "20"))
	score_blanco = canvas.create_text(850,750,text='Jugador fichas blancas: '+str(numBlnc),fill='black', anchor = W, font=("Helvetica", "20"))
	text_turno = canvas.create_text(850,400, text='El turno es de: ',fill='black', anchor = W, font=("Helvetica", "25"))
	linea_aux = canvas.create_line(800,0,800,800)
	ficha_aux = canvas.create_oval(1100-35,350,1200-35,450)	


num_ficha=56

def moverFicha(event):

    if event.keysym == 'Up':
        canvas.move(num_ficha, 0, -100)
        print(canvas.coords(num_ficha))

    elif event.keysym == 'Down':
        canvas.move(num_ficha, 0, 100)
        print(canvas.coords(num_ficha))
    elif event.keysym == 'Left':
        canvas.move(num_ficha, -100, 0)
        print(canvas.coords(num_ficha))
    else:
        canvas.move(num_ficha, 100, 0)
        print(canvas.coords(num_ficha))



canvas.bind_all('<KeyPress-Up>', moverFicha)
canvas.bind_all('<KeyPress-Down>', moverFicha)
canvas.bind_all('<KeyPress-Left>', moverFicha)
canvas.bind_all('<KeyPress-Right>', moverFicha)

crear_tablero()
crear_fichas()
status(puntNeg,puntBlnc)
print(canvas.find_all())



tk.mainloop()