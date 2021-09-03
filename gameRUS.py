  print("Игра кости на питоне лол")
	print("Версия фиг знает какая")

	import random

	input("Нажми ENTER для начала игры")

	gamer1 = random.randint(1,6)
	print("Твое число: ")
	print(gamer1)

	input("Нажми ENTER для продолжения игры")

	gamer2 = random.randint(1,6)
	print("Число ПК: ")
	print(gamer2)

	if gamer1 > gamer2:
		print("Ты выйграл лол")
	elif gamer2 == gamer2:
		print("Лошара, ничья")
	else:
		print("Ты проиграл, зай))))")

	game = input("Хочешь просрать игру? Нажми y для продолжения, и n чтобы свалить отсюда нафиг")

	if game == "n":
		print("Ну и иди ты")
		break
	elif game == "y":
		print("Удачного проигрыша)0))")
	else:
		print("Чел, ты норм?")
		input()
