#updating 
lst = [11, 45, 2, 4, 6, 1]
print(lst)

lst.append(10) #append function can update the list it can add only one element 
print(lst)

lst.sort() #sort function arranges values from min to max
print(lst)

lst.sort(reverse=True)
print(lst)

lst.reverse() #this function reverse the original list
print(lst)

# print(lst.index(1)) #this fun returns the index of the first occurence of the list item
# print(lst)

lst.extend([46]) # this function add more than one element
print(lst)

m = [100,200,300]
lst.extend(m);    

lst.remove(45) #this function removes the elemnet from the list
print(lst)

# m = lst.copy() #this copy the list

# for join the two list
# k = m + lst
# print(k)
# print(lst)