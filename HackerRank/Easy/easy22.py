def octal(num):
  o = 0
  i = 1
  lst = []
  while num!=0:
    o += (num % 8) * i
    num = int(num / 8)
    i *= 10
  return str(o)

def hexa(num):
  h = ""
  i = 1
  q = 0
  val = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
  lst = []
  while num != 0:
    q = int(num / 16)
    lst.append(num % 16)
    num = int(num / 16)
  if q > 0:
    h += val[q]
  for i in lst[::-1]:
    h += val[i]
  return h

def binary(num):
  b = 0
  i = 1
  lst = []
  while num!=0:
    b += (num % 2) * i
    num = int(num / 2)
    i *= 10
  return str(b)

def print_formatted(n):
    w = len(bin(n)[2:])
    for i in range(n):
        t = i + 1
        string = str(t).rjust(w) + " " + octal(t).rjust(w) + " " + hexa(t).rjust(w) + " " + binary(t).rjust(w)
        print(string)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)