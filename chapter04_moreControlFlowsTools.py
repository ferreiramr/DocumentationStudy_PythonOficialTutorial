## MORE CONTROL FLOW TOOLS

#%%
x = int(input("Please enter an integer: "))
# %%
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
# %%
## for Statements
# %%
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
# %%
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive'}
# Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
# %%
## The range() Function
# %%
for i in range(5):
    print(i)
# %%
list(range(5, 10))
# %%
list(range(0, 10, 3))
# %%
list(range(-10, -100, -30))
# %%
a = ['Mary', 'had', 'a', 'little', 'lamb']
# %%
for i in range(len(a)):
    print(i, a[i])
# %%
range(10)
# %%
sum(range(4)) # 0 + 1 + 2 + 3
# %%
##### break and continue Statements, and else Clauses on Loops
# %%
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
# %%
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# %%
##### pass Statements
# %%
while True:
    pass # Busy-wait for keyboard interrupt (Ctrl+C)
# %%
class MyEmptyClass:
    pass
# %%
def initlog(*args):
    pass # Remember to implement this!
# %%
##### match Statements
# %%
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"
# %%
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
# %%
