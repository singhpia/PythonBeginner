n=0
rows=5
for i in reversed(range(rows)):
       if(n==0):
              print(i*' '+'*')
              n=n+1
       elif i==0:
              print('*'+n*'*'+'*')
       else:
              print(i*' '+'*'+n*' '+'*')
              n=n+2
