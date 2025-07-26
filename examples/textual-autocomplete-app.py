from textual.app import App, ComposeResult
from textual.widgets import Input
from textual_autocomplete import AutoComplete, DropdownItem

class ColorFinder(App):
    def compose(self) -> ComposeResult:
        # Create a standard Textual input
        text_input = Input(placeholder="Type a color...")
        yield text_input

        # Add an autocomplete to the same screen, and pass in the input widget.
        yield AutoComplete(
            text_input,  # Target input widget
            candidates=["Red", "Green", "Blue", "Yellow", "Purple", "Orange"]
        )

if __name__ == "__main__":
    app = ColorFinder()
    app.run()