import socket


def mySend(a, b, c, d, sock):
	conn, addr = sock.accept()
	a = str(a) + "/" + str(b) + "/" + str(c) + "/" + str(d)
	print('Connected:', addr)
	conn.send(a.encode("utf-8"))
	conn.close()


def myGet(sock):
	conn, addr = sock.accept()
	data = sock.recv(2048)
	a = data.decode("utf-8")
	sock.close()
	return map(a.split("/"))


def binFirst(n):
	x = "0b" + "1" + "0" * (n ** 2)
	z = "0b" + "1" + "0" * (n ** 2 + 1)
	x1 = int(x, 2)
	# x2 = int(x, 2) + 1
	# x3 = int(x, 2) + 2
	# x4 = int(x, 2) + 3
	z = int(z, 2)
	return x1, z # x2, x3, x4, z

n = int(input("input n: "))
k = int(input("input k: "))
xi1, zi = binFirst(n)

sock = socket.socket()
sock.bind(('localhost', 8888))
sock.listen(4)

# sockGet = socket.socket()
# sockGet.bind(('localhost', 8989))
# sockGet.listen(4)

mySend(n, k, xi1, zi, sock)
# mySend(n, k, xi2, zi, sock)
# mySend(n, k, xi3, zi, sock)
# mySend(n, k, xi4, zi, sock))
# try:
# 	print(myGet(sockGet))
# except:
# 	print("NotWorkNow")
# --P-R-O-G-R-A-M-
