string = input("Write your favorite word or sentence: ")

print(f"Original String is {string}")
print("Printing only even index chars:")

for char in range(0, len(string), 2):
    print(string[char])
