from pyknow import *
################ Tung dac diem la 1 su that rieng

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
        Characteristics(feathers = 0)
        Characteristics(airbone = 0)
        Characteristics(legs = 4)
        Characteristics(airborne = 0)
        Characteristics(fins = 0)

    """ hair ^ eggs -> platypus (end)
        hair ^ |toothed -> platypus (end)
    """
    @Rule(AND(
        Characteristics(hair = 1),
        OR(
            Characteristics(eggs = 1),
            Characteristics(toothed = 0)
        )
    ))
    def platypus(self):
        print("This animal is platypus!")
        quit()

    """ hair ^ |tail -> bear (end)"""
    @Rule(AND(
        Characteristics(hair = 1),
        Characteristics(tail = 0))
    )
    def bear(self):
        print("This animal is bear!")
        quit()

    """ feathers -> eggs, legs2, tail"""
    @Rule(Characteristics(feathers = 1))
    def _feathers(self):
        Characteristics(eggs = 1),
        Characteristics(legs = 2)
        Characteristics(tail = 1)

    """ |feathers ^ airborne -> ladybird(end)"""
    @Rule(AND(
        Characteristics(feathers = 0),
        Characteristics(airborne = 1)
    ))
    def ladybird(self):
        print("This animal is ladybird!")
        quit()

    """ airborne ^ domestic -> duck (end)"""
    @Rule(AND(
        Characteristics(airborne = 1),
        Characteristics(domestic = 1)
    ))
    def duck(self):
        print("This animal is duck!")
        quit()

    """ fins ^ eggs -> carp (end)"""
    @Rule(AND(
        Characteristics(fins = 1),
        Characteristics(eggs = 1)
    ))
    def carp(self):
        print("This animal is Carp!")
        quit()

    """ fins ^ |eggs -> dolphin (end)"""
    @Rule(AND(
        Characteristics(fins = 1),
        Characteristics(eggs = 0)
    ))
    def dolphin(self):
        print("This animal is Dolphin!")
        quit()

    """ airborne ^ |domestic -> chicken, crow, dove (end)"""
    @Rule(AND(
        Characteristics(airborne = 1),
        Characteristics(domestic = 0)
    ))
    def chicken(self):
        print("This animals are Chicken, Crow or Dove!")
        quit()

    """ domestic ^ |airborne -> penguin (end)"""
    @Rule(AND(
        Characteristics(domestic = 1),
        Characteristics(airborne = 0)
    ))
    def penguin(self):
        print("This animal is Penguin!")
        quit()

    """ feathers ^ |airborne ^ |domestic -> ostrich (end)"""
    @Rule(AND(
        Characteristics(feathers = 1),
        AND(
            Characteristics(airborne = 0),
            Characteristics(domestic = 0)
        )
    ))
    def ostrich(self):
        print("This animal is Ostrich!")
        quit()

    """ legs8 -> crab, octopus (end)"""
    @Rule(Characteristics(legs = 8))
    def crab(self):
        print("This animals are Crab or Octopus!")
        quit()

    """ legs6 ^ |airborne -> lobster (end)"""
    @Rule(AND(
        Characteristics(legs = 6),
        Characteristics(airborne = 0)
    ))
    def lobster(self):
        print("This animal is Lobster!")
        quit()

    """ hair ^ legs4 ^ tail ^ |predator -> elephant"""

    @Rule(AND(
        Characteristics(tail=1),
        Characteristics(hair=1),
        Characteristics(legs=4),
        Characteristics(predator=0)
    ))
    def elephant(self):
        print("This animal is Elephant!")
        quit()

    """ tail ^ |feathers ^ legs4 -> turtle (end)"""
    @Rule(AND(
        Characteristics(tail = 1),
        Characteristics(feathers =0),
        Characteristics(legs = 4)
    ))
    def turtle(self):
        print("This animal is Turtle!")
        quit()

    """ |feathers ^ |tail ^ legs4 -> frog (end)"""

    @Rule(AND(
        Characteristics(tail=0),
        Characteristics(feathers=0),
        Characteristics(legs=4)
    ))
    def frog(self):
        print("This animal is Frog!")
        quit()




engine = Animals()
engine.reset()  # Prepare the engine for the execution.
engine.declare(Characteristics(hair=1, tail=1, toothed=1, predator=0, legs = 4, feathers = 0,
                               airborne = 0))
engine.run()  # Run it!