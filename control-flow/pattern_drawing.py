size = int(input("Enter the size of the pattern:"))
count = 0

while count < size:
    for x in range(size):
        print(f'{size * '*'}')
        count = count + 1