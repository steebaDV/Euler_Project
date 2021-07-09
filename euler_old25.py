def fibonachi(n):
    if n!=1 and n!=2:
        answer = fibonachi(n-1) + fibonachi(n-2)
        return answer
    else:
        return 1


i = 3
fibo = [1,1,2]
while True:
    i+=1
    fibo[1],fibo[2] = fibo[2],fibo[1]+fibo[2]
    if len(str(fibo[2])) == 1000:
        break
print(i)