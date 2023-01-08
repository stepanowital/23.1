arr = [1, 2, 3, 4, 5]


# arr1 = [item + 1 for item in arr]
#
# print(arr1)


		# СПИСКИ
def foo(item):
	return item ** 2


#
#
# list_obj = [foo(item) for item in arr]
# print(list_obj)
# print(type(list_obj))


		# СЛОВАРИ
# dict_obj = {item: foo(item) for item in arr}
# print(dict_obj)
# print(type(dict_obj))


		# ГЕНЕРАТОРЫ
# iter_obj = (foo(item) for item in arr)
# print(iter_obj)
# print(list(iter_obj))
# print(list(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))


		# Чему эквивалентны LIST COMPREHENSIONS

# СПИСКИ
# arr1 = [item + 1 for item in arr]
# print(arr1)

# arr1 = []
# for item in arr:
# 	arr1.append(item + 1)
# print(arr1)

# СЛОВАРИ
# dict_obj = {item: foo(item) for item in arr}

# dict_obj = {}
# for item in arr:
# 	dict_obj[item] = foo(item)
# print(dict_obj)

# ГЕНЕРАТОРЫ
# iter_obj = (foo(item) for item in arr)

# def sequence_gen(arr):
# 	for item in arr:
# 		yield foo(item)
# iter_obj = sequence_gen(arr)
# print(iter_obj)
# print(list(iter_obj))
# print(list(iter_obj))


		# ДОБАВЛЯЕМ УСЛОВИЯ
# СПИСКИ
# arr1 = [item + 1 for item in arr if item % 2 == 0]
# print(arr1)
#
# arr1 = []
# for item in arr:
# 	if item % 2 == 0:
# 		arr1.append(item + 1)
# print(arr1)


# СЛОВАРИ
# dict_obj = {item: foo(item) for item in arr if item % 2 != 0}
# print(dict_obj)
#
# dict_obj = {}
# for item in arr:
# 	if item % 2 != 0:
# 		dict_obj[item] = foo(item)
# print(dict_obj)


		# Пример для преобразования в LIST COMPREHENSIONS
class User:
	def __init__(self, id, name):
		self.id = id
		self.name = name

	def __str__(self):
		return f'User #{self.id}'

	def __repr__(self):
		return self.__str__()


class Blog:
	def __init__(self, id, subscriber_ids):
		self.id = id
		self.subscriber_ids = subscriber_ids


users = [User(1, 'Vitaliy'), User(2, 'Sergei')]
blogs = [Blog(1, [1, 2]), Blog(2, [2, 3, 4])]

res = {'<blog_id>': ['user']}


def attach_users(blogs, users):
	users_dict = {}
	for u in users:
		users_dict[u.id] = u

	blogs_dict = {}
	for b in blogs:
		blog_users = []
		for subscriber_id in b.subscriber_ids:
			if subscriber_id in users_dict:
				blog_users.append(users_dict[subscriber_id])
		blogs_dict[b.id] = blog_users

	return blogs_dict


print(attach_users(blogs, users))


def attach_users2(blogs, users):
	users_dict = {u.id: u for u in users}

	blogs_dict = {}
	for b in blogs:
		blog_users = [users_dict[subscriber_id] for subscriber_id in b.subscriber_ids if subscriber_id in users_dict]
		blogs_dict[b.id] = blog_users

	return blogs_dict


print(attach_users2(blogs, users))
