class Choices(object):
    def __init__(self,title, choice_deps,allow_many):

        self.title = title
        self.options = choice_deps
        self.allow_many = allow_many
