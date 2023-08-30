from datetime import datetime


def convert_str_to_datatime(
    reservation_date: str | None, hours: str | None, minutes: str | None
) -> datetime:
    time_str = f"{reservation_date} {hours}:{minutes}"
    time_format = "%Y-%m-%d %H:%M"
    time_datatime = datetime.strptime(time_str, time_format)
    return time_datatime
