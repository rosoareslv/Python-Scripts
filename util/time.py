from datetime import datetime
import time


def get_current_timestamp():
    return int(time.time())


def get_current_time_miliseconds():
    return time.time() * 1000


def get_current_datetime():
    return str(
        datetime.now(tz=datetime.now().astimezone().tzinfo).isoformat(
            timespec="milliseconds"
        )
    )


def convert_datetime_to_timestamp(timestamp: str, datetime_format: str):
    dt = datetime.strptime(timestamp, datetime_format)
    return dt.timestamp()


def check_end_date_time(
    start_date_time: str,
    end_date_time: str,
    datetime_format: str = "%Y-%m-%dT%H:%M:%S.%f%z",
):
    if convert_datetime_to_timestamp(
        start_date_time, datetime_format
    ) <= get_current_timestamp() and (
        end_date_time is None
        or end_date_time.startswith("9999")
        or convert_datetime_to_timestamp(end_date_time, datetime_format)
        > get_current_timestamp()
    ):
        return True
    return False
