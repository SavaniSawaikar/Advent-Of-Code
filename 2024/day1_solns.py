def find_distances():
    dist = 0

    for i in range(len(num1)):
        dist += abs(num1[i] - num2[i])

    return dist

def similarities():
    ev = 0
    for val in num1:
        count = num2.count(val)
        ev += val * count

    return ev


if __name__ == "__main__":
    num1 = []
    num2 = []
    with open ("day1_input.txt") as f:
        for line in f:
            nums = line.split("   ")
            num1.append(int(nums[0]))
            num2.append(int(nums[1]))

    num1.sort()
    num2.sort()

    print(find_distances())
    print(similarities())