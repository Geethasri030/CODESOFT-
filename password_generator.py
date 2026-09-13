import random
length_of_password=int(input("Enter how many characters should be add to your password:"))
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$_&!^%"
password=input("Enter your short password:")
for i in range(length_of_password):
	random_char=random.choice(characters)
	password=password+random_char
print(f"Your new strong password is :{password} ")