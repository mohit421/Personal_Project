'''

F 
E F
D E F
C D E F
B C D E F
A B C D E F
'''



def print1(n):
    ch = chr(ord('A') + n-1)
    for i in range(n):
        start = ord(ch) - i
        end = ord(ch)
        for j in range(start,end + 1):
            print(chr(j),end=' ')
            # ch = chr(ord(ch) + 1);
        print()  # New line after each row

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        n = int(input("Enter n: "))
        print1(n)
