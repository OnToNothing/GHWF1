
def compute_hw_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def compute_hw_min(grades):
    if len(grades) == 0:
        return 0
    return min(grades)