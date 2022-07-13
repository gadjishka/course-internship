from abc import ABC, abstractmethod


class Place(ABC):
    @staticmethod
    @abstractmethod
    def get_place():
        pass


class Kostroma(Place):
    name = 'Kostroma'

    @staticmethod
    def get_place():
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    @staticmethod
    def get_place():
        print('Godzilla stands near a skyscraper')
