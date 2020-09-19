pages = int(input('Ведите кол-во страниц (кратно 4):'))
print('#' * 10)

while pages % 4 !=0:
    pages +=1
f = []
total_first_side = []
total_second_side = []
for el in range(pages):
    f.append(el)
f.remove(0)
f.append(pages)
semi = int(len(f)/2)
fir_semi = f[:semi]
sec_semi = f[semi:]

for els in sec_semi[::-2]:
    total_first_side.append(els)

i = 1

for els in fir_semi[::2]:

    total_first_side.insert(i, els)
    i += 2

print(f'Для печати лицевой стороны скопируйте следующие страницы: {total_first_side}')
print('#' * 10)

for els in fir_semi[::-2]:
    total_second_side.append(els)

r = 1

for els in sec_semi[::2]:

    total_second_side.insert(r, els)
    r += 2

print(f'Для печати оборотной стороны (после разворота стопки) скопируйте следующие страницы: {total_second_side}')

    

