exp = []
prime = 1234567891

N = int(input())
hashvalue = 0
for index, alphabet in enumerate(list(input())):
    hashvalue += (ord(alphabet) - 96) * 31**index
print(hashvalue % prime)
