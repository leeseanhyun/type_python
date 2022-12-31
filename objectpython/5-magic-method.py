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
        
    @staticmethod
    def are_you_robot():
        print("yes!!")
    
    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call!!")
        return f"{self.name} call!!"
        
droid1 = Robot("R2-D2", 123456789)
droid1.say_hi()

print(dir(droid1))
print(droid1.__str__())     # <__main__.Robot object at 0x0000012F750102D0> -> R2-D2 robot!!


droid1()

