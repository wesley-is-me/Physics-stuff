N = 1
T = int(input('How many people are there? '))
while N < T:
    N = N * 2

N = N / 2


F = T - N

B = T - (2 * F)


print(f'You need {B} byes.')
 

