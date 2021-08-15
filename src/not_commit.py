""" error message / コンマ忘れてても教えてくれる
items = {
	"x":1,
	"y":2   #commaを忘れることくらい、ありますよね？
	"x":3,
}
print(items)
"""
""" error message / いい感じで名前を推論して教えてくれる
abcdefg = None # 斬新でよくわからない名前で変数名を定義
abcdee         # 案の定タイポしたとする
"""

"""
def where_is(points):
    match points:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")
"""
"""
def where_is(points):
    match points:
        case []:
            print("No points")
        case [Point() as x, Point() as y, *others]:
            print(f"{x}, {y} and {len(others)}others")
        case _:
            print("Something else")
where_is([Point(1,0),Point(2,0),Point(3,0),Point(0,1), Point(0,2)])
"""

""" 型チェックはまだ対応してないはずなのでこんなのかけちゃう
from enum import Enum
class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

def which_color(color: Color):
    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case 1:
            print("!!!")
which_color(1)
"""

""" bind変数が違うとエラー
def error(input):
    match input:
        case [0,x] | [1,y]:
            print("ok")
        case _:
            print("something wrong")
error([3,1])
"""

"""
class test1:
    def __enter__(self, *args):
        print("enter")
    def __exit__(self, *args):
        print("exit")

class test2:
    def __enter__(self, *args):
        print("enter2")
    def __exit__(self, *args):
        print("exit2")

with (test1() as f1, test2() as f2):
    print("hello")
    raise Exception("hoge")
"""
"""

def is_pet(animal):
    if(isinstance(animal, Cat|Dog)):
    #   if(isinstance(animal, Union[Cat, Dog])):
        return True
    else:
        return False

dog = Dog("pochi", "Chihuahua")
cat = Cat("tama", "white")
crow = Crow("car")

print(is_pet(dog))    
print(is_pet(cat))    
print(is_pet(crow))    
"""