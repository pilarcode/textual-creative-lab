from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, Digits, Footer, Header,Static
from textual_plotext import PlotextPlot, Plot
from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup
from textual.widgets import Placeholder
from textual_imageview import img
from pathlib import Path
from PIL import Image
import math
from textual.app import RenderResult
from textual import events
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from textual.widget import Widget




class ImageViewer(Widget):
    DEFAULT_CSS = """
    ImageViewer{
        height: 100%;
    }
    """

    def __init__(self, image: Image.Image):
        super().__init__()
        if not isinstance(image, Image.Image):
            raise TypeError(
                f"Expected PIL Image, but received '{type(image).__name__}' instead."
            )

        self.image = img.ImageView(image)
        self.mouse_down = False
    
    def on_show(self):
        w, h = self.size.width, self.size.height
        img_w, img_h = self.image.size

        # Compute zoom such that image fits in container
        zoom_w = math.log(max(w, 1) / img_w, self.image.ZOOM_RATE)
        zoom_h = math.log((max(h, 1) * 2) / img_h, self.image.ZOOM_RATE)
        zoom = max(0, math.ceil(max(zoom_w, zoom_h)))
        self.image.set_zoom(zoom)

        # Position image in center of container
        img_w, img_h = self.image.zoomed_size
        self.image.origin_position = (-round((w - img_w) / 2), -round(h - img_h / 2))
        self.image.set_container_size(w, h, maintain_center=False)

        self.refresh()
    
    def render(self) -> RenderResult:
        return self.image
    
    def on_resize(self, event: events.Resize):
        self.image.set_container_size(event.size.width, event.size.height)
        self.refresh()


class Box(Placeholder):
    """Example widget."""

    DEFAULT_CSS = """
    Box {
        width: 16;
        height: 8;        
    }
    """


class ContainerApp(App):
    """Simple app to play with containers."""

    CSS = """
      Screen {
        align: center middle;
        &:inline {
            border: none;
        }
    }
    .with-border {
        border: heavy red;
    }

    .box-background {
        color: white;
        border: none;
        margin: 1;
    }

    """
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]


    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(" ⚽")
        with HorizontalGroup(classes="with-border"):
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
        with HorizontalGroup(classes="with-border"):
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
        with HorizontalGroup(classes="with-border"):
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
            yield Box(classes="box-background")
        yield Footer()

if __name__ == "__main__":
    app = ContainerApp()
    app.run()