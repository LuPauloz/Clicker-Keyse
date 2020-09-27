import context
import keyse
from time import perf_counter, localtime
from datetime import datetime

# keyse.save_file(lista, "file")'''

lista = keyse.record()
ini = datetime.now()
keyse.play(lista)
fin = datetime.now()
print("Total gravação ", lista[-1]["time"])
print("Total de tempo corrido ", fin - ini)

# keyse.save_file(lista, "file")

# lista2 = keyse.load_file("file")



# record = keyse.Clickerpy()

# record.play(lista2)


# ini = datetime.now()

# while True:
#     ttt = perf_counter()
#     if ttt < 5:
#         continue
#     break

# fin = datetime.now()

# import time

# lista = keyse.record()
# keyse.play(lista)

# # ini = perf_counter()
# # # keyse.play(lista)
# # fin = perf_counter()
# # print("Total de tempo corrido ", fin - ini)
# for i in lista:
#     print(i)