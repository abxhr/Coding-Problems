m_n = list(map(int, input().split()))      # m_n[0] = N    m_n[1] = M
f = 1
str1 = "."
str2 = "."
for i in range(m_n[0]):
  if (i != int(m_n[0]/2)):
    print(str1.rjust(int(m_n[1]/2), '-') + "|" + str2.ljust(int(m_n[1]/2), '-'))
    if f:
      str1 += "|.."
      str2 = "..|" + str2
    else:
      str1 = str1[:-3]
      str2 = str2[3:]
  if (i == int(m_n[0]/2)):
    print("WELCOME".center(m_n[1], '-'))
    f = 0
    str1 = str1[:-3]
    str2 = str2[3:]