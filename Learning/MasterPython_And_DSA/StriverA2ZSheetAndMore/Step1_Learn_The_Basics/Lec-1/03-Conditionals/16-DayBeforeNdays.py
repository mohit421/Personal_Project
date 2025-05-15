# Problem Link:-https://www.geeksforgeeks.org/problems/days-before-n-days--150030/1?&selectedLang=python3


# Solution 1
#User function Template for python3
d = int(input())
n = int(input())


match ((d-n)%7):
    case 0:
        # print("Sunday")
        print(0)
    case 1:
        # print("Monday")
        print(1)
    case 2:
        # print("Tuesday")
         print(2)
    case 3:
        # print("Wednesday")
         print(3)
    case 4:
        # print("Thursday")
         print(4)
    case 5:
        # print("Friday")
         print(5)
    case 6:
        # print("Saturday")
         print(6)
    case _:
        print("Invalid")


# soluton 2 if want o print days aswell

def get_day_name(index):
    match index:
        case 0: return "Sunday"
        case 1: return "Monday"
        case 2: return "Tuesday"
        case 3: return "Wednesday"
        case 4: return "Thursday"
        case 5: return "Friday"
        case 6: return "Saturday"
        case _: return "Invalid"
    
def previous_day_with_name(d, n):
    day_index = (d - n) % 7
    return day_index, get_day_name(day_index)
idx, name = previous_day_with_name(4, 3)
print(idx, name)  # ➜ 1 Monday

idx, name = previous_day_with_name(2, 19)
print(idx, name)  # ➜ 4 Thursday

# Solution 3

def previous_day(d, n):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return (d - n) % 7, days[(d - n) % 7]

# Solution 4 Using dictionary

def previous_day(d, n):
    day_map = {
        0: "Sunday", 1: "Monday", 2: "Tuesday",
        3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"
    }
    idx = (d - n) % 7
    return idx, day_map[idx]

# Solution 5   Object-Oriented Approach (Using Class)

class WeekDay:
    def __init__(self):
        self.days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def previous_day(self, d, n):
        idx = (d - n) % 7
        return idx, self.days[idx]

# Example usage
wd = WeekDay()
print(wd.previous_day(2, 19))  # ➜ (4, 'Thursday')
