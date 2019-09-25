import os
import random
import inquirer
import string
from inquirer import themes
from .console import CustomConsoleRender

from typing import List


def get_quick_marks(ignore: List[str], shuffle: bool = True) -> List[str]:
    res = list(string.ascii_lowercase)
    for c in ignore:
        res.remove(c)
    if shuffle:
        random.shuffle(res)
    return res


def get_cache_dir() -> str:
    base_dir = os.getenv("XDG_CACHE_HOME")
    if base_dir is None:
        user_home = os.path.expanduser("~")
        base_dir = os.path.join(user_home, ".cache")
    return os.path.join(base_dir, "kuriyama")


def read_recent_dirs() -> List[str]:
    cache_dir = get_cache_dir()
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    cache_file = os.path.join(cache_dir, "buffer")
    with open(cache_file, "r") as f:
        return f.read().strip().split(" ")


class Path(inquirer.questions.List):
    kind = "pathlist"


def main():
    choices = map(
        lambda c: "| ".join(c),
        zip(get_quick_marks(["j", "k"]), read_recent_dirs()[:20]),
    )
    questions = [
        Path("path", message="", choices=list(choices), carousel=True)
    ]
    answers = inquirer.prompt(
        questions, render=CustomConsoleRender(theme=themes.Default())
    )
    if answers is None:
        return
    cache_dir = get_cache_dir()
    target_file = os.path.join(cache_dir, "target")
    with open(target_file, "w") as f:
        f.write(os.path.expanduser(answers["path"].split("| ")[-1]))
