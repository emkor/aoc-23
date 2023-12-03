import fileinput
import typing
from os import path

PROJ_NAME = "aoc-23"


def proj_path(rel_to_proj: str) -> str:
    dir_path = path.realpath(__file__).rpartition(PROJ_NAME)
    return path.join(dir_path[0], dir_path[1], rel_to_proj)


def input_lines(rel_path: str, encoding: str = "utf-8") -> typing.Iterable[str]:
    for line in fileinput.input(files=proj_path(rel_path), encoding=encoding):
        if line.strip():  # eliminate empty newline at the end
            yield line.strip()
