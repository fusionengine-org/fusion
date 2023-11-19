import fusionengine.files.window as fe_window


class Scene:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def run(self):
        self.function()

    def change_function(self, function):
        self.function = function


class SceneManager:
    def init(self, window: fe_window.Window):
        self.window = window
        self.scenes = {}

    def add_scene(self, scene: Scene):
        self.scenes[scene.name] = scene

    def remove_scene(self, name):
        del self.scenes[name]

    def change_scene(self, name, scene: Scene):
        self.scenes[name] = scene

    def get_scene(self, name):
        return self.scenes[name]

    def start(self):
        for scene in list(self.scenes.values()):
            scene.run()

    def loop(self, function, window):
        @window.loop
        def wrapper():
            function()
