from datetime import datetime, timedelta


def subtract_five_days():
    # Subtract 5 days from current date/time
    return datetime.now() - timedelta(days=5)


def get_yesterday_today_tomorrow():
    # Return yesterday, today, and tomorrow dates
    today = datetime.now().date()
    return today - timedelta(days=1), today, today + timedelta(days=1)


def drop_microseconds(dt):
    # Remove microseconds from a datetime object
    return dt.replace(microsecond=0)


def date_difference_in_seconds(date1, date2):
    # Calculate absolute difference between two dates in seconds
    return abs((date2 - date1).total_seconds())


if __name__ == "__main__":
    print("1) Current datetime - 5 days:", subtract_five_days())

    yesterday, today, tomorrow = get_yesterday_today_tomorrow()
    print("2) Yesterday:", yesterday)
    print("   Today:    ", today)
    print("   Tomorrow: ", tomorrow)

    now = datetime.now()
    print("3) Original datetime:      ", now)
    print("   Without microseconds:   ", drop_microseconds(now))

    d1 = datetime(2026, 4, 10, 12, 0, 0)
    d2 = datetime(2026, 4, 17, 15, 30, 0)
    print("4) Date difference (sec):", date_difference_in_seconds(d1, d2))