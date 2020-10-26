from socket import *


class TCPEchoServer:

	def __init__(self, port):
		serverSocket = socket(AF_INET, SOCK_STREAM)
		serverSocket.bind(('', port))
		serverSocket.listen()

		self.socket = serverSocket
		self.port = port

	def start(self):
		self._listen()

	def _listen(self):
		print("Start listening from port {p}".format(p=self.port))
		
		while True:
			clientSocket, clientAddress = self.socket.accept()

			message = clientSocket.recv(2048)

			print("received from {addr}: {msg}"
					.format(addr=clientAddress[0], msg=message.decode()))

			clientSocket.sendall(message)
			clientSocket.close()

server = TCPEchoServer(9999)
server.start()
