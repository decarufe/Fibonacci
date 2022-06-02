import sys
import time
import cProfile

def fibonacci_slow(n):
	a = 1
	b = 1
	for i in range(n-1):
		total = a + b
		b = a
		a = total
	return b

def fibonacci_fast(n):
    a1 = 1
    a2 = 1
    a3 = 1
    t = 0

    for i in range(n-1):
        match t:
            case 0:
                a3 = a1 + a2
                t = 1
            case 1:
                a1 = a2 + a3
                t = 2
            case 2:
                a2 = a1 + a3
                t = 0
    match t:
        case 0:
            return a3
        case 1:
            return a1
        case 2:
            return a2

start1 = time.time()
cProfile.run('fib = fibonacci_slow(1000000)')
start2 = time.time()
cProfile.run('fib = fibonacci_fast(1000000)')
stop = time.time()

#print(fib)
#print(len(str(fib)))

print(f"Slow {start2 - start1}")
print(f"Fast {stop - start2}")

