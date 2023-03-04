hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

#total minutes
t= mins + dura

#total hours in duration, excess minutes removed
y = t//60

#reminder of minutesin duration
x = t%60

#sum of hours 
h = hour + y
#time correction for hours over the 24 integer mark
hz = h%24

m = x

print (hz,m, sep=":")