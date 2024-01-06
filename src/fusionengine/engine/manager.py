from fusionengine.engine.window import Window
from fusionengine.engine.scene import Scene


class SceneManager:
    def init(self, window: Window) -> None:
        """
        Creates a new SceneManager

        Args:
            window (Window): Your window
        """
        self.window = window
        self.scenes = {}

    def add_scene(self, scene: Scene) -> None:
        """
        Adds a scene to the manager

        Args:
            scene (Scene): The scene to add
        """
        self.scenes[scene.name] = scene

    def remove_scene(self, name: str) -> None:
        """
        Removes a scene from the manager

        Args:
            name (str): The name of the scene to remove
        """
        del self.scenes[name]

    def change_scene(self, name: str, scene: Scene) -> None:
        """
        Changes the scene provided with a name to the given scene

        Args:
            name (str): The name of the scene to change
            scene (Scene): The scene to change to
        """
        self.scenes[name] = scene

    def get_scene(self, name: str) -> Scene:
        """
        Gets a scene from the manager

        Args:
            name (str): The name of the scene to get

        Returns:
            Scene: The scene
        """
        return self.scenes[name]

    def start(self):
        """
        Starts all the scenes one after a other
        """
        for scene in list(self.scenes.values()):
            scene.run()

    def loop(self, function, window: Window):
        """
        A decorator that to wrap the window loop

        Args:
            window (Window): The window to wrap
        """

        @window.loop
        def wrapper():
            function()
