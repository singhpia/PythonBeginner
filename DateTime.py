'''import time
import datetime
from datetime import datetime,timedelta

print(time.time())
print(time.thread_time())
print(time.clock())
print(time.localtime())
print(time.gmtime())
print(time.gmtime(time.time()))
print(time.strftime("%m : %d : %y"))

#creating date
a = datetime.date(1992,7,31)
print(a.year)
print(a.month)
print(a.day)

a = datetime.datetime(1991,7,31,1,4,22,12)
print(a.year)
print(a.date())
print(a.day)

# a.datetime.strptime("2001/07/31 04:11","%y/%d/%m %H:%M")

s = datetime.now()
print(s)

t = datetime.now() + timedelta(days=365, hours=4, minutes=6)
print(t)

for k in range(5):
    for l in range(k+1):
        print(l,end=" ")
    print("")'''
#
# from queue import PriorityQueue
#
# customers = PriorityQueue()
#
# customers.put((2, "Harry"))
#
# while customers:
#     print(customers.get())
import heapq

print(('   Geeks for Geeks   ').strip())
print(('   Geeks for Geeks   ').strip('Geeks   '))
print(('   Love o Love My   ').strip('   Love'))
print(("www.ghu.com").strip('.grow'))
print("tuck".replace("u","so"))
print("madagascar".replace("a","",1))

l = [3,3249,9]
a = heapq.heapify(l)
print(a)

u = {}
u['name'] = 'pia'
print(u)
u['profile'] = 'QA'
print(len(u))
print(u.keys())
print(u.values())
print(u['name'],"and",u['profile'])
print(sorted(u))

l = [434,35,12,24,6,314,0,43]
print(sorted(l))