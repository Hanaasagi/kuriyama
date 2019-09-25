from .render import PathRender
from inquirer.render.console import ConsoleRender
from inquirer.render.console.base import BaseConsoleRender


class CustomConsoleRender(ConsoleRender):
    def render_factory(self, question_type: str) -> BaseConsoleRender:
        if question_type == "pathlist":
            return PathRender
        return super().render_factory(question_type)

    def _print_header(self, render: BaseConsoleRender) -> None:
        """no header"""
