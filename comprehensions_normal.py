from statistics import mean
from enum import Enum
with open("data.txt") as better_open_file:
    data = better_open_file.read()


sentence = "List comprehensions are the Greatest!"

def remove_vowels(sentence):
    vowel = "aeiouAEIOU"
    return "".join([letter for letter in sentence if letter not in vowel])
print(remove_vowels(sentence))


data = data.split("\n")
new_list = []
for x in range(0,31):
    new_list.append(data[x].split(","))


def water_temp(new_list):
    water_temps = [row[4] for row in new_list]
    return water_temps
#print(water_temp(new_list))

def water_float(water_temps):
    water_floats = [float(x) for x in water_temps if not x == "Water Temp"]
    return water_floats
print(water_float(water_temp(new_list)))
#water_floats = [float(x) for x in water_temps(new_list) if not x == "Water Temp"]

def farenheit(water_floats):
    farenheit_list = [int((x * 1.8) + 32) for x in water_floats]
    return farenheit_list
#print(farenheit(water_float(water_temp#(new_list))))
#farenheit = [int((x*1.8) + 32) for x in water_floats]


# date_height = {x[5]: x[1] for x in new_list}
# print(date_height)

def date_height(list):
    return {x[5]: x[1] for x in list}
#print(date_height(new_list))
#print(date_height(new_list))


gradebook = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
             'Jordan': {'Homework 1': 92, 'Homework 2': 87},
             'Peyton': {'Homework 1': 84, 'Homework 2': 77},
             'River': {'Homework 1': 85, 'Homework 2': 91}}

def grade_avg(gradebook):
    return mean([(value['Homework 1']) for key, value in gradebook.items()])



#Joel Taddei
class DayOfWeek(Enum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6


def get_day_of_week(year, month, day):
    month_table = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= 1 if month < 3 else 0
    return DayOfWeek(int((year + year / 4 - year / 100 + year / 400 + month_table[month - 1] + day) % 7))



def sep_date(new_list):
    return [[x[5].split("-"), x[1]] for x in new_list if not x[1] == 'Wave Height']
cut_date = sep_date(new_list)
#print(cut_date)
def calc_day_week(new_list):
    return [[get_day_of_week(int(x[0][0]), int(x[0][1]), int(x[0][2])), float(x[1])] for x in new_list]
#print(calc_day_week(cut_date))

def avg_day(data_list, day):
    return mean([x[1] for x in data_list if x[0] == day])


def make_day_height_dict(cut_date):
    return {day: avg_day(calc_day_week(cut_date), day) for day in DayOfWeek}
print(make_day_height_dict(cut_date))
