from re import L


t = int(input())


for _ in range(t):
    input()
    board = []
    r = 1
    found = None
    f = False
    m = False
    for i in range(8):
        row = input()
        board.append(row)
        if f:
            found = row
            fr = i
            f = False
        elif ("#.#" in row) and not f and not m:
            f = True
            m = True
        r+=1

    found = list(found)
    c = found.index('#') + 1
    print(str(fr+1) + " " + str(c))
    
    