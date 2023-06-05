import random
import numpy as np

total_nurses = 20
total_technicians = 5
total_midwives = 10
total_days = 30
nurses, technicians, midwives = [], [], []

def generate(total_days, total):
    list = []
    for i in range(total_days):
        temp = []
        num_of_zeros = random.randint(0, 10)
        for j in range(total):
            element = random.choice([[0,0], [0,1], [1,0], [1,1]])
            if sum(element) == 0 and num_of_zeros >= 2:
                num_of_zeros -= 2
                temp.append(element)
            elif sum(element) == 1 and num_of_zeros >= 1:
                num_of_zeros -= 2
                temp.append(element)
            else:
                temp.append([1, 1])

        list.append(temp)
    return list

nurses = generate(total_days, total_nurses)
technicians = generate(total_days, total_technicians)
midwives = generate(total_days, total_midwives)
print(nurses)
print(technicians)
print(midwives)
