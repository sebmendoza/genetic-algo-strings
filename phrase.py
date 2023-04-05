import random

target = "Wow finals szn is coming up soon!"


class Phrase:
    def __init__(self):
        self.characters = []  # use a list bc lists are mutable, strings are not
        for i in range(len(target)):
            # create chr() turns integer to a unicode character
            # 31 - 127 are the unicode codes we want to usehttps://en.wikipedia.org/wiki/List_of_Unicode_characters
            # range between 32 to 127-1
            character = chr(random.choice(range(32, 127)))
            self.characters.append(character)

    def get_contents(self):
        return ''.join(self.characters)

    # this does not return a value, it sets a value
    def get_fitness(self):
        self.fitness = 0
        for i in range(len(self.characters)):
            if self.characters[i] == target[i]:
                self.fitness += 1

    # method to cross-breed with a partner, randomly selects between mother and father's genes,
    # more fine tuning could improve
    # possiblity to make a child class that extends Phrase
    def crossover(self, partner):
        child = Phrase()
        for i in range(len(self.characters)):
            if random.random() < 0.5:
                child.characters[i] = self.characters[i]
            else:
                child.characters[i] = partner.characters[i]

        return child

    # this mutation rate is what real algorithms would fine tune
    # you might want to change this over time
    # will I get stuck in a local minima?
    # https://stackoverflow.com/questions/31215003/genetic-algorithm-selection-method-stuck-at-local-minimum-after-few-generations

    def mutate(self):
        for i in range(len(self.characters)):
            if random.random() < 0.005:
                self.characters[i] = chr(random.choice(range(32, 127)))
