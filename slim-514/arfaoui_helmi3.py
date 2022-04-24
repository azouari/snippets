from statistics import mean


records = []
with open('NOTES.csv', 'r') as f:
    data = f.read()
    print(data)
    data = data.splitlines()
    print(data)
    data = data[1:]
    for record in data:
        moyenne = mean([int(value) for value in record.split(';')[4:]])
        a = record.split(';')[:3]
        a.append(moyenne)
        records.append(a)

with open('moyenne.csv', 'wt') as f:
    f.write('NodeDA; Nom; Prenom; Moyenne\n')
    for record in records:
        value = '; '.join([str(val) for val in record]) + '\n'
        f.write(value)
        
