def bad_fib(n):
	while n >= 0:
		if n == 0:
			print('Base case 0')
			return 0
		if n == 1:
			print('Base case 1')
			return 1
		x = bad_fib(n-1)
		y = bad_fib(n-2)
		print ('n={}, x={}, y={}, x+y={}\n'.format(n,x,y, x+y))
		return x+y
