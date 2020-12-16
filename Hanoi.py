def HanoiTowers(n):
    # O(2^n)
    print(f"Total number of moves is {Hanoi_towers(n, 1, 3)}")


def Hanoi_towers(n, fromPeg, toPeg):
    if n == 1:
        print(f"Move disk from {fromPeg} to {toPeg}")
        return 1
    unusedPeg = 6 - fromPeg - toPeg
    move_1 = Hanoi_towers(n-1, fromPeg, unusedPeg)
    print(f"Move disk from {fromPeg} to {toPeg}")
    move_2 = Hanoi_towers(n-1, unusedPeg, toPeg)
    return move_1+move_2+1


HanoiTowers(15)
