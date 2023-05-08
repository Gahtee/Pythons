from time import sleep
n=1
while True:
    qd=0
    if n%2 == 0:
        n=n+1
    else:
        for i in range(n-1, 2, -1):
            if n%i == 0:
                qd=qd+1
        if qd == 0:
            print(n, 'é primo')
        n=n+1
