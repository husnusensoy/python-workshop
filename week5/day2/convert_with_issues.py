from typing import List, Union


def convert01(l: List[str]) -> List[Union[int, None]]:
    res = []
    for e in l:
        try:
            ie = int(e)
        except ValueError:
            ie = None

        res.append(ie)

    return res


def convert02(l: List[str]) -> List[Union[int, None]]:
    res = []

    for e in l:
        is_with_sign_integer = e[0] in ["-","+"] and all(c in "0123456789" for c in e[1:])
        is_pos_integer = all(c in "0123456789" for c in e)


        if is_with_sign_integer or is_pos_integer:
            res.append(int(e))
        else:
            res.append(None)

    return res


sample_input = ["1", "1234", "agah", "washingthon", "-1", "+1", "0"]

print(convert01(sample_input))
print(convert02(sample_input))
