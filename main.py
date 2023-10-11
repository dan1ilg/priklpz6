def putin(N):
    if N<=1:
        return 1
    d=[0]*(N+1)
    d[1]=1
    for i in range(2,N+1):
        d[i]+=d[i-1]
        d[i]+=d[i-3]
        if i%2==0:
            d[i]+=d[i//2]
    return d[N]
N = int(input(('Введите значение N: ')))
result = putin(N)
print(f'Кол-во способов достичь {N} из точки 1: {result}')