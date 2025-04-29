# Problem link : https://www.geeksforgeeks.org/problems/if-loop-python/1?&selectedLang=python3

# Solution 1
def friends_in_trouble(j_angry, s_angry):
    if(j_angry == s_angry):
        return True
    else:
        return False
    
# solution 2
def in_trouble(j_angry, s_angry):
    if (j_angry and s_angry) or (not j_angry and not s_angry):
        return True
    else:
        return False
    
# solution 3
def in_trouble(j_angry, s_angry):
    return (j_angry and s_angry) or (not j_angry and not s_angry)


# solution 4
def in_trouble(j_angry, s_angry):
    return j_angry == s_angry

# Sloution 5 :Using XOR (!=) logic
def in_trouble(j_angry, s_angry):
    return not (j_angry != s_angry)

# solution 6 :  Using match-case
def in_trouble(j_angry, s_angry):
    match (j_angry, s_angry):
        case (True, True) | (False, False):
            return True
        case _:
            return False
