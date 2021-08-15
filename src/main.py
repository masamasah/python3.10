from dataclasses import dataclass 
from typing import Union
import sys


@dataclass 
class Dog:
    name:str
    breed:str

@dataclass
class Cat:
    name:str
    color:str

@dataclass
class Crow:
    name: str

# TypeUnion
def can_pet(animal: Dog | Cat):
    pass

# 数値リテラルのパターン
def lesson_1():
    def http_error(status):
        match status:
            case 400:
                print("Bad request")
            case 404:
                print("Not found")
            case 418:
                print("I'm a teapot")

    http_error(400)

# defaultのパターン
def lesson_2():

    def http_error(status):
        match status:
            case 400:
                print("Bad request")
            case 404:
                print("Not found")
            case 418:
                print("I'm a teapot")
            case 200 | 201:
                print("OK")
            case _:
                print("something worng")

    http_error(405)

# 自作型のパターン
def lesson_3():

    def is_dog(animal):
        """引数がDogかどうかを判定する
        """
        match animal:
            case Dog():
                return True
        return False

    def is_pet(animal):
        """引数がペットにできるかどうか(DogもしくはCat)かどうかを判定する
        """
        match animal:
            case Dog() | Cat():
                return True
            case _:
                return False

    dog = Dog("pochi", "Chihuahua")
    cat = Cat("tama", "white")
    crow = Crow("car")

    print(is_pet(dog))    
    print(is_pet(cat))    
    print(is_pet(crow))    

# メンバ変数でのパターン
def lesson_4():

    def is_mypet(animal):
        """自分のペットかどうかを判定する。
        name=pochiでbreed=Chihuahuaなのが自分のペット
        """
        match animal:
            case Dog(name="pochi", breed="Chihuahua"):
                return True
            case _:
                return False

    mypet = Dog("pochi", "Chihuahua")
    anotherDog = Dog("hanako", "Shiba")
    crow = Crow("car")

    print(is_mypet(mypet))    
    print(is_mypet(anotherDog))    
    print(is_mypet(crow))    

# メンバ変数パターンでのワイルドカード
def lesson_5():

    def is_Chihuahua(animal):
        """引数がチワワかどうかを判定する。
        """
        match animal:
            case Dog(name=_, breed="Chihuahua"):
                return True
            case _:
                return False

    chihuahua_1 = Dog("pochi", "Chihuahua")
    shiba = Dog("hanako", "Shiba")
    chihuahua_2 = Dog("taro", "Chihuahua")
    crow = Crow("car")

    print(is_Chihuahua(chihuahua_1))    
    print(is_Chihuahua(shiba))    
    print(is_Chihuahua(chihuahua_2))    
    print(is_Chihuahua(crow))    

#バインディング
def lesson_6():
    def build_message(animal):
        match animal:
            case Dog("pochi", "Chihuahua"):
                return f"he is my pet!"
            case Dog(name = _ as dog_name, breed="Chihuahua"): # dog_nameという名前にバインディングしている
                return f"I love Chihuahua ! come on {dog_name}!"
            case Dog(_, "Shiba"):
                return f"Shiba is not so bad."
            case _:
                return "..."

    mypet = Dog("pochi", "Chihuahua")
    anotherDog = Dog("hanako", "Shiba")
    chihuahua_2 = Dog("taro", "Chihuahua")
    cat = Cat("tama", "White")
    crow = Crow("car")

    print(build_message(mypet))    
    print(build_message(chihuahua_2))    
    print(build_message(anotherDog))
    print(build_message(cat))    
    print(build_message(crow))  

# lesson7 エラーで落ちるのでコメントアウトしています
def lesson_7():
    pass
    """
    # https://www.python.org/dev/peps/pep-0635/#overview-and-terminology

    def build_message(animal):
        hoge=[0]
        match animal:
            case Dog("pochi", "Chihuahua"):
                return f"he is my pet!"
            case Dog(_ as hoge[0], "Chihuahua"): # hogeの第一引数に代入しようとしているがNG
                return f"I love Chihuahua ! come on {name}!"
            case Dog(_, "Shiba"):
                return f"Shiba is not so bad."
            case _:
                return "..."

    dog = Dog("pochi", "Chihuahua")
    anotherDog = Dog("hanako", "Shiba")
    cat = Cat("tama", "White")
    crow = Crow("car")

    print(build_message(dog))    
    print(build_message(anotherDog))
    print(build_message(cat))    
    print(build_message(crow))  
"""

# バインディング
def lesson_8():
    # https://www.python.org/dev/peps/pep-0635/#overview-and-terminology

    def build_message(animal):
        name="X"
        match animal:
            case Dog("pochi", "Chihuahua"):
                val= f"he is my pet!"
            case Dog(_ as name, "Chihuahua"): # nameを上書きしているようにみえるが？
                val= f"I love Chihuahua ! come on {name}!"
            case Dog(_, "Shiba"):
                val= f"Shiba is not so bad."
            case _:
                val= "..."
        print(name) # ここではXが出力される。名前がかぶっていても、もとのnameが予期せぬ上書きをされない
        return val

    anotherDog = Dog("hanako", "Chihuahua")

    print(build_message(anotherDog))

# バインディング list
def lesson_9():
    l = [1,2,3,4,5]
    match l:
        case [first, *middle, last]:
            print(f"first is {first}, last is {last},")
            print(f"size of middle is {len(middle)}")

# input parser
args = sys.argv

match args:
    case (_, "lesson_1"): lesson_1()
    case (_, "lesson_2"): lesson_2()
    case (_, "lesson_3"): lesson_3()
    case (_, "lesson_4"): lesson_4()
    case (_, "lesson_5"): lesson_5()
    case (_, "lesson_6"): lesson_6()
    case (_, "lesson_7"): lesson_7()
    case (_, "lesson_8"): lesson_8()
    case (_, "lesson_9"): lesson_9()
    case (_, _): print("input lesson_n")
    case _: print(f"illegal input")

