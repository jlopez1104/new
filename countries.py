file = open('countries.txt','w')
file.write('Italy\n')
file.write('Portugal\n')
file.write('Zimbabwe\n')
file.write('Chine\n')
file.close

file = open('countries.txt','r')
print(file.read())
file.close

file = open('countries.txt','a')
file.write('united arab emirates\n')
file.close