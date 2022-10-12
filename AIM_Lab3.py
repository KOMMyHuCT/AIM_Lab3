import csv
import pandas as ps
import statistics
import random
import names
import matplotlib.pyplot as pyplot
from enum import Enum
ps.set_option('display.max_rows', None)
ps.set_option('display.max_columns', None)
ps.set_option('display.max_colwidth', None)

#„H„p„t„p„~„y„u „Š„p„„{„y
header = ['id', 'fullName', 'sex', 'yearOfBirth', 'enrolled', 'department', 'job', 'pay', 'completedProjects']

#„H„p„t„p„~„y„u „r„€„x„}„€„w„~„„‡ „x„~„p„‰„u„~„y„z „t„|„‘ „„€„|„p
class Sex(Enum):
    Male = 0
    Female = 1

#„H„p„t„p„~„y„u „r„€„x„}„€„w„~„„‡ „x„~„p„‰„u„~„y„z „t„|„‘ „„€„t„‚„p„x„t„u„|„u„~„y„‘
class Department(Enum):
    Main = 0
    Auxiliary = 1
    Support = 2

#„H„p„t„p„~„y„u „r„€„x„}„€„w„~„„‡ „x„~„p„‰„u„~„y„z „t„|„‘ „D„€„|„w„~„€„ƒ„„„y
class Job(Enum):
    Developer = 0
    Tester = 1
    Support = 2

#„H„p„„y„ƒ„ „r „†„p„z„|
with open('test.csv', 'w') as f:
    writer = csv.writer(f)
    #„H„p„„y„ƒ„ „Š„p„„{„y
    writer.writerow(header)
    #„B„„q„€„‚ „ƒ„|„…„‰„p„z„~„€„s„€ „{„€„|„y„‰„u„ƒ„„„r„p „ƒ„„„‚„€„{ „€„„ 1001 „t„€ 2000
    nRows = random.randint(1001, 2000);
    #„H„p„„y„ƒ„ „ƒ„„„‚„€„{
    for i in range(0, nRows):
        row = []
        sex = random.choice(list(Sex))
        if sex == Sex.Male:
            row = [i, names.get_first_name('male') + " " + names.get_last_name(), sex, random.randint(1940, 2004), random.randint(2010, 2022), random.choice(list(Department)), random.choice(list(Job)), random.randint(20000, 60000), random.randint(0, 10)]
        else:
            row = [i, names.get_first_name('female') + " " + names.get_last_name(), sex, random.randint(1940, 2004), random.randint(2010, 2022), random.choice(list(Department)), random.choice(list(Job)), random.randint(20000, 60000), random.randint(0, 10)]
        writer.writerow(row)

pay = []
with open('test.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        #print(row)
        pay.append(float(row['pay']))
    print('\nMax of Pay:\n', max(pay))
    print('\nMin of Pay:\n', min(pay))
    print('\nMean of Pay:\n', statistics.mean(pay))
    print('\nDispersion of Pay:\n', max(pay) - min(pay))
    print('\nStandard deviation of Pay:\n', statistics.stdev(pay))
    print('\nMedian of Pay:\n', statistics.median(pay))

dataframe = ps.read_csv('test.csv')
print('\nDescription:\n', dataframe.describe())
print('\nCount:\n', dataframe.count())
#print('\nDuplicated:\n', dataframe.duplicated(keep = False))
#print('\nIs N/A:\n', dataframe.isna())
print('\nMax of Pay:\n', max(dataframe['pay']))
print('\nMin of Pay:\n', min(dataframe['pay']))
print('\nMean of Pay:\n', statistics.mean(dataframe['pay']))
print('\nDispersion of Pay:\n', max(dataframe['pay']) - min(dataframe['pay']))
print('\nStandard deviation of Pay:\n', statistics.stdev(dataframe['pay']))
print('\nMedian of Pay:\n', statistics.median(dataframe['pay']))

pyplot.scatter(dataframe['enrolled'], dataframe['pay'])
pyplot.title('Dependence of salary on the year of enrollment')
pyplot.show()

pyplot.scatter(dataframe['completedProjects'], dataframe['pay'])
pyplot.title('Dependence of salary on the number of completed projects')
pyplot.show()

pyplot.scatter(dataframe['enrolled'], dataframe['completedProjects'])
pyplot.title('Dependence of the number of completed projects on the year of enrollment')
pyplot.show()