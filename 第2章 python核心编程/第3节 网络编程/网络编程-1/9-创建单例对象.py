class Dog(object):
    __instance = None
    __init__flag = False
    def __new__(cls,name):
        if cls.__instance==None:
            cls.__instance=object.__new__(cls)
            return cls.__instance
        else:
            return  cls.__instance
    def __init__(self,name):
        if Dog.__init__flag==False:
            self.name = name
            Dog.__init__flag=True


dog1 = Dog("旺财")
print(id(dog1))
print(dog1.name)
dog2 = Dog("哮天犬")
print(id(dog2))
print(dog2.name)