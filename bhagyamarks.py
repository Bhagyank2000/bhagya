print("enter "e" for exit")
print("enter marks obtained in 5 subjects: ")
mark1 = input()

if mark1 == "e":
	exit()
else:
	mark1 = int (input())
	mark2 = int (input())
	mark3 = int (input())
	mark4 = int (input())
	sum = mark1 + mark2 + mark3 + mark4 +mark5
	percentage = (sum/500)*100
	if (percentage>=91 and percentage<=100):
	 print("your grade is A+")

elif (percentage>=81 and percentage<=90):
	 print ("your grade is A")
	elif (percentage>=71 and percentage<=80):
	 print("your grade is B+")
	elif (percentage>=61 and percentage<=70):
	 print("your grade is B")
	elif ("percentage>=51 and percentage<=60"):
	 print("your grade is C+")
	elif(percentage>=41 and percentage<=50):
	 print("your grade is C")
	elif (percentage>=0 and percentage<=40):
print("your grade is F")
	else:
print("insufficient data!!")