"""
# * 추상화 : abstraction
# * 불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써
# * 공통의 속성 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것이다.

# * namespase : 개체를 구분할 수 있는 범위
# * __dict__ : 네임스페이스를 확인할 수 있다.
# * dir() : 네임스페이스의 key 값을 확인할 수 있다.
# * __doc__ : class의 주석을 확인한다.
# * __class__ : 어떤 클래스로 만들어진 인스턴스인지를 확인할 수 있다.
"""

class Robot:
    
    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0
    
    # 생성자 함수
    def __init__(self, name, code):
        self.name = name        # 인스턴스 변수
        self.code = code        # 인스턴스 변수
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        # code...
        print(f"Greetings, my masters call me {self.name}.")
    
    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b
    
    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    # 클래스 메서드
    @classmethod
    def how_many(cls):      # cls : 클래스를 받음
        print(f"We have {cls.population} robots.")

print(Robot.population)         # 0

siri = Robot("siri", 21039788127)

print(Robot.population)         # 1

jarvis = Robot("jarvis", 2311213123)

print(Robot.population)         # 2

bixby = Robot("bixby", 123456579)

print(Robot.population)         # 3

bixby2 = Robot("bixby2", 987654321)

print(Robot.population)         # 3

print(siri.name)
print(siri.code)

jarvis.say_hi()

siri.say_hi()
siri.cal_add(2,3)

siri.die()

Robot.how_many()

