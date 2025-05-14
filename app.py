import logging

from textual.app import App
from textual.widgets import Header, Footer, Button, Static
from textual import log

# Configuración de logging para archivo y consola
logging.basicConfig(
    level="INFO",
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("textual.log", mode='a', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


class TestApp(App):
    TITLE = "Textual Test App"
    
    def on_load(self):
        self.log("On the on_load method!")

    def compose(self):
        self.log("On the compose method!")
        yield Header()
        yield Button("Click Me!", id="btn")
        yield Static("This is a test Textual app")
        yield Footer()
    
    def on_button_pressed(self, event):
        self.log("On the on_button_pressed method!")
        self.query_one(Static).update("Button was clicked!")

if __name__ == "__main__":
    log.debug("Hello world!")
    app = TestApp()
    app.run()