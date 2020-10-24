from multipledispatch import dispatch
from vector import Vector2

class Component:
    def __init__(self, name):
        self.name = name

    def update(self):
        

class Transform:
    @dispatch(self, Vector2, Vector2, float)
    def __init__(self, position, scale, rotation):
        self.position = position
        self.scale = scale
        self.rotation = rotation

    @dispatch(self)
    def __init__(self):
        self.position = Vector2.zero
        self.scale = Vector2.one
        self.rotation = 0
