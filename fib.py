import math

size = 50
nrCells = 10
PHI = 0.61803399


def fib(n):
    if n == 1 or n == 2:
        return 1
    #elif n == 1:
    #    return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)
        
def fib_seq(n):
    #seq = []
    return [fib(i+1) for i in range(n)]

def fib_pos(n):
    r = math.sqrt(n)
    theta = n * PHI
    ekis = r * math.cos(2*math.pi * theta)
    ygriega = r * math.sin(2*math.pi * theta)
    #print 'r: ' + str(r) + ' theta: ' + str(theta) + ' x: ' + str(ekis) + ' y: ' + str(ygriega)
    return (ekis, ygriega)

def fib_spiral(n, m):
    spiral = []
    for i in range(1,m+1):
        spiral.append(fib_pos(n*i))
    return spiral
    
def fib2(n): # return Fibonacci series up to n
	result = []
	a, b = 0, 1
	while b < n:
		result.append(b)
		a, b = b, a+b
	return result

if __name__ == '__main__':
    #for i in range(10):
    #   print fib(i)
#    fibsq = fib_seq(nrCells)
    #print fib_seq(nrCells)
    #print fib2(nrCells)
    print fib_spiral(8, 10)
