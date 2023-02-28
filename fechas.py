import datetime as dt

hoy = dt.date.today()

print(hoy)

fecNac = dt.date(1977,6,14)

print(fecNac)


print(fecNac.year)
print(fecNac.day)
print(fecNac.month)
print(f"{hoy:%A,%B %d,%Y}")
print(f"{fecNac:%A,%B %d,%Y}")
print(f"{hoy:%d/%m/%y}")


for x in range(0,128):
    print(chr(x))
print("con while")
while contador < 127:
    print(chr(contador))
    contador+=1