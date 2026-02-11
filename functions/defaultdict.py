# Defaultdict in python
# They are used to provide default values for missing keys
# They are similar to regular dictionaries, but they have a default value for missing keys
# They are imported from the collections module


from collections import defaultdict

def findWinners(matches):
    loss_count = defaultdict(int)  # it will assign a default value of 0 to any key that is not present in the dictionary
    players = set()   # it will assign a default value of an empty set to any key that is not present in the dictionary
 
    for winner, loser in matches:
        players.add(winner)
        players.add(loser)
        loss_count[loser] += 1

    zero_losses = []
    one_loss = []

    for player in players:
        if loss_count[player] == 0:
            zero_losses.append(player)
        elif loss_count[player] == 1:
            one_loss.append(player)

    zero_losses.sort()
    one_loss.sort()

    return [zero_losses, one_loss]

