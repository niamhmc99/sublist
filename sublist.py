def check_lists(first_list, second_list):
    if first_list == second_list: 
        return EQUAL
    if contains(first_list, second_list):
        return SUPERLIST
    if contains(second_list, first_list):
        return SUBLIST
    return UNEQUAL

def SUBLIST(first_list, second_list):
    pass
    
def SUPERLIST(first_list, second_list):
    pass

def EQUAL(first_list, second_list):
    pass

def UNEQUAL(first_list, second_list):
    pass

def contains(l1, l2):
    if not l2:
        return True
    if len(l2) > len(l1):
        return False
    for i in range(len(l1) - len(l2) + 1):
        if l1[i] != l2[0]:
            continue
        for j in range(len(l2)):
            if l1[i + j] != l2[j]:
                break
        else:
            return True
    return False
