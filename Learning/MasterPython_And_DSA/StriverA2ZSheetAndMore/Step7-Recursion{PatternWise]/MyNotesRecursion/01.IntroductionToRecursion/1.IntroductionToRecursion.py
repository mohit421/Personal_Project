

# 
cnt = 0

def print_cnt():
    global cnt
    if cnt == 3:
        return
    print(cnt)
    cnt += 1
    print_cnt()

def main():
    print_cnt()

if __name__ == "__main__":
    main()

