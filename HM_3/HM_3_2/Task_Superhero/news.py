from heroes import Superman, SuperHero


class News:
    @staticmethod
    def create_news(sup: SuperHero, place):
        place_name = getattr(place, 'name', 'place')
        print(f'{sup.name} saved the {place_name}!')
