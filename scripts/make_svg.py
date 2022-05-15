#!.venv/bin/python3.10

"""
Run:

python3.10 -m venv .venv && \
    source .venv/bin/activate && \
    pip install rich

"""

from rich.console import Console
from rich.terminal_theme import TerminalTheme

console = Console(record=True)

CUSTOM_MONOKAI = TerminalTheme(
    (16, 16, 16),
    (217, 217, 217),
    [
        (26, 26, 26),
        (244, 0, 95),
        (152, 224, 36),
        (253, 151, 31),
        (157, 101, 255),
        (244, 0, 95),
        (88, 209, 235),
        (196, 197, 181),
        (98, 94, 76),
    ],
    [
        (244, 0, 95),
        (152, 224, 36),
        (224, 213, 97),
        (157, 101, 255),
        (244, 0, 95),
        (88, 209, 235),
        (246, 246, 239),
    ],
)

console.print(
    {
        "status": "ok",
        "statusCode": 200,
        "containerIP": "219.20.128.1",
        "message": "Hello world from container 1",
    },
    justify="center",
    style="",
)

console.save_svg("art/logo.svg", title="http://foo.localhost", theme=CUSTOM_MONOKAI)
