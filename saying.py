def readf(file):
	f = open(file)
	da = f.read()
	f.close()
	return da
def write_a(file, data):
	f = open(file, 'a+')
	f.write(data)
	f.close()
while True:
	words = readf('react.ns').strip().replace("\n", "").split(";")
	ll = True
	msg = input('Скажи: ').lower()
	for i in words:
		if ll:
			if i == msg:
				ll = False
				continue
			if words.count(msg) == 0:
				print('Что это?')
				write_rect = input("Какова моя реакция на это?: ")
				write_a('react.ns', ";\n"+msg+";"+write_rect)
				words = readf('react.ns').strip().replace("\n", "").split(";")
				print('Взял на заметку')
				ll = True
		else:
			print(i)
			ll = True
			continue