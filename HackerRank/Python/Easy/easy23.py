def print_rangoli(size):
    letters = "abcdefghijklmnopqrstuvwxyz"
    total = (2 * n) -1
    w = (4 * n) - 3
    lst = []
    for i in range(total):
        str = "-".join(letters[i:n])
        str = (str[::-1] + str[1::]).center(w, '-')
        lst.append(str)
    for i in lst[int(total/2)::-1]:
        print(i)
    for i in lst[1:int(total/2)+1]:
        print(i)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)