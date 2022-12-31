from typing import List, Tuple, Dict

int_var : int = 88
str_var : str = "hello world"
float_var : float = 88.9
bool_var : bool = True

# list_var : List[int] = [1, 2, 3]
list_var : List[str] = ["1", "2", "3"]
tuple_var : Tuple[int, ...] = (1, 3, 4)

dic_var : Dict[str, int] = {"hello": 47, "world": 47}

# 중요한 함수인 경우 타입체크를 권장
def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}")

def cal_add(x: int, y: int) -> int:
    type_check(x, int)
    type_check(y, int)
    return x + y

print(cal_add(1, 3))

# cal_add("1, ", "3, asdlkfjasdfl")

# print(cal_add([1, 3], [4, 5]))

# * isinstance(obj, class)

# print(isinstance(False, bool))
# print(isinstance(88.9, float))