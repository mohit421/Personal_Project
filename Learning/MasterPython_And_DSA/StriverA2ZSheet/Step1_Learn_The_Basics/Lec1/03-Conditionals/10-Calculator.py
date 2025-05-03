# Problem link:-

# Solution 1

a,b  = int(input()), int(input())
operator = int(input())

match operator:
    case 1:
        print(a+b)
    case 2:
        print(b-a)
    case 3:
        print(a*b)
    case _:
        print("Invalid input")