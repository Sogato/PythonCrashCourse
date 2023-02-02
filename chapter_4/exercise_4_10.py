oddNumbers = [number for number in range(1, 21, 2)]
for number in oddNumbers:
    print(number)

print(f'The first three items in the list are: {oddNumbers[0:3]}')
print(f'Three items from the middle of the list are: {oddNumbers[4:7]}')
print(f'The last three items in the list are: {oddNumbers[-3:]}')
