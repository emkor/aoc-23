import dataclasses
import typing

from aoc23.util import input_lines

COLORS = ('red', 'green', 'blue')


@dataclasses.dataclass
class GameSession:
    reds: int = dataclasses.field(default=0)
    greens: int = dataclasses.field(default=0)
    blues: int = dataclasses.field(default=0)

    def add(self, c: str, v: int) -> None:
        if c == 'red':
            self.reds += v
        elif c == 'green':
            self.greens += v
        elif c == 'blue':
            self.blues += v
        else:
            raise ValueError(f'Unexepcted cube color: {c} with value {v}')

    def __str__(self):
        return f"Session(reds={self.reds}, greens={self.greens}, blues={self.blues})"

    def could_be_played(self, req: 'GameSession') -> bool:
        return self.blues <= req.blues and self.greens <= req.greens and self.reds <= req.reds

    def power(self) -> int:
        return self.blues * self.greens * self.reds


@dataclasses.dataclass
class Game:
    ix: int
    sessions: list[GameSession] = dataclasses.field(default_factory=list)

    def add_session(self, s: GameSession):
        self.sessions.append(s)

    def can_be_played(self, req: GameSession) -> bool:
        return all((s.could_be_played(req=req) for s in self.sessions))

    def min_req_cubes(self) -> GameSession:
        return GameSession(reds=max((s.reds for s in self.sessions)),
                           greens=max((s.greens for s in self.sessions)),
                           blues=max((s.blues for s in self.sessions)))

    def __str__(self):
        return f"Game({str(self.sessions)})"


def parse_session(session_text: str) -> GameSession:
    session = GameSession()
    for cube_word in (w.strip() for w in session_text.split(",")):
        for c in COLORS:
            if cube_word.find(c) != -1:
                words = cube_word.split(" ")
                session.add(c, int(words[0]))
                break
    return session


def parse_game_line(line: str) -> Game:
    game_id, game_details = line.split(":")
    game_id = int(game_id.split()[1].strip())
    game_sessions = game_details.split(";")
    sessions = [parse_session(s.strip()) for s in game_sessions]
    return Game(ix=game_id, sessions=sessions)


def day_02_pt1_answer(lines: typing.Iterable[str], req: GameSession) -> int:
    sum_ix = 0
    for l in lines:
        game = parse_game_line(l)
        if game.can_be_played(req=req):
            sum_ix += game.ix
    return sum_ix


def day_02_pt2_answer(lines: typing.Iterable[str]) -> int:
    games = [parse_game_line(l) for l in lines]
    return sum([g.min_req_cubes().power() for g in games])


if __name__ == '__main__':
    day02pt1_answer = day_02_pt1_answer(lines=input_lines('input/day_02_cubes.txt'),
                                        req=GameSession(reds=12, greens=13, blues=14))
    print(f"Day 02 pt1 answer is: {day02pt1_answer}")
    day02pt2_answer = day_02_pt2_answer(lines=input_lines('input/day_02_cubes.txt'))
    print(f"Day 02 pt2 answer is: {day02pt2_answer}")
