#nod
def nod(arg1, arg2) -> int:
	if not(isinstance(arg1, int) and isinstance(arg2, int)): #проверка на входящие аргументы , чтобы они имели тип int, иначе ошибка
		raise ValueError("Value Error")
	a1 = max(arg1, arg2)
	b1 = min(arg1, arg2)
	if a1 % b1 == 0: #без этого if для простых чисел работало не очень хорошо, теперь же будет выдавать 1, если они взаимно просты
		return(b1)   #или же выдавать простое, если второе делится на него без остатка
	factor = 2
	s = []
	myltiply = 1
	while factor* factor < max(arg1, arg2):
		if a1 % factor + b1 % factor == 0: #одновременная проверка a1 и b1 на кратность factor
			s += [factor]
			a1 /= factor
			b1 /= factor
		else:
			factor += 1
	for i in s:
		myltiply *= i
	return(myltiply)

#nok
def nok(arg1, arg2) ->int:
	if not(isinstance(arg1, int) and isinstance(arg2, int)): #проверка на входящие аргументы , чтобы они имели тип int, иначе ошибка
		raise ValueError("Value Error")
	a1 = max(arg1, arg2)
	factor = 1
	while factor* factor < max(arg1, arg2): #пробежка по всем множителям максимального из двух чисел
		if (a1* factor) % min(arg1, arg2)== 0: #таким образом, если if примет True, то мы нашли нок,
			return(a1*factor)               #иначе выйдет из цикла while и вернет произведение чисел
		else:
			factor += 1
	return(arg1* arg2) #если же в while return не сработало, то мы выведем произведение чисел, так как они видимо взаимнопросты,
                       #или не имеют общих множителей

if __name__ == '__main__':
	print(nok(70, 24))
	print(nod(70, 24))
