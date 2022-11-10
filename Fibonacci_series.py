def  fibonacci(n):
	if n == 1  or n == 0:
		return n;
	else:
		return fibonacci(n-2) + fibonacci(n - 1)

numero = int(input("Enter the number of term for fibonacci series: "))
if numero < 0:
	print("Number not valid")

else:
    i = 0

    print("Required fibonacci series: ")

    for i in range(0, numero):
            print(fibonacci(i))
