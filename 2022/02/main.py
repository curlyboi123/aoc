import sys

ACTION_VALUES = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

RESULT_VALUES = {
    "loss": 0,
    "draw": 3,
    "win": 6,
}

WIN_RESPONSES = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

LOSS_RESPONSES = {v: k for k, v in WIN_RESPONSES.items()}


def round_calculator(self_action: str, opponent_action: str) -> int:
    """A function to calculate the points gained by player 1 in a round of rock, paper, scissors

    :param self_action: The action that self chooses
    :type self_action: str
    :param opponent_action: The action that opponent chooses
    :type opponent_action: str
    :returns: an int representing the number of points gained by self in that round
    :rtype: int
    """
    valid_actions = {"rock", "paper", "scissors"}
    if self_action not in valid_actions or opponent_action not in valid_actions:
        raise ValueError(f"Invalid player action: action must be one of {valid_actions}")

    points_won = 0  # This could cause issues where calls to function that don't match any condition appear to be a draw
    # Draw
    if self_action == opponent_action:
        points_won = 3
    # p1 loss
    elif self_action == WIN_RESPONSES[opponent_action]:
        points_won = 6
    # p1 win
    elif self_action == LOSS_RESPONSES[opponent_action]:
        points_won = 0
    return points_won


def action_calculator(opponent_action: str, desired_result: str) -> str:
    """A function to calculate the decision self should use to beat the opponent in a game of rock, paper, scissors

    :param opponent_action: The action that the opponent has chosen
    :type opponent_action: str
    :param desired_result: The desired result in the round
    :type desired_result: str
    :returns: a string representing the action the player should choose to beat the opponent
    :rtype: str
    """
    valid_actions = {"rock", "paper", "scissors"}
    if opponent_action not in valid_actions:
        raise ValueError(f"Invalid opponent action: action must be one of {valid_actions}")
    valid_results = {"win", "loss", "draw"}
    if desired_result not in valid_results:
        raise ValueError(f"Invalid desired result: action must be one of {valid_results}")

    player_action = ""
    if desired_result == "draw":
        player_action = opponent_action
    elif desired_result == "win":
        player_action = WIN_RESPONSES[opponent_action]
    elif desired_result == "loss":
        player_action = LOSS_RESPONSES[opponent_action]
    return player_action


def challenge_one(round_actions: list):
    action_mapping = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    self_points = 0
    for actions in round_actions:
        opponent_action = action_mapping[actions[0]]
        self_action = action_mapping[actions[1]]
        result_points = round_calculator(self_action, opponent_action)
        action_points = ACTION_VALUES[self_action]
        self_points += result_points + action_points
    return self_points


def challenge_two(round_actions: list):
    action_mapping = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "loss",
        "Y": "draw",
        "Z": "win",
    }

    self_points = 0
    for actions in round_actions:
        opponent_action = action_mapping[actions[0]]
        desired_result = action_mapping[actions[1]]
        self_action = action_calculator(opponent_action, desired_result)
        self_points += ACTION_VALUES[self_action] + RESULT_VALUES[desired_result]

    return self_points


def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        content = f.readlines()
    round_actions = [line.strip().split(" ") for line in content]

    challenge_one_result = challenge_one(round_actions)
    print(challenge_one_result)
    challenge_two_result = challenge_two(round_actions)
    print(challenge_two_result)


if __name__ == "__main__":
    main()
