import string
import random
import secrets

n = 10
characters = list(string.ascii_letters + string.digits + "@#!*-_"*random.randint(3,9))
print(characters)
random.shuffle(characters)


password = []
for i in range(n):
	password.append(secrets.choice(characters))

random.shuffle(password)
temp = "".join(password)

print(temp)