import json


class Dependency():
    def __init__(self):

        self.name = "glibc"
        self.operate = "eq"
        self.version = "4.6.*"


class Package():
    def __init__(self, first_name, deps):
        self.name = first_name
        self.maintainer = first_name
        self.updated = first_name
        self.version = first_name
        self.uses = first_name
        self.depends = deps
        self.opt_depends = deps
        self.choice_depends = deps


dp = Dependency()
pkg = Package("test", [dp])


json_data = json.dumps( pkg, default=lambda o: o.__dict__, indent=4,sort_keys=False)
print(json_data)
