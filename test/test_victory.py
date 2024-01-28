from moduls.victory import random, end_game, input_n, input_date, Man


def test_random():
    assert len(random(5)) == 5
    assert len(random(7)) == 7
    assert isinstance(random(10), dict)


def test_end_game(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'да')
    assert not end_game()

    monkeypatch.setattr('builtins.input', lambda _: 'Да')
    assert not end_game()

    monkeypatch.setattr('builtins.input', lambda _: 'НЕТ')
    assert end_game()

    monkeypatch.setattr('builtins.input', lambda _: 'нет')
    assert end_game()


def test_input_n(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '10')
    assert input_n() == 10


def test_input_date(monkeypatch):
    person = Man(name='Lao', data=[10, 12, 1245])
    monkeypatch.setattr('builtins.input', lambda _: '10.12.1245')
    assert input_date(person) == [10, 12, 1245]


def test_check():
    person = Man(name='Lao', data=[10, 12, 1245])
    assert person.check([1245, 12, 10])
