from rich.console import Console
from textual_image.renderable import Image


console = Console()
console.print(Image("./data/cat.png"))
