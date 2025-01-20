# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    play_order = {}
    n = 4  

    if len(opponent_history) > n:
        for i in range(len(opponent_history) - n):
            seq = ''.join(opponent_history[i:i+n])
            next_move = opponent_history[i+n]
            if seq not in play_order:
                play_order[seq] = {'R': 0, 'P': 0, 'S': 0}
            play_order[seq][next_move] += 1

        recent_sequence = ''.join(opponent_history[-n:])
        
        if recent_sequence in play_order:
            prediction = max(play_order[recent_sequence], key=play_order[recent_sequence].get)
        else:
            move_counts = {'R': 0, 'P': 0, 'S': 0}
            for move in opponent_history:
                move_counts[move] += 1
            prediction = max(move_counts, key=move_counts.get)
    else:
        prediction = 'R'

    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
    return counter_moves[prediction]
