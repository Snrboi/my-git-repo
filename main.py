def calculate_average(scores: list[float]) -> float:
    total = sum(scores)
    return total / len(scores) if scores else 0.0