import time
print(time.localtime())

t=time.localtime()
year=t[0]
month=t[1]
day=t[2]
hour=t[3]
min=t[4]
sec=t[5]

print("La fecha es: ",year,"/",month,"/",day)
print("La hora es: ",hour,":",min,":",sec)
