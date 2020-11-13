def finder(s_m, name):
    scores = [i for n, sm in s_m.items() if n==name for i in sm]
    print("%.2f" % (sum(scores)/len(scores)))
    

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    finder(student_marks, query_name)