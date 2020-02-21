
def broken_eggs(floor,eggs):
    dropped = 0
    broken = 0
    for num in range(floor):
        eggs.append("broken")
    for egg in eggs:
        if egg == "broken":
            dropped += 1
        elif egg == "dropped":
            broken += 1
    # print(dropped,broken)
    num_floor = dropped - broken
    # print(num_floor)
    return num_floor


def dont_break_eggs(n,f=0):
    broken = 0
    dropped = 0
    eggs = []
    if n <= f:
        # print(eggs)
        eggs.append('dropped')
        for egg in eggs:
            if egg == "broken":
                dropped += 1
            elif egg == "dropped":
                broken += 1
            num_floor = broken- dropped
        print(num_floor)
        return num_floor
    else:  
        return dont_break_eggs(broken_eggs(n-1,eggs),f)
dont_break_eggs(10,1)