from rich_pixels import Pixels
from rich.console import Console

console = Console()
pixels = Pixels.from_image_path("data/cat.png")
console.print(pixels)