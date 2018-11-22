from pyknow import *
import file_dict as f

class Characteristics(Fact):
    """ Dac diem nhan dang dong vat """
    pass

class Diagnosis_animals(KnowledgeEngine):

    @DefFacts()
    def set_rule(self):
        yield Characteristics()

    # print(bear)
    @Rule(Characteristics(name = 'bear'))
    def bear(self):
        print('bear')

    @Rule(Characteristics(name = 'platypus'))
    def platypus(self):
        print('platypus')

    @Rule(Characteristics(name = 'leopard'))
    def leopard(self):
        print('leopard')

    @Rule(Characteristics(name = 'gorilla'))
    def gorilla(self):
        print('gorilla')

    @Rule(Characteristics(name = 'elephant'))
    def elephant(self):
        print('elephant')

    @Rule(Characteristics(name = 'dolphin'))
    def dolphin(self):
        print('dolphin')

    @Rule(Characteristics(name = 'octopus'))
    def octopus(self):
        print('octopus')

    @Rule(Characteristics(name = 'frog'))
    def frog(self):
        print('frog')

    @Rule(Characteristics(name = 'turtle'))
    def turtle(self):
        print('turtle')

    @Rule(Characteristics(name = 'ladybird'))
    def ladybird(self):
        print('ladybird')

    @Rule(Characteristics(name = 'duck'))
    def duck(self):
        print('duck')

    @Rule(Characteristics(name = 'lobster'))
    def lobster(self):
        print('lobster')

    @Rule(Characteristics(name = 'snake'))
    def snake(self):
        print('snake')

    @Rule(Characteristics(name = 'carp'))
    def penguin(self):
        print('carp')

    @Rule(Characteristics(name = 'penguin'))
    def penguin(self):
        print('penguin')

    @Rule(Characteristics(name = 'giun'))
    def penguin(self):
        print('giun')

    @Rule(OR(
        AND(Characteristics(hair = 1),Characteristics(eggs = 1)),
        AND(Characteristics(hair = 1), Characteristics(teethed = 0))))
    def maybePlatypus(self):
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(eggs = 1))
        self.declare(Characteristics(teethed = 0))
        self.declare(Characteristics(backbone = 1))
        #print("something")

    @Rule(Characteristics(hair = 1))
    def hair(self):
        self.declare(Characteristics(backbone = 1))
        self.declare(Characteristics(airborne = 0))
        self.declare(Characteristics(feathers = 0))
        self.declare(Characteristics(fins = 0))
		# print(self.facts)

    @Rule(AND(
	      Characteristics(hair = 1), Characteristics(backbone = 1)
		  , Characteristics(airborne = 0)))
    def something(self):
        print("hello")





watch('RULES','FACTS')
engine = Diagnosis_animals()
bear = f.diction['bear'].copy()
del bear['name']
engine.reset()  # Prepare the engine for the execution.
engine.declare(Characteristics(hair = 1))
#engine.declare(Characteristics(hair = 1))
engine.facts
# print(engine.facts)
engine.run()  # Run it!