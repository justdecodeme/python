# >>>>>>>>>>>>>>>>>
# >>> while loop
# >>>>>>>>>>>>>>>>>
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1))

# >>> break & continue
n = 7
while n > 0:
    n -= 1
    if n == 4:
        continue
    if n == 2:
        break
    print(n)
print('> Loop ended.')

# >>> The else Clause
# When < additional_statement(s) > are placed in an else clause, they will be executed
# only if the loop terminates “by exhaustion”—that is, if the loop iterates until the
# controlling condition becomes false. If the loop is exited by a break statement,
# the else clause won’t be executed.
n = 7
while n > 0:
    n -= 1
    print(n)
else:
    print('>> Loop done.')  # will get printed

n = 7
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('>>> Loop done.')  # will not printed


a = ['a', 'b', 'c']
while True:
    if not a:
        break
    print(a.pop(-1))

# >>> One-Line while Loops
n = 5
# while n > 0: n -= 1; print(n)

# >>>>>>>>>>>>>>>>>
# >>> for loop
# >>>>>>>>>>>>>>>>>
a = ['foo', 'bar', 'baz']
for i in {'foo': 1, 'bar': 2, 'baz': 3}:
    print(i)
# >>> iterable
# iter('foobar')                             # String
# iter(['foo', 'bar', 'baz'])                # List
# iter(('foo', 'bar', 'baz'))                # Tuple
# iter({'foo', 'bar', 'baz'})                # Set
# iter({'foo': 1, 'bar': 2, 'baz': 3})       # Dict

# >>> aren’t iterable
# iter(42)                                   # Integer
# iter(3.1)                                  # Float
# iter(len)                                  # Built-in function

# >>>>>>>>>>>>>>>>>
# >>> Iterators
# >>>>>>>>>>>>>>>>>
a = ['foo', 'bar', 'baz']

itr = iter(a)
print(itr)
print(next(itr))
print(next(itr))
print(next(itr))


# >>>>>>>>>>>>>>>>>
# >>> The Guts of the Python for Loop
# >>>>>>>>>>>>>>>>>
# Iteration:	The process of looping through the objects or items in a collection
# Iterable:	An object ( or the adjective used to describe an object) that can be iterated over
# Iterator:	The object that produces successive items or values from its associated iterable
# iter():	The built-in function used to obtain an iterator from an iterable
