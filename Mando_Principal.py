import socket
import threading
import tkinter as tk
host='127.0.0.1'
port=5555
my_socket=socket.socket()
my_socket.bind((host,port))
my_socket.listen()
print(f"Servidor escuchando en el puerto {port}")
usuarios_conectados=[]
ip_user_conectados=[]




def anotar_mensaje(conexion):
	while True:
		mensaje=conexion.recv(1024).decode('utf-8')
		posicion=usuarios_conectados.index(conexion)
		mensaje=mensaje.replace("'","")
		with open(f"Cliente_{posicion}.txt",'a+') as f:
			f.write(str(mensaje))
def menu():			
	class Ver_maquinas(tk.Tk):
		def __init__(self):
			super().__init__()

			self.iniciar_gui()
			self.botones()
			self.instrucciones_botones()

		def ver_menu(self):
			print(ip_user_conectados)	
		def iniciar_gui(self):	
			self.title("MÁQUINAS")
			self.config(background="RoyalBLue1")
			self.frame=tk.Frame(self,background="blue")
			self.frame.pack()
		def botones(self):	
			self.button1=tk.Button(self.frame,text="MOSTRAR CLIENTES")
			self.button1.grid(row=0,column=0)
		def instrucciones_botones(self):
			self.button1['command']=lambda:self.ver_menu()


	app=Ver_maquinas()
	app.mainloop()

thread_three=threading.Thread(target=menu,args=(),)	
thread_three.start()


while True:
	conexion,  ip=my_socket.accept()

	#print(f"SE CONECTO EL USUARIO CON IP {ip}")
	usuarios_conectados.append(conexion)
	ip_user_conectados.append(ip)	
	#print(usuarios_conectados)
	thread_one=threading.Thread(target=anotar_mensaje,args=(conexion,))
	thread_one.start()
	


