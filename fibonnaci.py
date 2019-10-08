def fibonacci(n):
	a = 1
	b = 1
	for i in range(n-1):
		total = a + b
		b = a
		a = total
	return b

fib = fibonacci(1000)
print(fib)
print(len(str(fib)))
