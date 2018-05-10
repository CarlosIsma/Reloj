import time, os
print(time.localtime())

t=time.localtime()
year=t[0]
month=t[1]
day=t[2]
print("")
print("La fecha es: ",year,"/",month,"/",day)

print("")
print("***Reloj***")

seg=t[5]
while seg<60:
    h=time.localtime()

    print("La hora es: ",h[3],":",h[4],":",h[5])
    time.sleep(1)
