#!/usr/bin/env python3


def read_input(file: str):
    with open(file, 'r') as input:
        raw_input = [x.strip() for x in input.readlines()]

    clean_data = []
    for game_str in raw_input:
        game, turns_raw = game_str.split(':')
        game_id = game.split(' ')[1]
        turns = [x.strip() for x in turns_raw.split(';')]

        for t in turns:
            choices = t.split(', ')
            choice_dict = {'game_id': int(game_id)}
            for c in choices:
                number, color = c.split(' ')
                choice_dict[color] = int(number)
            clean_data.append(choice_dict)
    return clean_data


def main():
    inputs = read_input('02.input')

    # part 1
    max_colors = (('blue', 14),  ('red', 12),  ('green',  13))
    all_games = {x.get('game_id') for x in inputs}
    not_possible_games = set()
    for color, draw_max in max_colors:
        t = {turn.get('game_id') for turn in inputs if turn.get(color)
             is not None and turn.get(color) > draw_max}
        not_possible_games.update(t)
    possible_games = all_games.difference(not_possible_games)
    print('Part 1:', sum(list(possible_games)))

    # part 2
    games = {}
    for turn in inputs:
        game_id = int(turn.get('game_id'))
        if games.get(game_id) is None:
            games[game_id] = {}
        for color in ('blue', 'red', 'green'):
            if (existing_max := games[game_id].get(color)) is None:
                games[game_id][color] = (existing_max := 0)

            if (new_max := turn.get(color)) is not None and existing_max < new_max:
                games[game_id][color] = new_max

    lin = [games[id].get('red')*games[id].get('blue')*games[id].get('green')
           for id in games.keys()]
    print('Part 2:', sum(list(lin)))


if __name__ == '__main__':
    main()
