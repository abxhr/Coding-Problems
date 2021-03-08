if __name__ == '__main__':
    s = input()
    dict = {"alnum": False, "alpha": False, "digit": False, "lower": False, "upper": False}
    for i in s:
        if (i.isalnum()):
            dict["alnum"] = True
        if (i.isalpha()):
            dict["alpha"] = True
        if (i.isdigit()):
            dict["digit"] = True
        if (i.islower()):
            dict["lower"] = True
        if (i.isupper()):
            dict["upper"] = True
    for i in dict.values():
        print(i)