from socket import *


class UDPEchoServer:

	def __init__(self, port):
		serverSocket = socket(AF_INET, SOCK_DGRAM)
		serverSocket.bind(('', port))

		self.socket = serverSocket
		self.port = port
	def start(self):
		self._listen()

	def _listen(self):
		print("Start listening from port {p}".format(p=self.port))
		
		while True:
			message, clientAddress = self.socket.recvfrom(2048)
			print("received from {addr}: {msg}"
					.format(addr=clientAddress[0], msg=message.decode()))

			self.socket.sendto(message, clientAddress)

	

server = UDPEchoServer(12000)
server.start()
