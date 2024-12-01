class Q1:

    numbers = {
        "oneight" : '18',
        "threeight" : '38',
        "fiveight" : '58',
        "nineight" : '98',
        "sevenine" : '79',
        "eightwo" : '82',
        "eighthree" : '83',
        "twone" : '21',
        "one" : '1',
        "two" : '2',
        "three" : '3',
        "four" : '4',
        "five" : '5',
        "six" : '6',
        "seven" : '7',
        "eight" : '8',
        "nine" : '9'
    }

    def solution_part1(self):

        with open('input.txt',"r") as file:
            all_nums = []
            for line in file.readlines():
                nums = []
                for char in line:
                    if char.isnumeric():
                        nums.append(int(char))
                first_num = nums.pop(0)
                if len(nums) == 0:
                    second_num = first_num
                else:
                    second_num = nums.pop() 
                all_nums.append((10 * first_num) + second_num)
                nums = []
        
        return sum(all_nums)
    

    def solution_part2(self):
        
        all_nums = []
        with open ('input.txt', 'r') as file:
            for line in file.readlines():
                nums = []
                curr_line = line
                for word, value in self.numbers.items():
                    if word in curr_line:
                        curr_line = curr_line.replace(word, str(value))
                
                for char in curr_line:
                    if char.isdigit():
                        nums.append(int(char))
                first_num = nums[0]
                if len(nums) == 1:
                    second_num = first_num
                else:
                    second_num = nums[-1]
                all_nums.append((10 * first_num) + second_num)

        return sum(all_nums)  
        
    

print(Q1().solution_part2())
