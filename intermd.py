import os
names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    statement = ' '.join(['Hello there', name])
    print(statement)


count = 1
docname = ''.join(['doc',str(count)])
print(docname)
#os.path.join to join filepaths
location_of_files = 'Matplotlib/data/'
file_name = 'example.txt'

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())

# {} and format
who = 'Gary'
how_many = 12

print('{} bought {} apples today!'.format(who, how_many))    