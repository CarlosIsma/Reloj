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
    t=time.localtime()

    print("La hora es: "+str(t[3])+":"+str(t[4])+":"+(str(t[5])))
    time.sleep(1)
