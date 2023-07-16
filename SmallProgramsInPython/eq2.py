rows = 5
n=0
for s in reversed(range(rows)):
       if n==0:
              print(s*' '+'*')
              n=n+1
       elif s==0:
              print('*'+n*'*'+'*')
       else:
              print(s*' '+'*'+n*' '+'*')       
              n=n+2
       
