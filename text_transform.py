import math
import random

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import PushMatrix, PopMatrix, Rotate, Translate
from kivy.lang import Builder
from kivy.uix.label import Label

KIVY_CONFIG = """
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        id: container
"""

WORDS = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit,', 'sed', 'do', 'eiusmod',
         'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore', 'magna', 'aliqua.', 'Ut', 'enim', 'ad', 'minim',
         'veniam,', 'quis', 'nostrud', 'exercitation', 'ullamco', 'laboris', 'nisi', 'ut', 'aliquip', 'ex', 'ea',
         'commodo', 'consequat.', 'Duis', 'aute', 'irure', 'dolor', 'in', 'reprehenderit', 'in', 'voluptate', 'velit',
         'esse', 'cillum', 'dolore', 'eu', 'fugiat', 'nulla', 'pariatur.', 'Excepteur', 'sint', 'occaecat', 'cupidatat',
         'non', 'proident,', 'sunt', 'in', 'culpa', 'qui', 'officia', 'deserunt', 'mollit', 'anim', 'id', 'est',
         'laborum']
MIN_FONT_SIZE = 10
MAX_FONT_SIZE = 45


class TextTransformApp(App):

    def build(self):
        self.title = "Text transform experiment"
        self.root = Builder.load_string(KIVY_CONFIG)
        Window.size = (800, 800)
        container = self.root.ids.container
        self.create_word_cloud_widgets(container, WORDS)
        return self.root

    def create_word_cloud_widgets(self, container, words):
        for word in words:
            label = Label(text=word)
            label.font_size = random.uniform(MIN_FONT_SIZE, MAX_FONT_SIZE)
            position = tuple(random.uniform(-Window.size[0] / 2, Window.size[1] / 2) for _ in range(2))
            rotation = random.uniform(0, 360)
            self.set_up_transform(label, position, rotation)
            container.add_widget(label)

    @staticmethod
    def set_up_transform(widget, position, rotation):
        with widget.canvas.before:
            PushMatrix()
            # TODO: Translate is currently not working correctly.
            Translate(*position)
            Rotate(angle=rotation,
                   origin=tuple(x / 2 for x in Window.size))
        with widget.canvas.after:
            PopMatrix()


TextTransformApp().run()
