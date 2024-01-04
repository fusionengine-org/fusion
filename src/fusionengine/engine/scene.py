class Scene:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def run(self):
        self.function()

    def change_function(self, function):
        self.function = function

