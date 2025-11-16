from zxcvbn import zxcvbn  # type: ignore

def check_password(password):
    if password == "":
        return None
    results = zxcvbn(password)
    message = (
    f'On a scale from 0-4, the strength of your password is {results["score"]}. '
    f'Cracking your password with an online ratelimit (100 attempts per hour) would take '
    f'an estimated time of {results["crack_times_display"]["online_throttling_100_per_hour"]}, '
    f'and without an online ratelimit (10 attempts per second) would take '
    f'{results["crack_times_display"]["online_no_throttling_10_per_second"]}. '
    f'{results["feedback"]["warning"]}'
)
    return message
    

