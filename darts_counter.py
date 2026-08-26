def points_scored():
    points = int(input("How many points did you score with your 3 darts? "))

    if points > 180:
        print("Invalid! You cannot score more than 180 with 3 darts.")
        return None

    elif points == 179:
        print("Invalid! 179 cannot be scored with 3 darts.")
        return None

    return points


score = 501
darts_thrown = 0

while True:

    original_score = score

    points = points_scored()

    if points is None:
        continue

    score -= points
    darts_thrown += 3

    print(f"\nRemaining score: {score}")
    print(f"Total darts thrown: {darts_thrown}")

    if score == 0:
        print("\nGame shot and the match!")
        break

    elif score < 0:
        print("\nOh no, you have busted!")
        score = original_score
        print(f"Score restored to {score}.")