class day3:

    def get_num(self):
        nums = []
        with open ("input.txt", 'r') as file:
            for line in file.readlines():
                for i in range(len(line)):
                    