import re

global code
global status


def expand(string: str) -> str:
    def replace(match):
        word = match.group(1)
        return str(globals().get(word))

    return re.sub(r"\$\$(?<word>\w+)\$\$", replace, string)


code = "Code"
status = "great"

print(expand(f"{code} is {status} isn't it?"))
