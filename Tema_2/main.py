#Definim lista initiala
init_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

#Copiem lista si sortam copia crescator
asc_list = init_list.copy()
asc_list.sort()

#Copiem lista si sortam copia descrescator
desc_list = init_list.copy()
desc_list.sort(reverse=True)

#Fiecare al doilea element incepand cu primul este pe o pozitie para
even_pos_elem = init_list[::2]
#Fiecare al doilea element incepand cu al doilea este pe o pozitie impara
uneven_pos_elem = init_list[1::2]

#Definim o lista goala in care punem multpli lui 3
three_multiple = []

for x in init_list :
    if x%3==0:
        three_multiple.append(x)

print("Lista initiala:", init_list)
print("Lista sortata crescator:", asc_list)
print("Lista sortata descrescator:", desc_list)
print("Numere cu indici pari:",even_pos_elem)
print("Numere cu indici impari:",uneven_pos_elem)
print("Lista multiplilor lui 3:",three_multiple)
