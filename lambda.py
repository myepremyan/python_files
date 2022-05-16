# my_func = lambda a: a+10
# print(my_func(5))

# my_func = lambda a, b: a+b
# print(my_func(5, 10))


# def test_func(num):
# 	return lambda x: x * num
# result = test_func(10)
# print(result(9))


# numbers = (1, 2, 3, 4)
# result = map(lambda x: x * x, numbers)
# print(list(result))


# my_list = [10, 12, 14, 65, 54, 39]
# result = list(filter(lambda x: x % 2 == 0, my_list))
# print(result)



# my_list = [10, 12, 14, 65, 54, 39]
# result = filter(lambda x: x % 3 == 0, my_list)
# print(list(result))


# func = lambda x: x + 15
# print(func(10))

# func_2 = lambda x, y: x * y
# print(func_2(10, 5))


# lst = [10, 12, 14, 65, 54, 39]
# # result = map(lambda	x: x * x, lst)
# result = map(lambda	y: y ** 3, lst)
# print(list(result))


# lst = ["madam", "Map", "Gap"]
# result = filter(lambda x: x[0::] == x[::-1], lst)
# print(list(result))


# tup = [6, 5, 4, 2]
# odds = list(filter(lambda odd:  odd % 2 == 1, tup))
# evens = list(filter(lambda even: even % 2 == 0, tup))
# print(len(odds), len(evens))


# lst_1 = [1, 2, 3, 5, 7, 8, 9, 10]
# lst_2 = [1,2,4,8,9]
# result = list(filter(lambda x: x in lst_1, lst_2))
# print(result)


# x = lambda n: n **2 if n % 2 == 0 else n **3
# print(x(4))
# print(x(3))


# x = lambda n: n if n % 10 == 0 else n ** 2 if n % 2 == 0 else n **3
# print(x(4))
# print(x(3))
# print(x(10))


# lst_1 = [1, 2, 5, 8, 10, 15]
# new_lst = [i for i in lst_1 if i % 2 == 0]
# print(new_lst)


# new_lst = [i**2 for i in range(1,10)]
# print(new_lst)


# lst = [1, 2, 3, 4, 5, 6, 7]
# dic = {x:x ** 3 for x in lst if x % 2 ==0}
# print(dic)


# arr = [3, 4, -2, -10, 23, 20, -44, 1, -23]
# rearrange_numbers = lambda i: [x for x in arr if x < 0] + [x for x in arr if x >= 0]
# new_arr = rearrange_numbers(arr)
# print(new_arr)


