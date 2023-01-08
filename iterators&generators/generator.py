# def simple_gen():
# 	print('before first yield')
# 	yield
# 	print('after first yield')
# 	yield 'value from yield'
# 	print('after second yield')
#
#
# gen = simple_gen()
# print(gen)
# print()
#
# print(next(gen))
# print()
#
# print(next(gen))
# print()
#
#
# def numm():
# 	yield 1
# 	yield 2
# 	yield 3
#
#
# numm = numm()
#
# print(list(numm))


def MyGen(n):
	print('Start MyGen')
	current = 0
	while current < n:
		print('before yield, current is: ', current)
		yield current
		print('after yield, current is: ', current)
		current += 1


gen = MyGen(5)

print(next(gen))
print()

print(next(gen))
print()

print(next(gen))
print()

for item in gen:
	print(item)
