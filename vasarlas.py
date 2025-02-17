f = open('vasarlas.csv', 'r')
sor = f.readline()
sor = sor.strip().split(";")

print(sor)

def nap():
    napok = 0
    for i in sor:
        napok += 1
    print(napok, "nap volt a hónapban.")
nap()

