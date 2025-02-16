fruits=["apple","banana","cherry","orange"]
print("Accessing elements through index: ")
print(f"first: {fruits[0]}")
print(f"third: {fruits[2]}")
print(f"last: {fruits[-1]}")

fruits[1]="kiwies"

print(f"modified list: {fruits}")

fruits.remove("apple")
print(f"modified list: {fruits}")

length=len(fruits)

print(length)

fruits.sort()
print(f"Sorted list is : {fruits}")
