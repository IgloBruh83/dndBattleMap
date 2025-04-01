from random import randint

def Roll(rollcode='1d20', mod=None):
    if mod != 0 and mod is not None:
        rolls = [Roll(rollcode, mod=0), Roll(rollcode, mod=0)]
        print(f"Raw: [{rolls[0]}] [{rolls[1]}]")
        print(f"Final: {min(rolls) if mod == -1 else max(rolls)}")
        return min(rolls) if mod == -1 else max(rolls)
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
    if mod is None:
        print(f"Final: {result}")
    return result