class Critter(object):
    '''pitomec'''
    total = 0
    @staticmethod
    def status():
        print('vsego zverey: ', Critter.total)
    def __init__(self, name):
        self.name = name
        print('new zver!', self.name)
        Critter.total += 1
    def __str__(self):
        rep = 'object of class Critter \n'
        rep += 'neme: ' + self.name
        return rep
    def talk(self):
        print('hello. my name is ', self.name)

crit = Critter('bobik')
crit.talk()

crit2 = Critter('persik')
crit2.talk()

Critter.status()
print('vsego zverey (object): ', crit.total)

print('1st crit name is ', crit.name)
print(crit)
input()
