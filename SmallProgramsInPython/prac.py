n=1
for s in reversed(range(6)):
    a=' '
    if s==5:
        print(a*s+n*'*')
    n=n+1
    elif s==0:
        print('*'*n)
    else:
        print(a*s+'*'+' '*n+'*')
    
    
