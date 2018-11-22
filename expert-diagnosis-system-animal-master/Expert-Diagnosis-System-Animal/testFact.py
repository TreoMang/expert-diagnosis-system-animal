from pyknow import *
class Good_weather_3(KnowledgeEngine):
    @Rule(Fact("it's nice and warm"), salience=1)
    def _2(self):
        print("Let's go for a swim in the sea!")

    @Rule(Fact(MATCH.factstringvalue & "it's sunny"), salience=10)
    def _3(self,factstringvalue):
        print("given that ..." + factstringvalue + " ... I conclude it's nice and warm.")
        self.declare(Fact("it's nice and warm"))

    @Rule(AS.x << Fact("it's nice and warm"), Fact("winter"), salience=0)
    def _winter(self,x):
        self.retract(x)
        print("Never mind, it's winter.")

engine = Good_weather_3()
engine.reset()
engine.declare(Fact("Le Thi Thuy Trang"))
engine.run()