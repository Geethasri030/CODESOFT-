while True:
	first_num=int(input("Enter the first number:"))
	second_num=int(input("Enter thr second number:"))
	print("Choose an operation from below:")
	print("1.Addition")
	print("2.Subtraction")
	print("3.Multiplication")
	print("4.Division")
	print("5.Exit")
	choice=int(input("Enter your choice :"))
	if choice ==1:
		result=first_num+second_num
		print(f"The result of {first_num}+{second_num} is :{result}")
	elif choice ==2:
		result=first_num-second_num
		print(f"The result of {first_num}-{second_num} is:{result}")
	elif choice ==3:
		result=first_num*second_num
		print(f"The result of {first_num}*{second_num} is:{result}")
	elif choice ==4:
		result=first_num/second_num
		print(f"The result of {first_num}/{second_num} is :{result}")
	elif choice ==5:
		break
	else:
		print("Invalid choice.Please select valid choice.")
