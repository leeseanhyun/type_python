"""
* [property]
* 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
* 인스턴스 변수 값에 대한 유효성 검사 및 수정
"""

# class Robot:
class Robot():
    
    """
    Robot Class
    """
    
    # 클래스 변수 : 인스턴스들이 공유하는 변수
    __population = 0
    
    # 생성자 함수
    def __init__(self, name, age):
        self.__name = name        # 인스턴스 변수
        self.__age = age
        Robot.__population += 1

    @property
    def name(self):
        return f"Lee {self.__name}."

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if new_age - self.__age == 1:
            self.__age = new_age            
        else:
            raise TypeError("invalid range to age.")
    
    # 인스턴스 메서드
    def say_hi(self):
        # code...
        print(f"Greetings, my masters call me {self.__name}.")
    
    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b
    
    # 클래스 메서드
    @classmethod
    def how_many(cls):      # cls : 클래스를 받음
        print(f"We have {cls.__population} robots.")


droid = Robot("R2-D2", 2)

print(droid.age)

# droid.age = 7
droid.age += 1
# droid.age = -999

print(droid.age)

print(droid.name)
