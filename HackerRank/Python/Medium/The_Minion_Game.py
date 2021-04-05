def minion_game(string):
    kp = 0
    sp = 0
    vowels = "AEIOU"
    for i in range(len(string)):
        if string[i] in vowels:
            kp += len(string) - i
        else:
            sp += len(string) - i
    if kp > sp:
        print("Kevin " + str(kp))
    elif sp > kp:
        print("Stuart " + str(sp))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
