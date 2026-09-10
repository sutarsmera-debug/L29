from abc import ABC, abstractmethod
from modulefinder import test
class Absclass(ABC):
    def print(self,x):
        print("Passsed value: ", x)

        @abstractmethod
        def task(self):
            print("We are inside Absclass task")
class Test_class(Absclass):
    def task(self):
        print("We are inside Test_class task")

test.obj = Test_class()
test.obj.task()
test.obj.print(100)
