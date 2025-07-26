from rich.console import Console
from textual.app import App, ComposeResult
from textual_image.renderable import Image
from textual.widgets import Footer, Header
from textual.app import RenderResult
from textual.widget import Widget
from pathlib import Path

class ImageBox(Widget):
    """ ImageBox Widget"""
    DEFAULT_CSS = """
        
        ImageBox{
            height: 100%;
            &:inline {
                border: none;
            }
        }
    """

    def __init__(self, image_path: Path):
        super().__init__()
        self.image = Image(image_path)

    def render(self) -> RenderResult:
        return self.image



class MyImageApp(App[None]):

    TITLE = "App the shows an image in the terminal"
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self):
        
        yield Header()
        yield ImageBox(Path("data/world_champions.jpg"))
        yield Footer()
  

if __name__ == "__main__":
    app = MyImageApp()
    app.run()
