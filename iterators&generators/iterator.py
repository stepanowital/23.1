# with open('./apache_logs_big.txt') as f:
# 	file_content = f.read()
# 	lines = file_content.split('\n')
# 	print(lines[:10])


# with open('./apache_logs_big.txt') as f:
# 	counter = 0
# 	while True:
# 		try:
# 			line = next(f)
# 		except StopIteration:
# 			break
# 		print(line)
# 		counter += 1
# 		if counter > 10:
# 			break



# L = [1, 2, 3, 4, 5, 6]
# it = iter(L)
#
# print(it)
# print(next(it))
#
# print(list(it))
# print(list(it))



# Стандартные итераторы (список, кортеж, словарь)

# a = [1, 2, 3, 4, 5, 6]
# print(type(a))
# print(type(iter(a)))
# for item in a:
# 	print(item)

# b = (1, 2, 3, 4, 5, 6)
# print(type(b))
# print(type(iter(b)))
# for item in b:
# 	print(item)

# c = {'key1': 'value1', 'key2': 'value2'}
# print(type(c))
# print(type(iter(c.keys())))
# print(type(iter(c.values())))
# print(type(iter(c.items())))
# for key, value in c.items():
# 	print(key, value)


# class MyIter:
# 	def __init__(self, n):
# 		self.n = n
# 		self.current = 0
#
# 	def __iter__(self):
# 		print('__iter__')
# 		return self
#
# 	def __next__(self):
# 		print('__next__')
# 		if self.n > self.current:
# 			buf = self.current
# 			self.current += 1
# 			return buf
# 		else:
# 			raise StopIteration
#
# 	def next(self):
# 		print("Who am I???")
# 		self.__next__()


# it = MyIter(4)
# print('begin')
# print()
#
# # iter(it)
# # print()
#
# print(it)
# print()
#
# list(it)

# it.next()
# it.next()
# print()


# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print()


