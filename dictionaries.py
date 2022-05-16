# this_dict = {
# 	"brand": "Ford",
# 	"model": "Mustang",
# 	"year": 1964
# }
# print(this_dict)
# print(this_dict["model"])
# print(this_dict.get("brand"))

# x = this_dict.keys()
# print(x)
# y = this_dict.values()
# print(y)

# this_dict["year"] = 2018
# this_dict.update({"year": 2020})
# this_dict.update({"color": "red"})		
# print(this_dict)

# for i in this_dict:
# 	print(i)

# for x, y in this_dict.items():
# 	print(y)	

# for x in this_dict:
#     print(this_dict[x])	


dict_1 = {
	"date": 11,
	"month": "June",
	"year": 1992
}

dict_2 = {
	"name": "Mariam",
	"surname": "Yepremyan"
}

dict_3 = {
	"n": "Mariam",
	"s": "Yepremyan"
}
new_dict = dict_1 | dict_2 | dict_3
print(new_dict)

# # dict_1.update(dict_2)
# # print(dict_1)



# d ={{x:y for x,y in dict_1.items()}
# print(d)


# dict_sample = {"a": 100, "b": 200, "c": 300}
# for x,y in dict_sample.items():
# 	if y == 200:
# 		print("true")


# sampledict = {
# 	"emp1": {"name": "john", "salary": 7500},
# 	"emp2":{"name": "Brand", "salary": 6500}
# }
# sampledict["emp2"] = {"name": "Brand", "salary": 8500}
# print(sampledict)