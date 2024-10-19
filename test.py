import math


class house:
    def __init__(self):
        self.age = 0
def run(years):
    money = 20000
    houses = []
    delta = 0
    for year in range(years):
        if year <= 4:
            money += 1000
        if year >= 4 and len(houses) < 10 and year < 50:
            money += 100000 + year * 10000
        # if year > 10:
        #     money -= 100000
        while year < 50 and money >= 300000:
            money -= 300000
            houses.append(house())
        for h in houses:
            h.age += 1
            if h.age >= 20:
                money += 20000 * 0.8
        # print("delta = "+ str(money - delta))
        delta = money
        print("At age " + str(year + 18) + " you have " + str(len(houses)) + " houses and $" + str(money))
    tot = money + len(houses) * 300000 * math.pow(1.02, sum(f.age for f in houses)/len(houses))
    print(tot)
    return tot
run(60)
# print(run(64) - run(60))
