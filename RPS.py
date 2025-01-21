# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    plays = {}
    n = 4

    if len(opponent_history) > n:
        for i in range(len(opponent_history) - n):
            second = opponent_history[i + n]
            moves = ''.join(opponent_history[i:(i + n)])

            if moves not in plays:
                plays[moves] = {'R': 0, 'P': 0, 'S': 0}

            plays[moves][second] += 1

        last = ''.join(opponent_history[-n:])
        
        if last in plays:
            prediction = max(plays[last], key=plays[last].get)
        else:
            move_counts = {'R': 0, 'P': 0, 'S': 0}

            for move in opponent_history:
                move_counts[move] += 1

            prediction = max(move_counts, key=move_counts.get)
    else:
        prediction = random.choice(['R', 'P', 'S'])

    reverse = {'R': 'P', 'P': 'S', 'S': 'R'}

    return reverse[prediction]