from timeit import default_timer as timer

my_string= "Hello"
print(my_string)

my_string= 'Hello'
print(my_string)

my_string= 'I\'m programmer'
print(my_string)

my_string= """Hello
World"""
print(my_string)

my_string= """Hello \
World"""
print(my_string)

my_string= 'Hello'
char = my_string[0] 
print(char)
char = my_string[-1]
print(char)

#my_string[0] = 'h' #error

substring = my_string[1:4] #my_string[::-1] # reverse the string 
print(substring)

greeting="Hello"
name='Tom'
sentence= greeting + " " + name
print(sentence)

for i in greeting:
    print(i)

if 'el' in greeting:
    print('Yes')
else: 
    print('No')

my_string = '   Hello World   '
my_string = my_string.strip() #only my_string.strip() does not work because strings are immutable
print(my_string)

print(my_string.upper())
print(my_string.lower())

print(my_string.startswith('H'))
print(my_string.endswith('World'))

print(my_string.find('o'))
print(my_string.count('o'))

print(my_string.replace('World', 'Universe'))

my_list = my_string.split()
my_list = ''.join(my_list)
print(my_list)

my_list = ['a'] * 30
print(my_list)

#bad 
my_string = ''
start = timer()
for i in my_list:
    my_string += i # high cost
stop = timer()
print(stop - start)
print(my_string)

#good 
start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)
print(my_string)

var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 3.213124325
my_string = "the variable is %.2f" % var
print(my_string)

var = 4.56457
var2 = "sad"
my_string = "the variable is {:.2f} and {}".format(var, var2)
print(my_string)

var = 4.56457
var2 = "sad"
my_string = f"the variable is {var:.2f} and {var2}"
print(my_string)