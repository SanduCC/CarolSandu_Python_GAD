from class_Fractie import *

fr1 = Fractie(2,4)
fr2 = Fractie(3,2)
print("Fractia 1:",fr1)
print("Fractia 2:",fr2)
print()

sum_fr = fr1.__add__(fr2)
print("Suma fractiilor:",sum_fr)

dif_fr = fr1.__sub__(fr2)
print("Diferenta fractiilor:",dif_fr)

print()

inv_fr1 = fr1.inverse()
inv_fr2 = fr2.inverse()
print("Inversa fractiei 1:",inv_fr1)
print("Inversa fractiei 2:",inv_fr2)