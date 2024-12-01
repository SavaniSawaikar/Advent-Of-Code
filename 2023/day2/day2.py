class Game:
    def __init__(self, num_blue, num_red, num_green, power=0):
        self.num_blue = num_blue
        self.num_red = num_red
        self.num_green = num_green
        self.power = power


class Solution:

    games = {}
    games2 = {}

    def part1(self):
        ids = []

        with open ('input.txt', 'r') as file:
            for line in file.readlines():
                game = line.split(':')
                id = self.get_id(game[0])

                sets = game[1].split(';')
                current_game = Game(0, 0, 0)
                for set in sets:
                    colours = set.split(',')
                    for colour in colours:
                        number = self.find_num(colour)
                        if "red" in colour:
                            if number > current_game.num_red:
                                current_game.num_red = number
                        elif "green" in colour:
                            if number > current_game.num_green:
                                current_game.num_green = number
                        elif "blue" in colour:
                            if number > current_game.num_blue:
                                current_game.num_blue = number

                self.games[id] = current_game


        for num_game, score in self.games.items():
            if score.num_red <= 12 and score.num_blue <= 14 and score.num_green <= 13:
                ids.append(num_game)

        return sum(ids)


    def get_id(self, string):
        id = ""
        for char in string:
            if char.isdigit():
                id += char
        return int(id)


    def find_num(self, string):
        return self.get_id(string)
    
    def part2(self):
        powers = []

        with open ('input.txt', 'r') as file:
            for line in file.readlines():
                game = line.split(':')
                id = self.get_id(game[0])

                sets = game[1].split(';')
                current_game = Game(0, 0, 0, 0)
                for set in sets:
                    colours = set.split(',')
                    for colour in colours:
                        number = self.find_num(colour)
                        if "red" in colour:
                            if number > current_game.num_red:
                                current_game.num_red = number
                        elif "green" in colour:
                            if number > current_game.num_green:
                                current_game.num_green = number
                        elif "blue" in colour:
                            if number > current_game.num_blue:
                                current_game.num_blue = number

                self.games2[id] = current_game


        for score in self.games2.values():
            score.power = score.num_red * score.num_blue * score.num_green
            powers.append(score.power)

        print(powers)
        return sum(powers)


print(Solution().part2())