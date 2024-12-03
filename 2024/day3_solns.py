def get_mull_add():
    total = 0
    do = True
    for line in lines:
        elements = line.split(")")
        for val in elements:
            if "don't" in val:
                do = False
            elif "do" in val:
                do = True
            if "mul(" in val:
                vals = val.split("mul(")
                for val in vals:
                    nums = val.split(",")
                    if len(nums) == 2 and nums[0].isnumeric() and nums[1].isnumeric() and do:
                        total = total + (int(nums[0]) * int(nums[1]))
    return total

if __name__ == "__main__":
    path = "day3_input.txt"

    lines = []
    with open (path) as f:
        lines = f.readlines()

    print(get_mull_add())