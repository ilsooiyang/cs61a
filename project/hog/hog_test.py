from hog import *

m = 0
nr = 0

def repeat_swap():
    highest_nr = 0
    highest_rate = 0
    for nr in range(1,11):
        rate = average_win_rate(swap_strategee)
        if rate > highest_rate:
	          highest_rate, highest_nr = rate, nr
    return highest_rate, highest_nr
    
def repeat_final():
    highest_m = 0
    highest_nr = 0
    highest_rate = 0
    for m in range(1,11):
        for nr in range(1,11):
            print('m:{0} nr:{1}'.format(m, nr))
            rate = average_win_rate(final_strategee)
            if rate > highest_rate:
                highest_rate, highest_m, highest_nr = rate, m, nr
            print('highest_rate:{0}'.format(highest_rate))
    return highest_rate, highest_m, highest_nr

def final_strategee(score, opponent_score, margin=m, num_rolls=nr):
    """Try to find out which margin/num_rolls produces highest win rate for bacon/swap.
    Then write it out as conditional.
    """
    # BEGIN Question 10
    winning = score > opponent_score
    about_to_win = GOAL_SCORE - score <= margin
    swap_score = new_score_roll_zero(score, opponent_score)
    plus_one = largest_digit_plus_one(opponent_score)

    if is_swap(swap_score, opponent_score) and opponent_score < swap_score:
        return num_rolls
    if is_swap(swap_score, opponent_score) and opponent_score > swap_score:
        return 0
    if plus_one >= margin:
        return 0
    if is_prime(plus_one) and next_prime(plus_one) >= margin:
        return 0
    if about_to_win:
        return 0
    else:
        return num_rolls


def bacon_strategee(score, opponent_score, margin=m, num_rolls=nr):
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

def swap_strategee(score, opponent_score, num_rolls=nr):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 9
    score_new = new_score(score, opponent_score)
    if is_swap(score_new, opponent_score) and opponent_score > score_new:
        return 0
    else:
        return num_rolls