size = int(input('Enter size: '))

if len(str(size * size))> 4:
    largest = len(str(size * size))
else:
    largest = 4
for col in range(1, size + 1):
    for row in range(1, size + 1):
        print(f'{row * col:>{largest}}', end=' ')
    print()
