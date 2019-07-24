def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok('Do you really want to quit?')
num = int(input("Please enter an integer: "))
for n in range(2,num):
    for x in range(2,n):
        if n%x==0:
            print(n,'eqauls',x,'*',n//x)
            break
    else:
        print(n,'is a prime number')        

