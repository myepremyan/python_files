# def my_function():
# 	return "hallo world"
# my_function()


# def square_valu(num):
# 	return num ** 2
# print(square_valu(2))
# print(square_valu(-4))


# def my_function(name):
# 	print("my name is ", name)
# my_function("Jhon")
# my_function("Jane")


# def my_function(fname, lname):
# 	print(fname + " " + lname)
# my_function("Emil", "Kusturica")


# def myfunc1():
# 	x = "jhon"
# 	def myfunc2():
# 		nonlocal x
# 		x = "hello"
# 	myfunc2()
# 	return x
# print(myfunc1())

# lst = [8,2,3,0,7]
# def my_function():
# 	return sum(lst)
# print(my_function())

# myrange = range(0,10)
# def my_f():
# 	return [num for num in numbers]
# print(my_f(myrange))



# def my_f(num):
# 	if num in range(0,10):
# 		print(num, 'is in range')
# 	else:
# 		print(num, 'is not in range')
# my_f(5)



# my_str = "The quick Brown Fox"
# def new_funct():
# 	for i in my_str:
# 		if i.isupper():
# 			print("Upper letters are" + sum(i))
# 	for j in my_str:
# 		if j.islower():
# 			print("lower letters are" + sum(j))
# new_funct()



# lst_1 = [1,6,4,4,8,8]
# lst_2 = []
# def my_function():
# 	for i in lst_1:
# 		if i not in lst_2:
# 			lst_2.append(i)
#
# #my_function()
# print(my_function())


# def countdown(n):
# 	print(n)
# 	if n == 0:
# 		return
# 	else:
# 		countdown(n-1)
# countdown(5)


def factorial_recursive(n):
	1 != 1
if n == 1:
	return 1
	n! = n * (n-1)!
else:
	n * factorial_recursive(n-1)
factorial_recursive(5)
