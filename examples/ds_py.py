from collections import deque

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


print('Python Data structures')
print('Lists')

cars=['i10','800','amaze','mustang gt','ikon']

print(cars)
print('Total Elements =',len(cars))

cars.append('jeep')
cars.insert(0,'g-wagon')

ask_ok('Do you really want to continue(y/n)..?')   

print('List after append',cars)
print('pop last elemnt ',cars.pop())
print('pop first elemnt ',cars.pop(0))
print('List after pop',cars)

ask_ok('Do you really want to continue(y/n)..?') 
cars.sort()  
print('List after sorting ',cars)
print("List as Queue...import deque from collections")


queue = deque(cars)
queue.append("jeep")
queue.append("g-wagon")
queue.popleft()
print(queue)
ask_ok('Do you really want to continue(y/n)..?') 
print(" list comprehension consists of brackets containing "
"an expression followed by a for clause, then zero or more for or if clauses")

squares = [x**2 for x in range(10)]
sets=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print('eg:squares = [x**2 for x in range(10)] \n',squares)
print('eg2: sets=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]',
sets)
del cars[:]
del squares[:]
del sets[:]
print('Deleted all lists')
ask_ok('Do you really want to continue(y/n)..?') 
print('Dictionary')
print('The dict() constructor builds dictionaries directly from sequences of key-value pairs:')

dic=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dic['test']=2000
print("Dictionary",dic)
input('Press any key to quit..')
