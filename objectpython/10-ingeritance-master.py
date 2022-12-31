"""
* [클래스 상속]
* 1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.
* 2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
* 3. 메서드 오버라이딩
* 4. super()
* 5. Python의 모든 클래스는 object 클래서를 상속한다. : 모든 것은 객체이다.
* 6. MyClass.mro() --> 상속 관계를 보여준다.
"""


# class Robot:
class Robot(object):
    
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
    
    def call_me(self):
        print("네?")
    
    def cal_mul(self, a, b):
        self.a = a
        return a * b
    
    def cal_flexable(self, a, b):
        super().say_hi()
        self.say_hi()
        return self.cal_mul(a, b) + self.cal_add(a, b) + super().cal_add(a, b)
    
    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello apple!!")
        
    def say_hi(self):
        # code...
        print(f"Greetings, my masters call me {self.name}. by apple.")

    @classmethod
    def how_many(cls):      # cls : 클래스를 받음
        return f"We have {cls.population} robots. by apple."

siri = Siri("iphone8")

print(Siri.mro())           # [<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]

print(Robot.mro())

print(object)
print(dir(object))
print(object.__name__)
print(object.__repr__)

print(int.mro())
print(int.__init__(8.9))
print(int(8.9))

class A:
    pass

class B:
    pass

class C:
    pass

class D(A, B, C):
    pass

print(D.mro())