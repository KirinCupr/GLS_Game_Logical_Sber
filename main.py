import random

def get_rand_matr(n):
    numbers = [i for i in range(1, n**2+1)]
    matr = [[0 for i in range(n)] for j in range(n)]
    #print(matr)
    for i in range(n):
        for j in range(n):
            flag = True
            while (flag):
                rand_number = 1 + int(random.random() * 100) % (n**2+1)
                if (not(is_number_in_array(numbers, rand_number))): continue
                matr[i][j] = rand_number
                numbers.remove(rand_number)
                flag = False
    return matr

def is_number_in_array(arr, number):
    for i in arr:
        if (i == number): return True
    return False

# print(get_rand_matr(4))

matr = get_rand_matr(3)

for i in matr:
    print(i) 
