import unittest

from aoc23.day_01_01 import day_01_pt1_parse_calibration_value, day_01_pt1_calibration_sum, \
    day_01_pt2_parse_valibartion_value, day_01_pt2_calibration_sum
from aoc23.day_02_01 import parse_session, GameSession, parse_game_line, Game, day_02_pt1_answer


class TestAocDay02Tests(unittest.TestCase):

    def test_day_02_pt1_should_parse_game_session(self):
        assert parse_session("5 green, 1 blue, 3 red") == GameSession(reds=3, greens=5, blues=1)
        assert parse_session("8 green, 15 red") == GameSession(reds=15, greens=8, blues=0)
        assert parse_session("2 green, 3 red, 14 blue") == GameSession(reds=3, greens=2, blues=14)

    def test_day_02_pt1_parse_game(self):
        actual_game = parse_game_line(
            "Game 6: 5 green, 1 blue, 3 red; 8 green, 15 red; 16 green, 5 red, 1 blue")
        expect_game = Game(ix=6, sessions=[GameSession(greens=5, blues=1, reds=3), GameSession(greens=8, reds=15),
                                           GameSession(greens=16, blues=1, reds=5), ])
        assert actual_game == expect_game

    def test_day_02_pt1_session_can_by_played(self):
        req = GameSession(reds=12, greens=13, blues=14)
        assert parse_session("3 blue, 4 red").could_be_played(req) is True
        assert parse_session("1 red, 2 green, 6 blue").could_be_played(req) is True
        assert parse_session("2 green").could_be_played(req) is True
        assert parse_session("8 green, 6 blue, 20 red").could_be_played(req) is False
        assert parse_session("3 green, 15 blue, 14 red").could_be_played(req) is False

    def test_day_02_pt1_game_can_be_played(self):
        req = GameSession(reds=12, greens=13, blues=14)
        assert parse_game_line("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green").can_be_played(req) is True
        assert parse_game_line("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue").can_be_played(req) is True
        assert parse_game_line("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red").can_be_played(req) is False
        assert parse_game_line("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red").can_be_played(req) is False
        assert parse_game_line("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green").can_be_played(req) is True

    def test_day_02_pt1_answer(self):
        req = GameSession(reds=12, greens=13, blues=14)
        actual_answer = day_02_pt1_answer(lines=[
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ], req=req)
        assert actual_answer == 8
