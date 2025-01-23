def control(state,player):
    x, y, vx, vy, a, p1, p2 = state
    # Simple logic to move the pad based on the ball's position
    if abs(x - (p1 if player==1 else p2)) < 5:
        return 0
    elif x > (p1 if player==1 else p2):
        return 1  # Move right
    elif x < (p1 if player==1 else p2):
        return -1  # Move left
    
def control_s(state,player):
    return 1