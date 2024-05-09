import re


def match_date(date: str) -> None:
    pattern = r"[0-9]{2}\/[0-9]{2}\/[0-9]{4}"
    match = re.match(pattern, date)
    if match:
        print(match.group(0))
    else:
        print("Invalid date")


match_date("18/12/1997")
