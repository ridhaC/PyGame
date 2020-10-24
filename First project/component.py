from multipledispatch import dispatch
from vector import Vector2
from pygame import *

class Component:
    def __init__(self, name, gameobject):
        self.name = name
        self.gameobject = gameobject

    def update(self):
        pass

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

class SpriteRenderer:
    all_renderers = []
    screen = None
     
    @dispatch(self, pygame.image)
    def __init__(self, sprite):
        self.sprite = sprite
        SpriteRenderer.append(all_renderers)

    def render(self):
        SpriteRenderer.screen.blit(self.sprite, self.gameobject.transform.position.tuple())

    def render_all():
        for sprite in all_renderers:
            sprite.render()

