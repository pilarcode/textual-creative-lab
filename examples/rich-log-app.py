import csv
import io

from rich.syntax import Syntax
from textual import events
from textual.app import App, ComposeResult
from textual.widgets import RichLog
from textual.widgets import Footer, Header


CODE = '''\
def loop_first_last(values: Iterable[T]) -> Iterable[tuple[bool, bool, T]]:
    """Iterate and generate a tuple with a flag for first and last value."""
    iter_values = iter(values)
    try:
        previous_value = next(iter_values)
    except StopIteration:
        return
    first = True
    for value in iter_values:
        yield first, False, previous_value
        first = False
        previous_value = value
    yield first, True, previous_value\
'''


class RichLogApp(App):
    BINDINGS = [
        ("q", "quit", "Quit"),
    ]
    def compose(self) -> ComposeResult:
        yield Header()
        yield RichLog(highlight=True, markup=True)
        yield Footer()

    def on_ready(self) -> None:
        """Called  when the DOM is ready."""
        text_log = self.query_one(RichLog)
        text_log.write(Syntax(CODE, "python", indent_guides=True))

    
    def on_key(self, event: events.Key) -> None:
        """Write Key events to log."""
        text_log = self.query_one(RichLog)
        text_log.write(event)


if __name__ == "__main__":
    app = RichLogApp()
    app.run()