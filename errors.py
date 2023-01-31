import sys
from datetime import datetime
import time
import calendar

def bad_request(details):
    return {
        "error": "An unexpected error has occurred",
        "details": details
    }


def exit_code(msg: str, code: int):
    print(msg)
    sys.exit(code)

def write_log(details):
    with open("logs/log_error.log", "a", encoding="utf-8") as file:
        file.write(
            f"{datetime.fromtimestamp(calendar.timegm(time.gmtime()))}: {details}\n")