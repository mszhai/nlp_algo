
import random
import matplotlib.pyplot as plt

def coin():
    init_gold, person, minutes = 100, 500, 10000
    golds = [init_gold] * person
    for m in range(minutes):
        for p in range(person):
            if golds[p] > 0:
                golds[p] -= 1
                choice_person = random.randint(0, person-1)
                golds[choice_person] += 1
    
    for i in golds:
        print(i)

if __name__ == '__main__':
    coin()

