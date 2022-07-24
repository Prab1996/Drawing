import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)
        self.lol=[500,600,50,60]

        with self.canvas:
            Color(1,0,0,0.5, mode='rgba')
            self.draw = Line(points=(self.lol))

    def on_touch_down(self, touch):
        #print("mouse down", touch)
        x = touch.pos[0]
        y = touch.pos[1]
        self.lol.append(x)
        self.lol.append(y)
        self.draw.points=(self.lol)
        print(self.lol)
    def on_touch_move(self, touch):
        #print("mouse move", touch)
        m = touch.pos[0]
        x = touch.pos[1]
        self.lol.append(m)
        self.lol.append(x)
        self.draw.points=(self.lol)
        print(self.lol)
    #def on_touch_up(self, touch):
        #print("mouse up", touch)

class MyApp(App):
    def build(self):
        return Touch()

if __name__=="__main__":
    MyApp().run()
