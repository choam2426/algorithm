a=int(input())
number=list(map(int,input().split()))
count=0
for i in number:
    if i >1:
        no=0
        for j in range(2,i):
            if i%j==0:
                no+=1
        if no==0:
            count+=1

print(count)