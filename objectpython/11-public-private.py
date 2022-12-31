"""
* public vs private
"""

# class Robot:
class Robot():
    
    """
    Robot Class
    """
    
    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0
    
    # 생성자 함수
    def __init__(self, name, age):
        self.name = name        # 인스턴스 변수
        self.__age = age
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        # code...
        print(f"Greetings, my masters call me {self.name}.")
    
    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b
    
    # 클래스 메서드
    @classmethod
    def how_many(cls):      # cls : 클래스를 받음
        print(f"We have {cls.population} robots.")

class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(self.name)
        
        self.__age = 999
        print(self.__age)

ss = Robot("tss", 8)

sss = Siri("iphone8", 10)
