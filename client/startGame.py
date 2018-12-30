@jit
def start(k, n, map):
	return startGame(k, n, translate(map))

@jit
def translate(map):
	newMap = list()
	for i in map:
		newMap.append(bool(int(i)))
	return newMap

@jit
def startGame(k, n, map):
	nowMap = copyInMap(k, n, map)
	for i in range(k):
		lifeInStep = 0
		newMap = genClearMap(k, n)
		for x in range(1, len(nowMap) - 1):
			for y in range(1, len(nowMap) - 1):
				lifeInStep += int(nowMap[x][y])
				neighbors = int(nowMap[x - 1][y + 1]) + int(nowMap[x][y + 1]) + int(nowMap[x + 1][y + 1]) + \
				            int(nowMap[x - 1][y]) +                             int(nowMap[x + 1][y]) + \
				            int(nowMap[x - 1][y - 1]) + int(nowMap[x][y - 1]) + int(nowMap[x + 1][y - 1])
				if bool(nowMap[x][y]):
					if neighbors == 2 or neighbors == 3:
						newMap[x][y] = True
				else:
					if neighbors == 3:
						newMap[x][y] = True
		if lifeInStep == 0:
			break
		nowMap = newMap[:]
	return countingLiving(nowMap)

@jit
def copyInMap(k, n, map):
	startPosition = int((k * 2 + n + 2) / 2 - (n / 2))
	newMap = genClearMap(k, n)
	for x in range(n):
		for y in range(n):
			newMap[x + startPosition][y + startPosition] = map[x * n + y]
	return newMap

@jit
def genClearMap(k, n):
	f = list()
	k = int(k)
	n = int(n)
	for x in range(k * 2 + n + 2):
		f.append(list())
	for x in range(len(f)):
		for y in range(len(f)):
			f[x].append(False)
	return (f)

@jit
def countingLiving(map):
	c = 0
	for x in range(len(map)):
		c += map[x].count(True)
	return c

