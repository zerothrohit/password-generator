import secrets
import string

alphabet = string.ascii_letters + string.digits

n = 10

while True:
	password = ''.join(secrets.choice(alphabet) for i in range(n))

	if (any(c.islower() for c in password) and any(c.isupper()
	for c in password) and sum(c.isdigit() for c in password) >= 3):
		print(password)
		break
