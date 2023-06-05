import random
import math
import numpy as np

min_shifts, max_shifts = 10, 23  # Declaring min and max number of shifts
N = 30  # Number of days
S = 2  # Number of shifts
# Declaring number of employees
total_nurses = 20
total_laboratory_technicians = 5
total_midwives = 10
# Declaring requried minimum of each group of employees
min_nurses = 4
min_laboratory_technicians = 1
min_midwives = 2

# Declaring requested by employees work schedule
declared_nurses = [
    [[1, 1], [0, 0], [1, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 0], [1, 1], [0, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 0], [0, 0], [1, 1], [0, 1], [0, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[0, 1], [1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 0], [1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[0, 1], [0, 0], [1, 0], [0, 0], [1, 1], [1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[0, 1], [1, 1], [0, 0], [1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[0, 0], [0, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 1], [1, 0], [1, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[0, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 0], [0, 0], [0, 0], [0, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[0, 1], [0, 1], [1, 1], [1, 0], [0, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[0, 0], [0, 1], [1, 0], [1, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[0, 1], [0, 0], [0, 0], [1, 1], [0, 1], [0, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 1], [1, 1], [1, 0], [0, 1], [1, 0], [1, 1], [0, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 0], [1, 1], [1, 0], [0, 0], [0, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[0, 0], [0, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[0, 1], [1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 1], [0, 0], [1, 0], [0, 0], [0, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 0], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 0], [0, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
    [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1],
     [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]]
declared_laboratory_technicians = [[[1, 0], [1, 1], [1, 0], [1, 1], [1, 1]], [[0, 0], [1, 0], [0, 0], [1, 1], [1, 1]],
                                   [[0, 1], [0, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                                   [[0, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [1, 0], [0, 1], [1, 0], [1, 1]],
                                   [[0, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [0, 0], [0, 0], [0, 0], [1, 0]],
                                   [[0, 1], [1, 1], [1, 1], [1, 1], [1, 0]], [[1, 1], [1, 1], [0, 1], [1, 0], [1, 0]],
                                   [[0, 0], [1, 1], [0, 1], [1, 1], [1, 1]], [[1, 0], [1, 1], [1, 1], [1, 1], [1, 1]],
                                   [[1, 0], [0, 0], [1, 1], [0, 0], [0, 0]], [[0, 1], [1, 1], [1, 0], [1, 0], [1, 1]],
                                   [[1, 0], [0, 1], [1, 0], [1, 1], [1, 1]], [[0, 1], [1, 0], [0, 0], [0, 1], [1, 1]],
                                   [[0, 0], [1, 0], [1, 1], [1, 1], [1, 1]], [[1, 0], [1, 1], [1, 0], [0, 0], [1, 1]],
                                   [[0, 0], [0, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [1, 1], [1, 1], [0, 0], [1, 1]],
                                   [[0, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [0, 0], [0, 0], [1, 1], [1, 1]],
                                   [[0, 0], [1, 1], [0, 0], [1, 0], [1, 1]], [[0, 1], [0, 0], [1, 1], [1, 1], [1, 1]],
                                   [[1, 0], [0, 0], [1, 1], [0, 1], [1, 1]], [[1, 0], [1, 1], [1, 1], [0, 1], [1, 1]],
                                   [[1, 0], [0, 0], [0, 1], [0, 0], [1, 1]], [[1, 1], [0, 1], [1, 0], [1, 0], [1, 1]],
                                   [[1, 0], [0, 1], [0, 1], [1, 1], [1, 1]], [[0, 0], [1, 1], [1, 1], [1, 1], [1, 1]]]
declared_midwives = [[[1, 0], [0, 0], [1, 1], [0, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [1, 1], [0, 0], [0, 0], [1, 1], [0, 0], [1, 1], [0, 0], [1, 0], [1, 1]],
                     [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [0, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 0], [1, 0], [1, 0], [0, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [1, 1], [1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[0, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [1, 1], [1, 1], [0, 1], [0, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1]],
                     [[0, 0], [0, 1], [1, 1], [1, 1], [0, 0], [0, 1], [1, 0], [1, 1], [1, 1], [1, 1]],
                     [[1, 0], [0, 0], [1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[0, 0], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [1, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[0, 0], [0, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[0, 1], [1, 1], [1, 0], [1, 0], [0, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [0, 0], [1, 1], [1, 1], [1, 0], [1, 0], [0, 0], [0, 1], [1, 1], [1, 1]],
                     [[0, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[1, 1], [0, 1], [1, 0], [1, 1], [0, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[0, 1], [0, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
                     [[0, 0], [1, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 0], [0, 0], [1, 1], [1, 0]],
                     [[1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]]

def calculate_total_employees(schedule_nurses, schedule_technicians, schedule_midwives):
    total_shifts_nurses = np.sum(schedule_nurses)
    total_shifts_technicians = np.sum(schedule_technicians)
    total_shifts_midwives = np.sum(schedule_midwives)
    return total_shifts_nurses + total_shifts_technicians + total_shifts_midwives


# Checking if all constraints are satisfied with new schedules, if not adding to cost value used in objective function
def verify_solutions(schedule_nurses, schedule_technicians, schedule_midwives):
    punish_cost = 0
    punishment = 999999
    # Each employee can work only one shift a day
    for day in range(N):
        for employee in range(total_nurses):
            if sum(schedule_nurses[day][employee]) == 2:
                punish_cost += punishment
        for employee in range(total_laboratory_technicians):
            if sum(schedule_technicians[day][employee]) == 2:
                punish_cost += punishment
        for employee in range(total_midwives):
            if sum(schedule_midwives[day][employee]) == 2:
                punish_cost += punishment

    # Each employee can't take day shift after a night shift
    for day in range(N - 1):
        for employee in range(total_nurses):
            if schedule_nurses[day][employee][1] + schedule_nurses[day + 1][employee][0] == 2:
                punish_cost += punishment
        for employee in range(total_laboratory_technicians):
            if schedule_technicians[day][employee][1] + schedule_technicians[day + 1][employee][0] == 2:
                punish_cost += punishment
        for employee in range(total_midwives):
            if schedule_midwives[day][employee][1] + schedule_midwives[day + 1][employee][0] == 2:
                punish_cost += punishment

    # Each employee must work between minimum and maximum number of shifts
    for employee in range(total_nurses):
        employee_sum = 0
        for day in range(N):
            employee_sum += sum(schedule_nurses[day][employee])
        if employee_sum < min_shifts or employee_sum > max_shifts:
            punish_cost += punishment
    for employee in range(total_laboratory_technicians):
        employee_sum = 0
        for day in range(N):
            employee_sum += sum(schedule_technicians[day][employee])
        if employee_sum < min_shifts or employee_sum > max_shifts:
            punish_cost += punishment
    for employee in range(total_midwives):
        employee_sum = 0
        for day in range(N):
            employee_sum += sum(schedule_midwives[day][employee])
        if employee_sum < min_shifts or employee_sum > max_shifts:
            punish_cost += punishment

    # Employee can't be assigned to shift if he requested holiday on certain shift
    for day in range(N):
        for employee in range(total_nurses):
            for shift in range(S):
                if declared_nurses[day][employee][shift] == 0 and schedule_nurses[day][employee][shift] == 1:
                    punish_cost += punishment
        for employee in range(total_laboratory_technicians):
            for shift in range(S):
                if declared_laboratory_technicians[day][employee][shift] == 0 and schedule_technicians[day][employee][shift] == 1:
                    punish_cost += punishment
        for employee in range(total_midwives):
            for shift in range(S):
                if declared_midwives[day][employee][shift] == 0 and schedule_midwives[day][employee][shift] == 1:
                    punish_cost += punishment

    # Required minimum number of employees on each shift from each profession must be satisfied
    for day in range(N):
        for shift in range(S):
            if sum(schedule_nurses[day][:][shift]) < min_nurses:
                punish_cost += punishment
            if sum(schedule_technicians[day][:][shift]) < min_laboratory_technicians:
                punish_cost += punishment
            if sum(schedule_midwives[day][:][shift]) < min_midwives:
                punish_cost += punishment

    return punish_cost


def generate_neighbour(schedule_nurses, schedule_technicians, schedule_midwives):
    new_schedule_nurses = schedule_nurses
    new_schedule_technicians = schedule_technicians
    new_schedule_midwives = schedule_midwives

    day = random.randint(0, N - 1)
    shift = random.randint(0, 1)
    profession = random.randint(0,2)
    temp = random.random()
    if profession == 0:
        nurse = random.randint(0, total_nurses - 1)
        if temp <= 0.5:
            new_schedule_nurses[day][nurse][shift] = 1
        else:
            new_schedule_nurses[day][nurse][shift] = 0
    elif profession == 1:
        technician = random.randint(0, total_laboratory_technicians - 1)
        if temp <= 0.5:
            new_schedule_technicians[day][technician][shift] = 1
        else:
            new_schedule_technicians[day][technician][shift] = 0
    else:
        midwife = random.randint(0, total_midwives - 1)
        if temp <= 0.5:
            new_schedule_midwives[day][midwife][shift] = 1
        else:
            new_schedule_midwives[day][midwife][shift] = 0

    punish_cost = verify_solutions(new_schedule_nurses, new_schedule_technicians, new_schedule_midwives)

    return new_schedule_nurses, new_schedule_technicians, new_schedule_midwives, punish_cost


def simulated_annealing():
    # Generating first solution, where each worker is assigned maximum allowed number of shifts
    current_schedule_nurses = [[[0, 0] for _ in range(total_nurses)] for _ in range(N)]
    current_schedule_technicians = [[[0, 0] for _ in range(total_laboratory_technicians)] for _ in range(N)]
    current_schedule_midwives = [[[0, 0] for _ in range(total_midwives)] for _ in range(N)]
    def assign_maximum_shifts(schedule, total_employees):
        shift = random.randint(0, 1)
        for employee in range(total_employees):
            i = 0
            while i <= min_shifts:
                day = random.randint(0, N - 1)
                if schedule[day][employee][shift] == 0:
                    schedule[day][employee][shift] = 1
                    i += 1
        return schedule

    current_schedule_nurses = assign_maximum_shifts(current_schedule_nurses, total_nurses)
    current_schedule_technicians = assign_maximum_shifts(current_schedule_technicians, total_laboratory_technicians)
    current_schedule_midwives = assign_maximum_shifts(current_schedule_midwives, total_midwives)

    best_schedule_nurses = current_schedule_nurses
    best_schedule_technicians = current_schedule_technicians
    best_schedule_midwives = current_schedule_midwives

    current_total_shifts = calculate_total_employees(current_schedule_nurses, current_schedule_technicians, current_schedule_midwives) + verify_solutions(current_schedule_nurses, current_schedule_technicians, current_schedule_midwives)
    best_total_shifts = current_total_shifts

    temperature = 1000
    cooling_rate = 0.97

    max_iter = 10000 # Allowed number of iterations
    total_iter = 0

    while temperature > 0.1:
        new_schedule_nurses, new_schedule_technicians, new_schedule_midwives, punish_cost = generate_neighbour(
            current_schedule_nurses, current_schedule_technicians, current_schedule_midwives)
        new_total_shifts = calculate_total_employees(new_schedule_nurses, new_schedule_technicians, new_schedule_midwives) + punish_cost
        delta_total_shifts = new_total_shifts - current_total_shifts

        if delta_total_shifts < 0 or math.exp(-delta_total_shifts / temperature) > random.random():
            current_schedule_nurses = new_schedule_nurses
            current_schedule_technicians = new_schedule_technicians
            current_schedule_midwives = new_schedule_midwives
            current_total_shifts = new_total_shifts

        if current_total_shifts < best_total_shifts:
            best_schedule_nurses = current_schedule_nurses
            best_schedule_technicians = current_schedule_technicians
            best_schedule_midwives = current_schedule_midwives
            best_total_shifts = current_total_shifts

        temperature *= cooling_rate

        if total_iter >= max_iter:
            print("Iteration limit exceeded")
            break
        total_iter += 1

    return best_schedule_nurses, best_schedule_technicians, best_schedule_midwives

best_schedule_nurses, best_schedule_technicians, best_schedule_midwives = simulated_annealing()

# Visualize solutions
def visualize_shifts(schedule, name):
    day_shifts = []
    night_shifts = []
    for day in schedule:
        temp_day_shifts = []
        temp_night_shifts = []
        for i in range(len(day)):
            if day[i][0] == 1:
                temp_day_shifts.append(i+1)
            elif day[i][1] == 1:
                temp_night_shifts.append(i+1)
        day_shifts.append(temp_day_shifts)
        night_shifts.append(temp_night_shifts)

    def print_shifts(schedule):
        day_index = 1
        for day in schedule:
            print(f"Day {day_index}: {day}")
            day_index += 1
    print(f"Day shift for {name}:")
    print_shifts(day_shifts)
    print(f"Night shift for {name}:")
    print_shifts(night_shifts)

total_shifts_worked = 0
def cos(name, data):
    print("=" * 50)
    print(name)
    all_employees = []
    for i in range(np.shape(data)[1]):
        curr_column = [row[i] for row in data]
        total = 0
        for row in curr_column:
            total += sum(row)
        print(f"Row {i+1} total: {total}")
        all_employees.append(total)
    print("All employees: ", all_employees)
    global total_shifts_worked
    total_shifts_worked += np.sum(all_employees)
cos("Nurses", best_schedule_nurses)
cos("Lab technicians", best_schedule_technicians)
cos("Midwives", best_schedule_midwives)
print("Total shifts worked: ", total_shifts_worked)
#visualize_shifts(best_schedule_nurses, "nurse")
#visualize_shifts(best_schedule_technicians, "laboratory technician")
#visualize_shifts(best_schedule_midwives, "midwife")
