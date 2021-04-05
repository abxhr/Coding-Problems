if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        query = input().split()

        if query[0] == "insert":
            e = []
            pos = int(query[1])
            e.append(int(query[2]))
            lst = lst[:pos] + e + lst[pos:]
        elif query[0] == "print":
            print(lst)
        elif query[0] == "remove":
            lst.remove(int(query[1]))
        elif query[0] == "append":
            e = [int(query[1])]
            lst += e
        elif query[0] == "sort":
            lst.sort()
        elif query[0] == "pop":
            lst = lst[:len(lst)-1]
        elif query[0] == "reverse":
            lst = lst[::-1]
