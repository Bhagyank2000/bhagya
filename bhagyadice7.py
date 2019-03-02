import random

d=0
p=0

while True:
	r = input("press r to roll, q to quit :")

	if r == 'r':
		d=random.randint(1,6)
		print("you got :" ,d)
	elif d==6:
	 	   print("congratulations,you can play now.")
	 	   break
	else:
	 		print("roll again,till you get 6.")

while true:
	r=("press r to roll, q to quit : ")

	if r == 'r' :
		d=random.randint(1,6)
		print("you got :" ,d)

		if p==p+d:
			p=100
			p=p-d
			print("wait till you get", 100,p,"or else.")

		print("your new position is :", p)

		if p==100:
			print("you won!")
			exit()
			if p==8:
				p=37
				print("wow,a ladder .go to " ,p)


			elif r== 'q':
				print("bye!")
				exit()