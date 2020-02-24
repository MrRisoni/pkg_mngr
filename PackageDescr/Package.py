class Package:

    def __init__(self, name, maintain,updated,version,uses,depends,opt_depends, choice_depends):
        self.name = name
        self.maintainer = maintain
        self.updated = updated
        self.version = version
        self.uses = uses
        self.depends = depends
        self.opt_depends = opt_depends
        self.choice_depends = choice_depends
