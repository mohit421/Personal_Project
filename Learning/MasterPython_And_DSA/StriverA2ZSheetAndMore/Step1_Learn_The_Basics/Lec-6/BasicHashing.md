# Hashing

    - It is something like pre-stroing and fetching
    - Pre store something and fetch when required

##### Examples:-

    - arr[] = [1,2,3,4,5,1,2,3,2,1,4]
    - how many time each digit appears in array
    - 1 appears 3 times
    - 2 appears 3 times
    - 3 appears 2 times
    - 4 appears 2 times
    - 5 appears 1 times

- First approach that comes us to our mind is , we will iterate to our entire array
- Take each digits and compare with all array element
- for code check 1-HashingTheory.py file

#### Hashing ways

    arr[] = {1,2,1,3,2}
    - An array have at max have number till 12 or 15. Let's say 12
    - Atmax it will have 12, what does it mean over here you're seeing at max is 3
    - SO what hashing does is :- We create another array and call this as hashArr and indexing will go from  0,1,2,3....12
    hashArr[] = {0,0,0,0,0,0,0,0,0,0,0,0}
    - We will do pre-calculation
        - We will say can you just remember that I have one one so he will say Okay, I'll remember we have one next
        - then go to 2 and say we have 1 times 2 we will remember
        - then goes to 1 again and incre 1 to 2 so 2 times 1 and say remember 2 times 1 next time
        - Similary for 3 :- 1 times 3
        - next for 2 again :- 2times 2
        - hashArr[1] :- 2
        - hashArr[2] :- 2
        - hashArr[3] :- 1
    - For code check 1-HashingTheory.py

- If array has max element till 10^9, Can we declare an array of size 10^9 + 1
  - No, we can't , bcuz maximum array size that we can declare is 10^6 if it is of integer inside main
    - arr[10^6] => inside main
      - if we declare more than 10^6 then it will throw segmentation fault
    - If we declare array Globally then we can declare array til 10^7 or 10^7 + 1

#### For int

    - arr[10^6] :- If declared inside main
    - arr[10^7] :- if declared globally

#### For boolean

    - arr[10^7] :- If declared inside main
    - arr[10^8] :- if declared globally

| Concept           | C++ STL         | Java Collections | Python Equivalent              |
| ----------------- | --------------- | ---------------- | ------------------------------ |
| Hash map          | `unordered_map` | `HashMap`        | `dict` / `collections.Counter` |
| Hash set          | `unordered_set` | `HashSet`        | `set`                          |
| Frequency counter | Manual map      | `Map` with loop  | `collections.Counter`          |
