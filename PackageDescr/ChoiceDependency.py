from .Dependency import Dependency

class ChoiceDependency(Dependency):
    def __init__(self,title,opr,ptr,defaultVal):
        super().__init__(title,opr,ptr)
        self.default = defaultVal
