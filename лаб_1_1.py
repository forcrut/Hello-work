#nod
def nod(arg1, arg2) -> int:
	if arg1 == 0 and arg2 == 0:
		return("Infinity")
	elif arg1 == 0 and arg2 != 0:
		return(arg2)
	elif arg2 == 0:
		return(arg1)
	if type(arg1) != type(int()) or type(arg2) != type(int()): #проверка на входящие аргументы , чтобы они имели тип int, иначе ошибка
		raise ValueError("Value Error")                      #фактический вызов ошибки Value Error
	a1, b1, factor, s, myltiply = max(arg1, arg2), min(arg1, arg2), 2, [], 1
	if a1 % b1 == 0: #без этого if для простых чисел работало не очень хорошо, теперь же будет выдавать 1, если они взаимно просты
	 	return(b1)   #или же выдавать простое, если второе делится на него без остатка 
	while factor* factor < max(arg1, arg2):
		if a1 % factor + b1 % factor == 0: #одновременная проверка a1 и b1 на кратность factor
			myltiply *= factor
			a1 //= factor
			b1 //= factor
		else:
			factor += 1
	return(myltiply)

#nok
def nok(arg1, arg2) ->int:
	if type(arg1) != type(int()) or type(arg2) != type(int()) or arg1 == 0 or arg2 == 0: #проверка на входящие аргументы , 
		raise ValueError("Value Error")         #чтобы они имели тип int  не равны 0, иначе ошибка,фактический вызов ошибки Value Error
	myltiply, factor, a1, b1 = 1, 2, max(arg1, arg2), min(arg1, arg2)
	while a1 != 1 or b1 != 1:
		if a1 % factor == 0 or b1 % factor == 0: # если хотя бы одно из чисел делится на factor, то мы умножаем myltiply на него
			myltiply *= factor
			if a1 % factor == 0:# избавление от множителя factor
				a1 //= factor
			if b1 % factor == 0:# избавление от множителя factor
				b1 //= factor
		else:
			factor += 1 # начинаем поиск дальнейшего множителя myltiply
	return(myltiply)	



#nodGauss
def nodGauss(arg1, arg2) -> int: #нахождение НОД по методу Гаусса a1 = q* a2 + remains; a2 = q1* remains + remains1 ...
	if arg1 == 0 and arg2 == 0:
		return("Infinity")
	elif arg1 == 0 and arg2 != 0:
		return(arg2)
	elif arg2 == 0:
		return(arg1)
	if type(arg1) != type(int()) or type(arg2) != type(int()): #проверка на входящие аргументы , чтобы они имели тип int, иначе ошибка
		raise ValueError("Value Error")                      #фактический вызов ошибки Value Error
	a1, a2, remains = max(arg1, arg2), min(arg1, arg2), 1 
	while remains != 0:
		remains, a1=a1 % a2, a2
		a2 = remains
	return(a1)



if __name__ == '__main__':
	print(nok(10, 13))
	print(nod(1604, 56))
	print(nodGauss(22,11))
	print(nod(56, 0))
	print(nodGauss(22,0))
