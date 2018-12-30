import numba
import re
import socket
from time import time
from threading import Thread
import startGame

@jit
def connectGame():
    listSock = list()
    sock = socket.socket()
    sock.bind(('localhost', 1010))
    sock.listen(4)
    listSock.append(sock.accept())
    listSock.append(sock.accept())
    listSock.append(sock.accept())
    listSock.append(sock.accept())

@jit
def myGet():
    sock = socket.socket()
    sock.connect(('localhost', 8888))
    data = sock.recv(2048)
    a = data.decode("utf-8")
    sock.close()
    return map(int, a.split("/"))

@jit
def mySend(maxInt, maxMap):
    sock = socket.socket()
    sock.connect(('localhost', 8989))
    a = str(maxInt) + "/" + str(maxMap)
    sock.send(a.encode("utf-8"))
    sock.close()

@jit
def combGen(x, z):
    global resultMap
    global resultInt
    maxMap = list()
    maxInt = 0
    counter = 0
    time1 = time()
    while x < z:
        binComb = bin(x)[3:]
        if summ(binComb) > len(binComb) * 0.6:
            totalLife = startGame.start(k, n, str(binComb))
            if totalLife > maxInt:
                maxInt = totalLife
                maxMap.clear()
                maxMap.append(re.findall('.' * n + '?', binComb))
            elif totalLife == maxInt:
                maxMap.append(re.findall('.' * n + '?', binComb))
        x += 1
    print(time()-time1)
    resultMap.append(maxMap)
    resultInt.append(maxInt)

@jit
def summ(x):
    summa = 0
    for i in x:
        summa += int(i)
    return summa


n, k, xi, zi = myGet()
resultMap = []
resultInt = []

combGen(xi, zi)
# if __name__ == "__main__":
# 	t1 = Thread(target=combGen, args=(xi, zi))
# 	t2 = Thread(target=combGen, args=(xi+4, zi))
# 	t3 = Thread(target=combGen, args=(xi+8, zi))
# 	t4 = Thread(target=combGen, args=(xi+12, zi))
#
# 	t1.start()
# 	t2.start()
# 	t3.start()
# 	t4.start()
#
# 	t1.join()
# 	t2.join()
# 	t3.join()
# 	t4.join()


print(*resultMap[resultInt.index(max(resultInt))], max(resultInt))
