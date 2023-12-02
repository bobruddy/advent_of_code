#!/usr/bin/env python3


def score(actions) -> tuple:

    their_action, my_action = actions

    who_wins = {"P": "S", "R": "P", "S": "R"}
    action_score = {"S": 3, "R": 1, "P": 2}
    action_map = {"A": "R", "B": "P", "C": "S", "X": "R",
                  "Y": "P", "Z": "S", "R": "R", "P": "P", "S": "S"}
    their_action = action_map.get(their_action)
    my_action = action_map.get(my_action)

    their_score = action_score.get(their_action)
    my_score = action_score.get(my_action)

    # draw
    if their_action == my_action:
        their_score += 3
        my_score += 3
        return ((their_score, my_score))

    if who_wins.get(their_action) == my_action:
        their_score += 0
        my_score += 6
        return ((their_score, my_score))
    else:
        their_score += 6
        my_score += 0
        return ((their_score, my_score))


def read_input(file):
    with open(file, "r") as file:
        return ([tuple(x.strip().split(' ')) for x in file.readlines()])


def get_results(file):
    action_list = read_input(file)
    return list(map(score, action_list))


def my_total_score(file):
    overall_results = get_results(file)
    return (sum([x[1] for x in overall_results]))


raw_input = "02.input"

# part 1
print('Part 1:', my_total_score(raw_input))

# part 2


def figure_my_action(file):
    results = read_input(file)
    who_wins = {"P": "S", "R": "P", "S": "R"}
    possible_actions = who_wins.keys()

    action_map = {"A": "R", "B": "P", "C": "S"}
    action_list = [(action_map.get(theirs), mine) for theirs, mine in results]

    actions = []
    for r in action_list:
        theirs, mine = r
        if mine == 'Y':
            actions.append((theirs, theirs))
        elif mine == 'Z':
            actions.append((theirs, who_wins.get(theirs)))
        else:
            lose_action = list(set(possible_actions) -
                               set((theirs, who_wins.get(theirs))))
            actions.append((theirs, lose_action[0]))

    return (actions)


new_actions = figure_my_action(raw_input)
overall_results_new = list(map(score, new_actions))
print('Part 2:', sum([x[1] for x in overall_results_new]))


# X -> lose
# Y -> draw
# Z -> win
