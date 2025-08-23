from datetime import datetime, timedelta

def add_gigasecond(birth_date=datetime.now()):
    return birth_date + timedelta(seconds=pow(10, 9))
