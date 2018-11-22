from pyknow import *

class Characteristics(Fact):
    """ Dac diem nhan dang dong vat """
    pass

class Animals(KnowledgeEngine):
    """ Cac luat """
    characteristics = Fact(
        hair = 1, feathers = 2, eggs = 3, airborne = 4, domestic =5, predator = 6,
        toothed = 7, fins = 8, legs = 9, legs2 = 10, legs4 = 11, legs6 = 12, legs8 = 13, tail = 14
        )

    """ hair ^ |toothed = platypus """
    @Rule(AND(
            Characteristics(hair = 1),
            Characteristics(toothed = 0)
    ),salience=10)
    def platypus(self):
        print("This animal is platypus!")
        quit()

    """ hair ^ |tail = bear """
    @Rule(AND(
            Characteristics(hair = 1),
            Characteristics(tail = 0)
    ))
    def bear(self):
        print("This animal is bear!")
        quit()

    """ hair ^ tail = func_predator() """
    @Rule(AND(
            Characteristics(hair = 1),
            Characteristics(tail = 1)
    ))

    @Rule(Characteristics(predator = 1),salience=0)
    def func_predator(self):
        print("This animal is Lion, Leopad or Wolf!")
        quit()


        

engine = Animals()
engine.reset()  # Prepare the engine for the execution.
engine.declare(Characteristics(hair = 1, tail = 1, toothed = 1, predator = 0))
engine.run()  # Run it!