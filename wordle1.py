import random
 

words= ["route","crash","clown","shaky","power"]

wordnum = random.randint(0,5)
word = words[wordnum] 
letter = []
for char in word:
	letter.append(char)
print (letter)

print("guess a 5 letter word")

pos=0
while pos < 8:
	user_g=input()
	guess=[]
	for char in user_g:
		guess.append(char)

	g1= guess[0]
	g2= guess[1]
	g3= guess[2]
	g4= guess[3]
	g5= guess[4]
	
	
	t1=0
	t2=0
	t3=0
	t4=0
	t5=0
	
	
	if g1 == letter[0]:
		print ("correct letter ")
		t1=1
	for x in letter:
		if g1 == x and t1 == 0:
			print("letter is in incorrect place")
			t1=2
	if t1 == 0:
		print("incorrct letter")
	
	
	if g2 == letter[1]:
		print ("correct letter ")
		t2=1
	for x in letter:
		if g2 == x and t2 == 0:
			print("letter is in incorrect place")
			t2=2
	if t2 == 0:
		print("incorrct letter")
	
	
	if g3 == letter[2]:
		print ("correct letter ")
		t3=1
	for x in letter:
		if g3 == x and t3 == 0:
			print("letter is in incorrect place")
			t3=2
	if t3 == 0:
		print("incorrct letter")
	
	
	if g4 == letter[3]:
		print ("correct letter ")
		t4=1
	for x in letter:
		if g4 == x and t4 == 0:
			print("letter is in incorrect place")
			t4=2
	if t4 == 0:
		print("incorrct letter")
	
	
	if g5 == letter[4]:
		print ("correct letter ")
		t5=1
	for x in letter:
		if g5 == x and t5 == 0:
			print("letter is in incorrect place")
			t5=2
	if t5 == 0:
		print("incorrct letter")

	if t1 ==1 and t2==1 and t3==1 and t4==1 and t5==1:
		pos =8
		print("word correctly guessed")
	elif pos == 7:
		print("unlucky, end of game")
	else:
		print("try agian")
		
	pos = pos +1

