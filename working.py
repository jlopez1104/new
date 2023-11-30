import csv
file = open('Stars.csv','w')

new_rec = 'Brian,73,Tarus\n'
file.write(new_rec)

file.close()
for i in range(3):
    file = open('Stars.csv','a')
    name = input('enetr name: ')
    age = int(input('enter age: '))
    star = input('enter start symbol: ')
    new_rec = name + ',' + str(age) + ',' + star + '\n'
    file.write(new_rec)
    file.close

file = open('Stars.csv','r')

for row in file:
    print(row)

file.close()

print('the better way')

file = open('Stars.csv','r')
reader = csv.reader(file)
database = list(reader)
print(database)
file.close()
