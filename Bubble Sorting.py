import time
import random
my_list = random.sample(range(10000), 10000)
def bubble(bad_list):
    Length = len(bad_list) - 1
    Sorted = False
    while not Sorted:
        Sorted = True
        for i in range(Length):
            if bad_list[i] > bad_list[i+1]:
                Sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
bubble(my_list)
print(my_list)
