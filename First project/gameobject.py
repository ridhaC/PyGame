class Gameobject:
    gameobject_list = []
    def __init__(self, name):
        self.name = name
        self.component_list = []
        self.transform = component.Transform()
        Gameobject.gameobject_list.append(self)

    def add_componenet(self, componenet):
        self.component_list.append(componenet)

    def update(self):
        for component in self.component_list:
            component.update()


    