from pyknow import *
import file_dict as f

class Characteristics(Fact):
    """ Dac diem nhan dang dong vat """
    pass

class Diagnosis_animals(KnowledgeEngine):
    N = 20
    M = 10
    # print(bear)
    @Rule(Characteristics(name = 'platypus'))
    def platypus(self):
        print('platypus')
        # quit()

    @Rule(AND(Characteristics(hair=1),
              Characteristics(toothed=0),
              Characteristics(backbone=1),
              Characteristics(tail=1),
              Characteristics(eggs=1),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=1),
              Characteristics(fins=0),
              Characteristics(legs=4),
              Characteristics(predator=1)),salience=N)
    def _platypus(self):
        self.declare(Characteristics(name='platypus'))

    #######################################################
    @Rule(Characteristics(name='bear'))
    def bear(self):
        print('bear')
        # quit()

    @Rule(AND(Characteristics(hair=1),
              Characteristics(toothed=1),
              Characteristics(backbone=1),
              Characteristics(tail=0),
              Characteristics(eggs=0),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=0),
              Characteristics(fins=0),
              Characteristics(legs=4),
              Characteristics(predator=1)),salience=N)
    def _bear(self):
        self.declare(Characteristics(name='bear'))

    #######################################################
    @Rule(Characteristics(name = 'leopard'))
    def leopard(self):
        print('leopard')
        # quit()

    @Rule(AND(Characteristics(hair=1),
              Characteristics(toothed=1),
              Characteristics(backbone=1),
              Characteristics(tail=1),
              Characteristics(eggs=0),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=0),
              Characteristics(fins=0),
              Characteristics(legs=4),
              Characteristics(predator=1)),salience=N)
    def _leopard(self):
        self.declare(Characteristics(name='leopard'))

    #######################################################
    @Rule(Characteristics(name = 'gorilla'))
    def gorilla(self):
        print('gorilla')
        # quit()

    @Rule(AND(Characteristics(hair=1),
              Characteristics(toothed=1),
              Characteristics(backbone=1),
              Characteristics(tail=0),
              Characteristics(eggs=0),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=0),
              Characteristics(fins=0),
              Characteristics(legs=2),
              Characteristics(predator=0)),salience=N)
    def _gorilla(self):
        self.declare(Characteristics(name='gorilla'))

    #######################################################
    @Rule(Characteristics(name = 'elephant'))
    def elephant(self):
        print('elephant')
        # quit()

    @Rule(AND(Characteristics(hair=1),
              Characteristics(toothed=1),
              Characteristics(backbone=1),
              Characteristics(tail=1),
              Characteristics(eggs=0),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=0),
              Characteristics(fins=0),
              Characteristics(legs=4),
              Characteristics(predator=0)),salience=N)
    def _elephant(self):
        self.declare(Characteristics(name='elephant'))

    #######################################################
    @Rule(Characteristics(name = 'dolphin'))
    def dolphin(self):
        print('dolphin')
        # quit()

    @Rule(AND(Characteristics(hair=0),
              Characteristics(toothed=1),
              Characteristics(backbone=1),
              Characteristics(tail=1),
              Characteristics(eggs=0),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=1),
              Characteristics(fins=1),
              Characteristics(legs=0),
              Characteristics(predator=1)),salience=N)
    def _dolphin(self):
        self.declare(Characteristics(name='dolphin'))

    #######################################################
    @Rule(Characteristics(name = 'octopus'))
    def octopus(self):
        print('octopus')
        # quit()

    @Rule(AND(Characteristics(hair=0),
              Characteristics(toothed=0),
              Characteristics(backbone=0),
              Characteristics(tail=0),
              Characteristics(eggs=1),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=1),
              Characteristics(fins=0),
              Characteristics(legs=8),
              Characteristics(predator=1)),salience=N)
    def _octopus(self):
        self.declare(Characteristics(name='octopus'))

    #######################################################
    @Rule(Characteristics(name = 'frog'))
    def frog(self):
        print('frog')
        # quit()

    @Rule(AND(Characteristics(hair=0),
              Characteristics(toothed=1),
              Characteristics(backbone=1),
              Characteristics(tail=0),
              Characteristics(eggs=1),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=1),
              Characteristics(fins=0),
              Characteristics(legs=4),
              Characteristics(predator=1)),salience=N)
    def _frog(self):
        self.declare(Characteristics(name='frog'))

    #######################################################
    @Rule(Characteristics(name = 'turtle'))
    def turtle(self):
        print('turtle')
        # quit()

    @Rule(AND(Characteristics(hair=0),
              Characteristics(toothed=0),
              Characteristics(backbone=1),
              Characteristics(tail=1),
              Characteristics(eggs=1),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=1),
              Characteristics(fins=0),
              Characteristics(legs=4),
              Characteristics(predator=0)),salience=N)
    def _turtle(self):
        self.declare(Characteristics(name='turtle'))

    #######################################################
    @Rule(Characteristics(name = 'ladybird'))
    def ladybird(self):
        print('ladybird')
        # quit()

    @Rule(AND(Characteristics(hair=0),
              Characteristics(toothed=0),
              Characteristics(backbone=0),
              Characteristics(tail=0),
              Characteristics(eggs=1),
              Characteristics(feathers=0),
              Characteristics(airborne=1),
              Characteristics(domestic=0),
              Characteristics(fins=0),
              Characteristics(legs=6),
              Characteristics(predator=1)),salience=N)
    def _ladybird(self):
        self.declare(Characteristics(name='ladybird'))

    #######################################################
    @Rule(Characteristics(name = 'duck'))
    def duck(self):
        print('duck')
        # quit()

    @Rule(AND(Characteristics(hair=0),
              Characteristics(toothed=0),
              Characteristics(backbone=1),
              Characteristics(tail=1),
              Characteristics(eggs=1),
              Characteristics(feathers=1),
              Characteristics(airborne=1),
              Characteristics(domestic=1),
              Characteristics(fins=0),
              Characteristics(legs=2),
              Characteristics(predator=1)),salience=N)
    def _duck(self):
        self.declare(Characteristics(name='duck'))

    #######################################################
    @Rule(Characteristics(name = 'lobster'))
    def lobster(self):
        print('lobster')
        # quit()

    @Rule(AND(Characteristics(hair=0),
              Characteristics(toothed=0),
              Characteristics(backbone=0),
              Characteristics(tail=1),
              Characteristics(eggs=1),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=1),
              Characteristics(fins=0),
              Characteristics(legs=6),
              Characteristics(predator=1)),salience=N)
    def _lobster(self):
        self.declare(Characteristics(name='lobster'))

    #######################################################
    @Rule(Characteristics(name = 'snake'))
    def snake(self):
        print('snake')
        # quit()

    @Rule(AND(Characteristics(hair=0),
              Characteristics(toothed=1),
              Characteristics(backbone=1),
              Characteristics(tail=1),
              Characteristics(eggs=1),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=0),
              Characteristics(fins=0),
              Characteristics(legs=0),
              Characteristics(predator=1)),salience=N)
    def _snake(self):
        self.declare(Characteristics(name='snake'))

    #######################################################
    @Rule(Characteristics(name = 'carp'))
    def crap(self):
        print('carp')
        # quit()

    @Rule(AND(Characteristics(hair=0),
              Characteristics(toothed=1),
              Characteristics(backbone=1),
              Characteristics(tail=1),
              Characteristics(eggs=1),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=1),
              Characteristics(fins=1),
              Characteristics(legs=0),
              Characteristics(predator=1)),salience=N)
    def _carp(self):
        self.declare(Characteristics(name='carp'))

    #######################################################
    @Rule(Characteristics(name = 'penguin'))
    def penguin(self):
        print('penguin')
        # quit()

    @Rule(AND(Characteristics(hair=0),
              Characteristics(toothed=0),
              Characteristics(backbone=1),
              Characteristics(tail=1),
              Characteristics(eggs=1),
              Characteristics(feathers=1),
              Characteristics(airborne=0),
              Characteristics(domestic=1),
              Characteristics(fins=0),
              Characteristics(legs=2),
              Characteristics(predator=1)),salience=N)
    def _penguin(self):
        self.declare(Characteristics(name='penguin'))

    #######################################################
    @Rule(Characteristics(name = 'earthworm'))
    def earthworm(self):
        print('earthworm')
        # quit()

    @Rule(AND(Characteristics(hair=0),
              Characteristics(toothed=0),
              Characteristics(backbone=0),
              Characteristics(tail=1),
              Characteristics(eggs=1),
              Characteristics(feathers=0),
              Characteristics(airborne=0),
              Characteristics(domestic=0),
              Characteristics(fins=0),
              Characteristics(legs=0),
              Characteristics(predator=0)),salience=N)
    def _earthworm(self):
        self.declare(Characteristics(name='earthworm'))

    #######################################################


    @Rule(OR(
        AND(Characteristics(hair = 1),Characteristics(eggs = 1)),
        AND(Characteristics(hair = 1), Characteristics(teethed = 0))),salience=M)
    def maybePlatypus(self):
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(eggs = 1))
        self.declare(Characteristics(teethed = 0))
        self.declare(Characteristics(backbone = 1))
        #print("something")

    @Rule(Characteristics(hair = 1),salience=M-1)
    def hair(self):
        self.declare(Characteristics(backbone = 1))
        self.declare(Characteristics(airborne = 0))
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(fins = 0))
        # print(self.facts)


    @Rule(Characteristics(toothed = 1),salience=M-2)
    def toothed(self):
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(backbone = 1))
        self.declare(Characteristics(airborne = 0))

    @Rule(Characteristics(backbone = 1),salience=M-3)
    def backbone(self):
        print("co xuong cung co suy ra duoc cai gi dau")

    @Rule(Characteristics(tail = 0),salience=M-4)
    def tail0(self):
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(fins = 0))

    @Rule(Characteristics(tail = 1),salience=M-6)
    def tail(self):
        print("co duoi cung vay thoi a")

    @Rule(Characteristics(eggs = 1),salience=M-7)
    def eggs(self):
        print("de trung thi de chua biet lam sao")

    @Rule(Characteristics(eggs = 0),salience=M-8)
    def eggs0(self):
        self.declare(Characteristics(backbone = 1))
        self.declare(Characteristics(hair = 1))
        self.declare(Characteristics(toothed = 1))
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(airborne = 0))

    @Rule(Characteristics(feathers = 1),salience=M-9)
    def feathers(self):
        self.declare(Characteristics(eggs = 1))
        self.declare(Characteristics(backbone = 1))
        self.declare(Characteristics(hair = 0))
        self.declare(Characteristics(toothed = 0))
        self.declare(Characteristics(tail = 1))
        self.declare(Characteristics(fins = 0))

    @Rule(Characteristics(airborne = 1),salience=M+1)
    def airborne(self):
        self.declare(Characteristics(eggs = 1))
        self.declare(Characteristics(toothed = 0))
        self.declare(Characteristics(hair = 0))
        self.declare(Characteristics(fins = 0))

    @Rule(Characteristics(fins = 1),salience=M+2)
    def fins(self):
        self.declare(Characteristics(hair = 0))
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(toothed = 1))
        self.declare(Characteristics(backbone = 1))
        self.declare(Characteristics(tail = 1))
        self.declare(Characteristics(airborne = 0))
        self.declare(Characteristics(domestic = 1))
        self.declare(Characteristics(legs = 0))
        self.declare(Characteristics(predator = 1))

    @Rule(Characteristics(legs = 0),salience=M+3)
    def legs0(self):
        self.declare(Characteristics(tail = 1))
        self.declare(Characteristics(hair = 0))
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(airborne = 0))

    @Rule(Characteristics(legs = 4),salience=M+4)
    def legs4(self):
        self.declare(Characteristics(backbone = 1))
        self.declare(Characteristics(airborne = 0))
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(fins = 0))

    @Rule(Characteristics(legs = 6),salience=M+5)
    def legs6(self):
        self.declare(Characteristics(predator = 1))
        self.declare(Characteristics(hair = 0))
        self.declare(Characteristics(feathers  = 0))
        self.declare(Characteristics(eggs = 1))
        self.declare(Characteristics(fins = 0))
        self.declare(Characteristics(backbone = 0))

    @Rule(Characteristics(legs = 8),salience=M+6)
    def legs8(self):
        self.declare(Characteristics(predator = 1))
        self.declare(Characteristics(hair = 0))
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(tail = 0))
        self.declare(Characteristics(eggs = 1))
        self.declare(Characteristics(toothed = 0))
        self.declare(Characteristics(fins = 0))
        self.declare(Characteristics(domestic = 1))
        self.declare(Characteristics(backbone = 0))
        self.declare(Characteristics(airborne = 0))




watch('RULES','FACTS')
engine = Diagnosis_animals()
bear = f.diction['bear'].copy()
del bear['name']
engine.reset()  # Prepare the engine for the execution.
# engine.declare(Characteristics(hair = 0))
engine.declare(Characteristics(feathers = 1))
engine.declare(Characteristics(airborne =0))
engine.declare(Characteristics(backbone = 1))
engine.declare(Characteristics(eggs = 1))
engine.declare(Characteristics(toothed = 0))
engine.declare(Characteristics(predator = 1))
engine.declare(Characteristics(legs = 2))
engine.declare(Characteristics(fins = 0))
engine.declare(Characteristics(domestic = 1))
engine.declare(Characteristics(tail =1))
engine.facts
# print(engine.facts)
engine.run()  # Run it!