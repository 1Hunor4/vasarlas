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

def nemkoltes():
    uresnap = 0
    for i in sor:
        if i == "0":
            uresnap += 1
    print(uresnap, "napon nem történt költés.")
nemkoltes()

def napiatlag():
    szum = 0
    db = 0
    for i in sor:
        szum += int(i)
        db += 1
    atl = szum/db
    print("A napi átlagos költés:",round(atl),"ft")
napiatlag()

def max_min():
    lnagyobb = 0 
    lkisebb = 30876
    for i in sor:
        j = int(i)
        if j > lnagyobb:
            lnagyobb = j
        if j < lkisebb and j != 0:
            lkisebb = j
    print("A legnagyobb összeg:", lnagyobb, ", és", lkisebb, "a legkisebb összeg." )
max_min()

