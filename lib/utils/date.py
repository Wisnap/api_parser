from datetime import datetime


class OzonDateParser:
    def __init__(self, date):
        self.date = date

    def stringify_date_for_analytics(self):
        return self.date.strftime('%Y-%m-%d')


def stringify_datetime(datetime):
    return datetime.strftime('%Y-%m-%d %H-%M-%S')


def is_date_valid(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
