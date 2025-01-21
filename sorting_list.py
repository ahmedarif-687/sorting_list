"""
this is the code where there are 3 list input
 and i am removign the dulicates
 """

STRING_1="abcd"
STRING_2="defg"
STRING_3="cbfz"

list_1=list(STRING_1)
list_2=list(STRING_2)
list_3=list(STRING_3)

input_list=list_1+ list_2 + list_3
input_list.sort()

print("Actual list: ",input_list)

unique_list=[]
duplicate_list=[]

#print(d)

for i in input_list:
    if i not in unique_list:
        unique_list.append(i)
    elif i in unique_list:
        duplicate_list.append(i)

print("Unique Elements: ", unique_list)
print("Duplicate Elements: ", duplicate_list)
removed_duplicate_element_list = list( set(unique_list) - set(duplicate_list))
print("removed Duplicate Elements: ", removed_duplicate_element_list)
