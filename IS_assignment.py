# Task 1
list1=[]
list2=[]
n=int(input("Enter the Number of elements for first list:"))
for i in range(n):
    element=int(input(f"Enter element {i+1}:"))
    list1.append(element)
print("list1:",list1)
n=int(input("Enter the Number of elements for second list:"))
for i in range(n):
    element=int(input(f"Enter element {i+1}:"))
    list2.append(element)
print("list2:",list2)
merge_list=list1+list2
merge_list.sort()
print("After merging the sorted list is: ",merge_list)

# task 2
print("Maximum value is:",max(merge_list),"And minimum is :", min(merge_list))


# task 3
Birthday_dict={"Sumbal":"28 NOV,2004","Uswa":"07 FEB,2004","Brekhna":"4 Jan,2003","Komal":"28 AUG,2002","Manahil":"26 DEC,2006","Umama":"17 NOV,2004"}
print("Welcome to the Birthday Ductionary.we know the birthdays of:")
for key in Birthday_dict:
    print(key)
print("whose birthday do you want to look up:")
name=input("Enter the name:")
n=name.capitalize()
print(n," birthday is ",Birthday_dict[n])


# task 4
my_dict={"name":"Aliya","age":26,"subject":"information system","grade":"A"}
print("Here is Aliya's Detail:")
print(my_dict)
keys=input("Enter required keys to extraxt").split()
new_dict={}
for k in keys:
    if k in my_dict:
        new_dict[k]=my_dict[k]
print("Extraxted dictionary :",new_dict)
