import csv
import statistics
import pandas as ps
ps.set_option('display.max_rows', None)
ps.set_option('display.max_columns', None)
ps.set_option('display.max_colwidth', None)

fare = []
with open('003_titanic.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        fare.append(float(row['Fare']))
    print('Median of Fare: ', statistics.median(fare))

dataframe = ps.read_csv('003_titanic.csv')
print('\nDescription:\n', dataframe.describe())
print('\nCount:\n', dataframe.count())
print('\nDuplicated:\n', dataframe.duplicated(keep = False))
print('\nIs N/A:\n', dataframe.isna())
print('\nMedian of Fare:\n', statistics.median(dataframe['Fare']))