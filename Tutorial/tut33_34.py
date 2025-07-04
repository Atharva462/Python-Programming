# dictionaries in python 
# dic = {
#     "spoon": "a metal object",
#     "apple": "a fruit"
# }
# print(dic["apple"])
# print(type(dic))

# dic = {
#     1: "shubham",
#     8: "atharva",
#     453: "om",
#     123: "uma"
# }
# print(dic[8])

# info = {'name':'atharva', 'age':19, 'eligible':True}
# print(info)

info = {'name':'atharva', 'age':19, 'eligible':True}
# print(info['name'])
# print(info.get('eligible')) #this two ways are exactly the same thigs to print dictionory items
# print(info.keys()) #to access multiple keys 
# print(info.values()) 

# for key in info.keys():
# print(info[key]) #to access multiple keys
# print(f"the value corresponding to the key {key} is {info[key]}")
print(info.items())

