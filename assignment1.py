# ================================
# Lab Assignment 1
# ================================

# ----------------
# Task 1: Merge two lists and sort
# ----------------
# We will take input for two lists, merge them, and display in sorted order.

list1 = []
n1 = int(input("How many numbers in list1? "))
for i in range(n1):
    num = int(input("Enter number for list1: "))
    list1.append(num)   

list2 = []
n2 = int(input("How many numbers in list2? "))
for i in range(n2):
    num = int(input("Enter number for list2: "))
    list2.append(num)   


merged = list1 + list2
merged.sort()

print("Sorted merged list:", merged)


# ----------------
# Task 2: Smallest and largest
# ----------------
# Take numbers from the user and find the smallest and largest using min() and max().

numbers = []
n = int(input("\nEnter no of numbers for finding their MAX & MIN \ "))
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Smallest number is:", min(numbers))
print("Largest number is:", max(numbers))


# ----------------
# Task 3: Birthday dictionary
# ----------------
# Store some birthdays in a dictionary and let user look them up.

birthdays = {
    "Zain ul Abiden": "03/14/2000",
    "Arsalan khan": "01/17/2006",
    "Uzair khan": "12/10/2003",
    "Shahzeb khan": "12/10/2004",
    "Zuhaib khan": "12/10/2005"
}

print("\nWe know birthdays of:")
for key in birthdays:
    print(key)

name = input("Enter a name to find their birthday: ")

if name in birthdays:
    print("Name", name, "was born on", birthdays[name])
else:
    print("Sorry, not found")


# ----------------
# Task 4: Extract keys from dictionary
# ----------------
# From the given dictionary, we only want 'name' and 'salary'.

myDict = {
    "name": "Arsalan",
    "age": 20,
    "salary": 40000,
    "city": "Pakistan"
}

keys = ["name", "age"]
newDict = {}

for k in keys:
    if k in myDict:
     newDict[k] = myDict[k]

print("The extracted keys in New dictionary:", newDict)
