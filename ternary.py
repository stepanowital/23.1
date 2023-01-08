# greeting_msg = 'Hello'
# name = input("Введите ваше имя, уважаемый!\n")
#
# if name:
# 	greeting_msg += f', {name.upper()}!'
#
# print(greeting_msg)
#
# greeting_msg = f'Hello, {name.upper()}!' if name else 'Hello'
# print(greeting_msg)


DEFAULT = 1
def_value = 10

new_def_value = def_value or DEFAULT
print(new_def_value)

a = [1, 2, 0, 3, 4, 5, 0, 6, 7, 8, 0, 9]

res = [item if item else 'Пусто' for item in a]
print(res)
