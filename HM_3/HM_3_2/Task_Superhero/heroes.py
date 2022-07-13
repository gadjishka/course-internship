from antagonistfinder import AntagonistFinder


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)


class Gun:
    @staticmethod
    def attack():
        print('PIU PIU')


class Lasers:
    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


class Kick:
    @staticmethod
    def roundhouse_kick():
        print('Bump')


class Superman(SuperHero, Lasers, Kick):

    def __init__(self):
        super(Superman, self).__init__('Superman', True)

    @staticmethod
    def attack():
        print('Kick')

    @staticmethod
    def ultimate():
        Lasers.incinerate_with_lasers()


class ChackNorris(SuperHero, Gun, Kick):
    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris', True)

    @staticmethod
    def ultimate():
        Kick.roundhouse_kick()
