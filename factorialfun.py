import sys

def factorial(n):
    factor=1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            factor=factor*i
        return factor
    
if __name__=='__main__':
  nums=sys.argv[1:]
  print('computing the factorial of',nums)
  for num in nums:
      num=int(num)
      result=factorial(num)
      print('The factirial of {} is {}'.format(num,result))