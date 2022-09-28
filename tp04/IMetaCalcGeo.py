from abc import ABCMeta, abstractmethod


class IMetaCalcGeo(metaclass=ABCMeta):

    @abstractmethod
    def get_surface(self):
        pass


    def hello(self):
        print("hello")