from pyknow import *


class Characteristics(Fact):
    """ Dac diem nhan dang dong vat """
    pass


class Animals(KnowledgeEngine):
    """ Cac luat """
    characteristics = Fact(
        hair=1, feathers=2, eggs=3, airborne=4, domestic=5, predator=6,
        toothed=7, fins=8, legs=9, legs2=10, legs4=11, legs6=12, legs8=13, tail=14
    )
    """ hair -> |feathers, |airborne, legs4, |airborne, |fins"""
    @Rule(Characteristics(hair = 1))
    def _hair(self):
        Characteristics(feathers = 0, airbone = 0, legs = 4, airborne = 0, fins = 0)

    """ hair ^ eggs -> platypus (end)
        hair ^ |toothed -> platypus (end)
    """
    @Rule(Characteristics(hair = 1, eggs = 1, toothed = 0))
    def platypus(self):
        print("This animal is platypus!")
        quit()

    """ hair ^ |tail -> bear (end)"""
    @Rule(Characteristics(hair = 1, tail = 0))
    def bear(self):
        print("This animal is bear!")
        quit()

    """ feathers -> eggs, legs2, tail"""
    @Rule(Characteristics(feathers = 1))
    def _feathers(self):
        Characteristics(eggs = 1, legs = 2, tail = 1)

    """ |feathers ^ airborne -> ladybird(end)"""
    @Rule(Characteristics(feathers = 0, airborne = 1))
    def ladybird(self):
        print("This animal is ladybird!")
        quit()

    """ airborne ^ domestic -> duck (end)"""
    @Rule(Characteristics(airborne = 1, domestic = 1))
    def duck(self):
        print("This animal is duck!")
        quit()

    """ fins ^ eggs -> carp (end)"""
    @Rule(Characteristics(fins = 1, eggs = 1))
    def carp(self):
        print("This animal is Carp!")
        quit()

    """ fins ^ |eggs -> dolphin (end)"""
    @Rule(Characteristics(fins = 1,eggs = 0))
    def dolphin(self):
        print("This animal is Dolphin!")
        quit()

    """ airborne ^ |domestic -> crow(end)"""
    @Rule(Characteristics(airborne = 1, domestic = 0))
    def chicken(self):
        print("This animal is Crow!")
        quit()

    """ domestic ^ |airborne -> penguin (end)"""
    @Rule(Characteristics(domestic = 1, airborne = 0))
    def penguin(self):
        print("This animal is Penguin!")
        quit()

    """ feathers ^ |airborne ^ |domestic -> ostrich (end)"""
    @Rule(Characteristics(feathers = 1, airborne = 0, domestic = 0))
    def ostrich(self):
        print("This animal is Ostrich!")
        quit()

    """ legs8 -> crab, octopus (end)"""
    @Rule(Characteristics(legs = 8))
    def crab(self):
        print("This animals are Crab or Octopus!")
        quit()

    """ legs6 ^ |airborne -> lobster (end)"""
    @Rule(Characteristics(legs = 6, airborne = 0))
    def lobster(self):
        print("This animal is Lobster!")
        quit()

    """ hair ^ legs4 ^ tail ^ |predator -> elephant"""

    @Rule(Characteristics(tail=1, hair=1, legs=4, predator=0))
    def elephant(self):
        print("This animal is Elephant!")
        quit()

    """ tail ^ |feathers ^ legs4 -> turtle (end)"""
    @Rule(Characteristics(tail=1, feathers=0, legs=4 , hair =0))
    def turtle(self):
        print("This animal is Turtle!")
        quit()

    """ |feathers ^ |tail ^ legs4 -> frog (end)"""

    @Rule(Characteristics(tail=0, feathers=0, legs=4))
    def frog(self):
        print("This animal is Frog!")
        quit()




engine = Animals()
engine.reset()  # Prepare the engine for the execution.
engine.declare(Characteristics(hair=1, tail=1, toothed=0, predator=1, legs = 4, feathers = 0,
                               airborne = 1, eggs = 0, domestic = 0))
engine.run()  # Run it!