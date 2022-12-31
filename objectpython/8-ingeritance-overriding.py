class Robot:
    
    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0
    
    # 생성자 함수
    def __init__(self, name):
        self.name = name        # 인스턴스 변수
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
        
class Siri(Robot):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Siri.population += 1
    
    def call_me(self):
        print("네?")
    
    def cal_mul(self, a, b):
        self.a = a
        return a * b
    
    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello apple!!")
        
    def say_hi(self):
        # code...
        print(f"Greetings, my masters call me {self.name}. by apple.")

    @classmethod
    def how_many(cls):      # cls : 클래스를 받음
        return f"We have {cls.population} robots. by apple."

siri = Siri("iphone6", 17)
siri.say_hi()
print(Siri.how_many())