def check_safety(levels):
    
    sign = None
    
    for i in range(len(levels)):
        if i + 1 < len(levels):
            curr = int(levels[i])
            next = int(levels[i + 1])
            if curr == next:
                return False
            elif curr < next and sign == -1:
                return False
            elif curr > next and sign == 1:
                return False
            elif abs(curr - next) > 3:
                return False
            elif curr < next and sign is None:
                sign = 1
            elif curr > next and sign is None:
                sign = -1

    return True

def num_safe():
    count = 0
    for report in reports:
        levels = report.split(" ")
        safe = check_safety(levels)
        if safe:
            count += 1
        else:
            for i in range(len(levels)):
                safe2 = check_safety(levels[:i] + levels[i + 1:])
                if safe2:
                    count += 1
                    break


    return count
    


if __name__ == "__main__":
    path = "day2_input.txt"

    reports = []
    
    with open (path) as f:
        reports = f.readlines()

    print(num_safe())

    
