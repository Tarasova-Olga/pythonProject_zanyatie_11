class CardDeck:
    def __init__(self):
        self.length = 52
        self.index = 0
        self.masty = ['Пик', 'Бубей', 'Червей', 'Крестей']
        self.rang = [*range(2, 11), 'J', 'Q', 'K', 'A']            # *args - кортеж

    def __len__(self):
        return self.length

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration                                     # вызов исключения, принт здесь не сработает
        else:
            suit = self.masty[self.index // len(self.rang)]         # масти [0] -> пик 0-12/13 (13 рангов) = 0
                                                                    # масти [1] -> бубей 13-25/13 (13 рангов) = 1
                                                                    # целочисл деление
            rank = self.rang[self.index % len(self.rang)]           # 0 % 13 = 0, 1 % 13 = 1 ...
            self.index += 1
            return f'{rank} {suit}'                                 # вызов принта в ф-ции

    def __iter__(self):
        return self

deck = CardDeck()
while True:
    print(next(deck))

