str1 = input().lower()
str2 = input().lower()
f = 1
for i in range(len(str1)):
  a = ord(str1[i])
  b = ord(str2[i])
  if a != b:
    f = 0
    if (a > b):
      print(1)
    else:
      print(-1)
    break
if f:
  print(0)