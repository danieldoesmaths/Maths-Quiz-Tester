def points_scored(dart):
    points = int(input(f"How many points did you score with dart {dart}? "))

    if points > 60:
        print("Invalid! You cannot score more than 60 with one dart.")
        return None

    return points


score = 501
darts_thrown = 0

print("Welcome to the Dart Counter!")
print(f"\nYour starting score is {score}")

while True:

    original_score = score
    turn_score = 0

    print("\nNew turn!")

    for dart in range(1, 4):

        points = points_scored(dart)

        while points is None:
            points = points_scored(dart)

        turn_score += points
        darts_thrown += 1

        score_after_dart = original_score - turn_score

        print(f"Score after dart {dart}: {score_after_dart}")

        if score_after_dart == 0:
            score = 0
            print("\nGame shot and the match!")
            break

        elif score_after_dart < 0:
            print("\nOh no, you have busted!")
            score = original_score
            print(f"Score restored to {score}")
            break

    else:
        score = original_score - turn_score

    if score == 0:
        break


print("\n========== FINAL STATS ==========")
print(f"Final Score: {score}")
print(f"Total Darts Thrown: {darts_thrown}")
print("=================================") 