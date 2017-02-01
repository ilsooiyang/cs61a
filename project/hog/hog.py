"""The Game of Hog."""
from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 0.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    r, total = 1, 0
    rolled_1 = False
    while num_rolls >= r:
        rolled = dice()
        if rolled == 1:
            rolled_1 = True
        else:
            total += rolled
        r += 1
    if rolled_1:
        return 0
    else:
        return total 
    # END Question 1

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while n > i:
        if n % i == 0:
            return False
        i += 1
    return True

def next_prime(n):
    i = 1
    while not is_prime(n + i):
        i += 1
    return n + i   

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    total = 0
    if num_rolls >= 1:
        total = roll_dice(num_rolls, dice)
    if num_rolls == 0:
        total = max(list(map(int,str(opponent_score)))) + 1
    if is_prime(total):
        return next_prime(total)
    return total
    # END Question 2


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if (score + opponent_score) % 7 == 0:
        return four_sided
    else:
        return six_sided
    # END Question 3


def is_swap(score0, score1):
    """Returns whether the last two digits of SCORE0 and SCORE1 are reversed
    versions of each other, such as 19 and 91.
    """
    # BEGIN Question 4
    scores = [score0, score1]
    new_scores = []
    for score in scores:
        score = [int(n) for n in str(score)] #score is now a list [9,1]
        if len(score) == 1:
            score.insert(0, 0)
        elif len(score) == 3:
            score.pop(0)
        for n in score:
            new_scores.append(n)
    if new_scores[0] == new_scores[3] and new_scores[1] == new_scores[2]:
        return True
    else:
        return False

    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def finish(score0, score1, goal):
    return score0 >= goal or score1 >= goal

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and 
    returns a number of dice 
    that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    #################################################################################################
    # who_is_0 = {"score": score0, "strategy": strategy0(score0, score1)}
    # who_is_1 = {"score": score1, "strategy": strategy1(score1, score0)}
    #
    # def my_turn(me, other):
    #     score = take_turn(me["strategy"], other["score"], select_dice(me["score"], other["score"]))
    #     if score == 0:
    #         other["score"] += me["strategy"]
    #     else:
    #        me["score"] += score
    #
    # while not game_over:
    #     if who == 0:
    #         my_turn(who_is_0, who_is_1)
    #     elif who == 1:
    #         my_turn(who_is_1, who_is_0)
    #     if is_swap(score0, score1):
    #         score0, score1 = score1, score0
    #     if finish(score0, score1, goal):
    #         game_over = True
    #     who = other(who)
    # return score0, score1
    #################################################################################################

    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    game_over = False

    while not game_over:
        if who == 0:
            score = take_turn(strategy0(score0, score1), score1, select_dice(score0, score1))
            if score == 0:
                score1 += strategy0(score0, score1)
            else:
                score0 += score
        elif who == 1:
            score = take_turn(strategy1(score1, score0), score0, select_dice(score1, score0))
            if score == 0:
                score0 += strategy1(score1, score0)
            else:
                score1 += score
        if is_swap(score0, score1):
            score0, score1 = score1, score0
        if finish(score0, score1, goal):
            game_over = True
        who = other(who)
    # END Question 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n

    return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    5.5

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 0.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 5.5.
    Note that the last example uses roll_dice so the hogtimus prime rule does
    not apply.
    """
    # BEGIN Question 6
    def averaged(*args):
        total = 0
        for _ in range(num_samples): #run fn num_samples times
            total += fn(*args)
        return total / num_samples

    return averaged
    # END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    total = 0
    max_num_roll = 0
    if make_averaged(roll_dice, num_samples)(1, dice) == 0: #to test if dice == make_test_dice(1)
        return 1
    else:
        for i in range(1,11):
            result = make_averaged(roll_dice, num_samples)(i, dice)
            if result > total:
                total, max_num_roll = result, i
    return max_num_roll

    # END Question 7


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2

def run_experiments():
    """Run a series of strategy experiments and report results."""
    # if True:  # Change to False when done finding max_scoring_num_rolls
    #     six_sided_max = max_scoring_num_rolls(six_sided)
    #     print('Max scoring num rolls for six-sided dice:', six_sided_max)
    #     four_sided_max = max_scoring_num_rolls(four_sided)
    #     print('Max scoring num rolls for four-sided dice:', four_sided_max)

    # if True:  # Change to True to test always_roll(5)
    #     print('always_roll(5) win rate:', average_win_rate(always_roll(5)))

    # if True:  # Change to True to test bacon_strategy
        # print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    # if True:  # Change to True to test swap_strategy
        # print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True:
        print('final_strategy win rate:', average_win_rate(final_strategy))


# If you name a function as plus_one, and then make a variable with the name plus_one
# the function gets overriden by the variable.

# Strategies
def largest_digit_plus_one(opponent_score):
    return max(list(map(int,str(opponent_score)))) + 1

def roll_zero(score, opponent_score):
    plus_one = largest_digit_plus_one(opponent_score)
    if is_prime(plus_one):
        return score + next_prime(plus_one)
    else:
        return score + plus_one

def bacon_strategy(score, opponent_score, margin=7, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    plus_one = largest_digit_plus_one(opponent_score)
    if plus_one >= margin:
        return 0
    elif is_prime(plus_one) and next_prime(plus_one) >= margin:
        return 0
    else:
        return num_rolls
    # END Question 8


def swap_strategy(score, opponent_score, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 9
    swap_score = roll_zero(score, opponent_score)
    if is_swap(swap_score, opponent_score) and opponent_score > swap_score:
        return 0
    else:
        return num_rolls
    # END Question 9


def final_strategy(score, opponent_score, margin=7, num_rolls=4):
    """
    --Swap Strategy--
    When you're losing and can swap scores, swap.
    When you're winning, don't swap.

    --Bacon Strategy--
    When you can score >= 7 by rolling 0, do it.

    Roll 4 otherwise.
    """
    # BEGIN Question 10
    swap_score = roll_zero(score, opponent_score)
    plus_one = largest_digit_plus_one(opponent_score)

    if is_swap(swap_score, opponent_score) and opponent_score < swap_score:
        return num_rolls
    if is_swap(swap_score, opponent_score) and opponent_score > swap_score:
        return 0
    if plus_one >= margin:
        return 0
    if is_prime(plus_one) and next_prime(plus_one) >= margin:
        return 0
    else:
        return num_rolls
    
    # END Question 10

##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
