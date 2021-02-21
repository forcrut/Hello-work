print("Hello world, Python, work, mistakes!!!")# первая команда вывода текста "Hello world, Python, work, mistakes!!!"
for i in range(0,2):# цикл for
	print("Держаться, только держаться\t")
	for k in "Python":# цикл for , где i будет браться как каждая буква в слове Python
		print(k, end=" ")# end определяет,что будет находится полсе каждого k элемента
	print(" \n")# переход на новый абзац