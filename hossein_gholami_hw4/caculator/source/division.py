def division(number: list):
    result = number[0]

    for i in range(1, len(number)):
        result /= number[i]

    return result


