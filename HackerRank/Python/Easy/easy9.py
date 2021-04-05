def finder(lst, score):
    s = []
    for i in lst:
        if i[1] == score:
            s.append(i[0])
    s.sort()
    for name in s:
        print(name)


if __name__ == '__main__':
    lst = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in scores:
            scores.append(score)
        lst.append([name, score])
        scores.sort()
    finder(lst, scores[1])
