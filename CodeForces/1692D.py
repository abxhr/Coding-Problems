def check_pal(s):
    return s == s[::-1]

def update_time(x, a):
    h,m = x.split(":")
    h = int(h)
    m = int(m)

    h = (h + ((m+a)//60))%24

    m = (m+a)%60

    s = str(h).zfill(2)+":"+str(m).zfill(2)

    return s

t = int(input())

for _ in range(t):
    s,x = input().split()
    x = int(x)

    ret_times = []
    pals = 0
    ret_times.append(s)
    if check_pal(s):
        pals += 1
    
    

    f = True
    while(f):
#        print(ret_times)
        temp_time = update_time(s,x)
#        print(temp_time)
        if temp_time in ret_times:
            f = False
            continue
        
        if check_pal(temp_time):
            pals += 1

        ret_times.append(temp_time)
        s= temp_time
    
    print(pals)