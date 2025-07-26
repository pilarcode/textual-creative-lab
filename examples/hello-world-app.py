from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, Digits, Footer, Header,Static
from textual_plotext import PlotextPlot

class MyApp(App[None]):

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self):
        yield Header()
        yield Static("This is a test Textual app!")
        yield Footer()
  

if __name__ == "__main__":
    app = MyApp()
    app.run()
