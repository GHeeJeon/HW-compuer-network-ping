from socket import *
from time import *

# Unit of RTT: ms

class TCPPing:

	def __init__(self, address, port, size=64, timeout=0.5):
		self.address = address
		self.port = port
		self.size = size
		self.timeout = timeout

	def startPingTest(self, delay, repeat):
		sent = 0
		recv = 0
		lost = 0
		rtts = []
		
		try:
			for i in range(repeat):
				rtt = self._sendPing()
				sent += 1

				if rtt is not None:
					recv += 1
					rtts.append(rtt)
					
					print("{size} bytes from {addr}: seq={seq}, rtt={rtt} ms"
							.format(size=self.size, addr=self.address, seq=i, rtt=rtt))
				else:
					lost += 1
					
					print("Request timeout for seq {seq}".format(seq=i))

				sleep(delay)

		except KeyboardInterrupt:
			print()

		# After everything done: print summary.
		self._printStatistics(sent=sent, received=recv, lost=lost, rtts=rtts)

	def _sendPing(self):
		"""

			Returns: (Number: RTT if succeeded, None otherwise)
		"""
		try:
			toSend = "o" * self.size
	
			# Create socket
			s = socket(AF_INET, SOCK_STREAM)

			s.settimeout(self.timeout)

			# Connect socket
			s.connect((self.address, self.port))

			startTime = time()

			# Send through socket
			s.sendall(toSend.encode())

			# Receive froms socket
			reply = s.recv(2048)

			endTime = time()

			# Close socket
			s.close()

			return (endTime - startTime) * 1000

		except timeout:
			return None

	def _printStatistics(self, sent, received, lost, rtts):
		# Blah!!
		print("--- {addr} ping statistics ---".format(addr=self.address))
		print("{sent} packets transmitted, {received} packets received, {lose}% packet loss".format(sent=sent, received=received, lose=lost/sent * 100))
		print("rount-trip average = {avg} ms".format(avg=sum(rtts)/len(rtts) if len(rtts) > 0 else 0))


# count sendMessage, 응답메시지수 에러율, RTT
#################################


ping = TCPPing(input("Server address: "), int(input("Port: ")), timeout=5)
#ping = TCPPing("172.20.10.2", 9999)
ping.startPingTest(delay=0, repeat=1000) 
