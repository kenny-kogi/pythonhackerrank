ret_date = map(int, raw_input().strip().split(' '))
due_date = map(int, raw_input().strip().split(' '))

def myfunc(r, d):
    difs = [r[i]-d[i] for i in range(3)]
   
    if difs[2] > 0:
        return 10000
    elif difs[1] > 0 and difs[2] == 0:
        return 500*difs[1]
    elif difs[0] > 0 and difs[1] == 0:
        return 15* difs[0]
    else:
        return 0
             
print myfunc(ret_date, due_date)