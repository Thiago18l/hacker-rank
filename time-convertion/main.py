def timeConversion(s: str) -> None:
    time = s.split(":")

    if s[-2:] == "AM" and int(time[0]) != 12:
        time[0] = str(int(time[0]) + 12)
    else:
        time[0] = "00" if int(time[0]) == 12 else time[0]
    time_result = ":".join(time)
    print(time_result[:-2])


timeConversion("12:45:54PM")
