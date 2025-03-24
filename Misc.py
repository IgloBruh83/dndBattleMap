from random import randint

def Roll(rollcode='1d20'):
    parts = list(rollcode.split("+"))
    result = 0
    for _ in parts:
        if "d" in _:
            temp = _.split("d"); subresult = 0
            for i in range(int(temp[0])):
                subresult += randint(1, int(temp[1]))
        else:
            subresult = int(_)
        result += subresult
    return result
