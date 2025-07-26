from datetime import datetime

from textual.app import App, ComposeResult
from textual.widgets import Digits
from textual.widgets import Header, Footer


class ClockApp(App):
    CSS = """
    Screen {
        align: center middle;
        &:inline {
            border: none;
            height: 50vh;
            Digits {
                color: $success;
            }
        }
    }
    #clock {
        width: auto;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Digits("", id="clock")
        yield Footer()

    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now().time()
        self.query_one(Digits).update(f"{clock:%T}")


if __name__ == "__main__":
    #Most apps will not require modification to run inline, but if you want to tweak the height and border you can write CSS that targets inline mode with the :inline pseudo-selector.
    app = ClockApp()
    app.run(inline=True)