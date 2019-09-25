import inquirer
from readchar import key
from inquirer.render.console import List as ListRender


class PathRender(ListRender):
    current: int

    def process_input(self, pressed: str) -> None:
        question = self.question
        if pressed == "k":
            if question.carousel and self.current == 0:
                self.current = len(question.choices) - 1
            else:
                self.current = max(0, self.current - 1)
            return
        if pressed == "j":
            if question.carousel and self.current == len(question.choices) - 1:
                self.current = 0
            else:
                self.current = min(
                    len(self.question.choices) - 1, self.current + 1
                )
            return
        if pressed == key.ENTER:
            value = self.question.choices[self.current]
            raise inquirer.errors.EndOfInput(getattr(value, "value", value))

        if pressed == key.CTRL_C:
            raise KeyboardInterrupt()

        for index, choice in enumerate(question.choices):
            mark = choice.split("|")[0]
            if mark == pressed:
                value = self.question.choices[index]
                raise inquirer.errors.EndOfInput(
                    getattr(value, "value", value)
                )
