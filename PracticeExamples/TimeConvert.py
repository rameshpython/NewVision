class TimeConvert:
    def __init__(self):
        pass

    def convert(self,minutes):
        hours = minutes //60
        remaining_minutes = minutes % 60
        return f"{minutes}minutes = {hours}hours(s) and {remaining_minutes}minutes(s)"