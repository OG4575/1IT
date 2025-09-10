#1
numbers = []
numbers.append("1")
numbers.append("2")
numbers.append("3")
numbers.append("4")
numbers.append("5")
print(numbers)

#2
names = []

for i in range(5):
    name = input(f"Zadej {i+1}. jméno: ")
    names.append(name)

names.sort()

print("Seřazená jména:", names)

#3
numberstwo = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
numberstwo.pop()
numberstwo.pop()
numberstwo.pop()
numberstwo.pop()
numberstwo.pop()
numberstwo.pop()
numberstwo.pop()
numberstwo.pop()
numberstwo.pop()
numberstwo.pop()
print(numberstwo)

