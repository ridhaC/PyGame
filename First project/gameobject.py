class gameobject:
    gameobject_list = []
    def __init__(self, name):
        self.name = name
        self.component_list = []
        gameobject.gameobject_list.append(self)

    