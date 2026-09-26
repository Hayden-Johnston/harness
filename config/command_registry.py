import inspect
from typing import Callable, Any
from pathlib import Path
from dataclasses import dataclass
from config import commands

@dataclass
class Command:
    name: str
    handler: Callable
    help: str

class CommandRegistry:

    def __init__(self):
        self.cmds = self.load_commands()

    def load_commands(self):
        c = {}
        module = commands
        for name, func in inspect.getmembers(module, inspect.isfunction):
            if not name.startswith("_"):
                doc = inspect.getdoc(func) or "No description provided."
                cmd_name = f"{name}"
                c[cmd_name] = Command(cmd_name, func, doc)
        return c

    def get_cmds(self):
        return self.cmds

if __name__ == "__main__":
    c = CommandRegistry()
    print(c.get_cmds())