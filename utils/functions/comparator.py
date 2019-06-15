from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return str(self.name) + ' ' + str(self.score)

    def comparator(a, b):

        def cmp(a, b):
            return (a > b) - (a < b)

        if a.score != b.score:
            return cmp(a.score, b.score) * -1
        else:
            return cmp(a.name, b.name)


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i)