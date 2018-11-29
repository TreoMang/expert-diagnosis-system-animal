from pyknow import *
import file_dict as f
# import GUI
class Characteristics(Fact):
    """ Dac diem nhan dang dong vat """
    pass

class Diagnosis_animals(KnowledgeEngine):
    N = 20
    M = 10
    # def __init__(self):
    #     self.name = ' '
    # print(bear)
    @Rule(Characteristics(name = 'platypus'))
    def platypus(self):
        self.name = 'Thú mỏ vịt'
        # self.func_return('Thú mỏ vịt')
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
        self.name = 'Gấu'
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
        self.name = 'Báo'
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
        self.name = 'Gorilla'
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
        self.name = 'Voi'
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
        self.name = 'Cá heo'
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
        self.name = 'Bạch tuột'
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
        self.name = 'Ếch'
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
        self.name = 'Rùa'
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
        self.name = 'Bọ rùa'
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
        self.name = 'Vịt'
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
        self.name = 'Tôm'
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
        self.name = 'Rắn'
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
        self.name = 'Cá chép'
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
        self.name = 'Chim cánh cụt'
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
        self.name = 'Giun đất'
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

    # @Rule(Characteristics(backbone = 1),salience=M-3)
    # def backbone(self):
    #     print("co xuong cung co suy ra duoc cai gi dau")

    @Rule(Characteristics(tail = 0),salience=M-4)
    def tail0(self):
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(fins = 0))

    # @Rule(Characteristics(tail = 1),salience=M-6)
    # def tail(self):
    #     print("co duoi cung vay thoi a")

    # @Rule(Characteristics(eggs = 1),salience=M-7)
    # def eggs(self):
    #     print("de trung thi de chua biet lam sao")

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


    def func_return(self):
        # self.name = name
        return self.name

class Process(Fact):
    def __init__(self,value):
        watch('RULES','FACTS')
        self.engine = Diagnosis_animals()
        self.engine.reset()  # Prepare the engine for the execution.

        self.para(value)

        self.engine.facts
        self.engine.run()  # Run it!

    def call_again(self):
        return self.engine.func_return()

    def para(self, value):
        # for i in range(11):
        #     variable = f.key[i + 1]
        #     self.engine.declare(Characteristics(setattr(self, variable, value[i].get())))
        self.engine.declare(Characteristics(hair=value[0].get()))
        self.engine.declare(Characteristics(toothed=value[1].get()))
        self.engine.declare(Characteristics(backbone=value[2].get()))
        self.engine.declare(Characteristics(tail=value[3].get()))
        self.engine.declare(Characteristics(eggs=value[4].get()))
        self.engine.declare(Characteristics(feathers=value[5].get()))
        self.engine.declare(Characteristics(airborne=value[6].get()))
        self.engine.declare(Characteristics(domestic=value[7].get()))
        self.engine.declare(Characteristics(fins=value[8].get()))
        self.engine.declare(Characteristics(legs=value[9].get()))
        self.engine.declare(Characteristics(predator=value[10].get()))

        # engine.declare(Characteristics(exec(tmp + " = 1")))
        # self.engine.declare(Characteristics(hair = 1))
        # self.engine.declare(Characteristics(feathers = 0))
        # self.engine.declare(Characteristics(airborne =0))
        # self. engine.declare(Characteristics(backbone = 1))
        # self.engine.declare(Characteristics(eggs = 1))
        # self.engine.declare(Characteristics(toothed = 0))
        # self.engine.declare(Characteristics(predator = 1))
        # self.engine.declare(Characteristics(legs = 4))
        # self.engine.declare(Characteristics(fins = 0))
        # self.engine.declare(Characteristics(domestic = 1))
        # self.engine.declare(Characteristics(tail =1))

    # print(engine.facts)

