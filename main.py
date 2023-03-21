import random
import threading
import queue
import time
from datetime import datetime
from Classes import wish, time_machine


request_history=[]
flag=1

def request (q):
    r = wish()
    global flag
    while(flag==1):
        who = r.subject()
        where = r.place(who)
        when = r.time(who, where)
        new_item=[who,where,when,datetime.now().strftime('%H:%M:%S')]
        global request_history
        request_history+=[new_item]
        q.put(new_item)
        time.sleep(random.randint(2,5))

def answer(q):
    a = time_machine()
    while(True):
        request=q.get()
        a.sending(request)


q=queue.Queue()
thr1=threading.Thread(target=request, args=(q,), daemon=True)
thr1.start()
thr2 = threading.Thread(target=answer, args=(q,), daemon=True)
thr2.start()
time.sleep(30)
flag=0
while(True):
    if not thr1.is_alive():
        break

print("\nThe requests history:")
for i in range(len(request_history)):
    if request_history[i][2]>=0:
        print(f"{i+1}. A {request_history[i][0]} was sent to {request_history[i][1]} {request_history[i][2]} days forward at {request_history[i][3]}")
    else:
        print(f"{i+1}. A {request_history[i][0]} was sent to {request_history[i][1]} {-request_history[i][2]} days ago at {request_history[i][3]}")
