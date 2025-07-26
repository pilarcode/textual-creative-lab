from rich_pixels import Pixels
from rich.console import Console

console = Console()
pixels = Pixels.from_image_path("../images/panda.png")
console.print(pixels)