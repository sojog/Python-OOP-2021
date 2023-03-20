#Importarea modului de time
import time



print ("Hello")
# time.sleep -> programul face o pauza de 2 secunde
time.sleep(0.2)


# time.time() -> programul intoarce nr de secunde de la 1 January 1970
print(time.time())

# timpul GMT
gmt = time.gmtime()
print (gmt)
# GMT - per componente
print (gmt.tm_mday)
print (gmt.tm_mon)
print (gmt.tm_year)

print ("----------")
print ("----------")


#Importarea calendarului
import calendar

cal = calendar.Calendar()
tm = time.localtime()
all_dates = cal.monthdatescalendar(tm.tm_year, tm.tm_mon)
for week in all_dates:
    for day in week:
        print(day)
print ("----------")
print ("----------")

tm = time.localtime()
print(calendar.month(tm.tm_year, tm.tm_mon))

print ("----------")
print ("----------")

import datetime

now = datetime.datetime.now()
dt2 = datetime.datetime(2020, 11, 3)
dt3 = datetime.datetime.fromtimestamp(time.time())
print (now)
print (dt2)
print (dt3)

#Obiectului datetime i se poate schimba data prin adăugarea, adică scăderea unei anumite perioade.
#Aceasta se obţine, de asemenea, cu clasa timedelta.
p = datetime.timedelta(2,0,0,0,0,0,0)
the_day_after_tomorrow = now + p



#Obtinerea unui timedelta

print(the_day_after_tomorrow)
