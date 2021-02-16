from collections import defaultdict
def tournamentWinner(competitions, results):
    scores = defaultdict(int)
    curr_max, winner = 0, competitions[0][0]
    for i in range(len(results)):
      competitor = competitions[i][results[i]-1]
      scores[competitor]+=3
      if scores[competitor] >= curr_max:
        curr_max = scores[competitor]
        winner = competitor
    return winner