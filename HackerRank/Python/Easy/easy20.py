def wrap(string, max_width):
    ind = 0
    str = ""
    for i in list(string):
        str += i
        ind += 1
        if ind % max_width == 0:
            str += "\n"
    return str


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
