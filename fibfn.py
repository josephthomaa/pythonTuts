def ask_ok(prompt, retries=3, reminder='Please try again!!'):
    while True:
        ok=input(prompt)
        if ok in('y','yes'):
            return True
        if ok in('n','no'):
            return False
        retries=retries-1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        input("Press Enter to continue...")    
def fib2(n):
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result
ask_ok('Do you really want to continue/quit?')    
num = int(input("Please enter an integer: "))
res=fib2(num)
print('Fibanacci series of ',num,'\n',res)    
input("Press Enter to continue...")