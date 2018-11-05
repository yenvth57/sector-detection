import csv
sector_name: str = input('Please input a sector name: ')
with open('input.csv', 'r') as sector:
    r = csv.reader(sector)
    for i in range(len(r)):
        if sector_name in r[i][13]:
            print(r[i])
