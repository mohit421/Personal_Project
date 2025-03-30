# Lists
# Problem Link:- 

if __name__ == '__main__':
    N = int(input())
    # lst = ["insert","print","remove","append","sort","pop","reverse"]
    lst = []
    for _ in range(N):
        cmd = input().split()
        oper = cmd[0]
        if oper=="insert":
            lst.insert(int(cmd[1]),int(cmd[2]))
        elif oper =="print":
            print(lst)
        elif oper == "remove":
            lst.remove(int(cmd[1]))
        elif oper == "append":
            lst.append(int(cmd[1]))
        elif oper == "sort":
            lst.sort()
        elif oper == "pop":
            lst.pop() 
        elif oper == "reverse":
            lst.reverse()
    

# using getattr
'''
How getattr() Works?
getattr(lst, "append") → Equivalent to lst.append
map(int, args) → Converts input arguments to integers
*(map(int, args)) → Unpacks multiple arguments (e.g., for insert)
✅ Less repetitive & more Pythonic!

'''
if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        command, *args = input().split()
        if command == "print":
            print(lst)
        else:
            getattr(lst, command)(*(map(int, args)))



'''
 Approach 3: Using eval() (Shorter but Risky)
Using eval() makes the solution extremely concise but poses a security risk if untrusted input is used.

Why Use eval()?
Converts "lst.append(5)" into executable code dynamically.
Supports all commands without if-else checks.
⚠ Risk: eval() can execute harmful code if inputs are not trusted.
'''

if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        command = input()
        if command == "print":
            print(lst)
        else:
            eval(f"lst.{command}")


'''
🔹 Approach 4: Using Dictionary for Faster Lookup
Using a dictionary of function references allows efficient command execution.
'''

if __name__ == '__main__':
    N = int(input())
    lst = []

    operations = {
        "insert": lambda x, y: lst.insert(x, y),
        "print": lambda: print(lst),
        "remove": lambda x: lst.remove(x),
        "append": lambda x: lst.append(x),
        "sort": lambda: lst.sort(),
        "pop": lambda: lst.pop(),
        "reverse": lambda: lst.reverse(),
    }

    for _ in range(N):
        command, *args = input().split()
        operations[command](*map(int, args))
