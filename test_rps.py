import rps
import pytest

def test_rock_is_a_valid_play():
    assert rps.is_valid_play('rock') is True

def test_paper_is_a_valid_play():
    assert rps.is_valid_play('paper') is True

def test_scissors_is_a_valid_play():
    assert rps.is_valid_play('scissors') is True

def test_spock_is_a_valid_play():
    assert rps.is_valid_play('spock') is False

def test_random_play_is_always_valid():
    for _ in range(1000):
        assert rps.is_valid_play(rps.random_play())

def test_random_play_is_fair():
    plays = {
        'rock': 0,
        'paper': 0,
        'scissors': 0
    }
    for _ in range(10000):
        play = rps.random_play()
        plays[play] += 1

    for value in plays.values():
        assert value > 3000

@pytest.mark.parametrize('play', ['rock', 'paper', 'scissors'])
def test_same_is_tie(play):
    assert rps.determine_game_result(play, play) == 'tie'

@pytest.mark.parametrize('human, computer',
                        [('rock', 'scissors'),
                         ('paper', 'rock'),
                         ('scissors', 'paper')])
def test_human_wins(human, computer):
    assert rps.determine_game_result(human, computer) == 'human'
