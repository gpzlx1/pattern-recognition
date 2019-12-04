input1 = "aababaaababaaa"
input2 = "ababaababaaba"


def judge(input : str):
    S = 0
    B = 1
    acc = 2
    status = S
    for char in input:
        if status == S:
            if char == "a":
                status = B
            else:
                return False
        elif status == B or status == acc:
            if char == "a":
                status = acc
            elif char == "b":
                status = S
            else:
                return False
        else:
            return False
    if status == acc:
        return True
    else:
        return False

if __name__ == "__main__":
    print(judge(input1))
    print(judge(input2))