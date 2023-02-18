def format_duration(sec):
    if sec == 0:
        return "now"
    year = sec // 31536000
    day = sec // 86400
    hour = sec // 3600
    minute, second = divmod(sec, 60)

    if hour > 0:
        minute -= 60 * hour
    if day > 0:
        hour -= 24 * day
    if year > 0:
        day -= 365 * year

    y_format = f"{year} year{'' if year == 1 else 's'}" if year > 0 else ""
    d_format = f"{day} day{'' if day == 1 else 's'}" if day > 0 else ""
    h_format = f"{hour} hour{'' if hour == 1 else 's'}" if hour > 0 else ""
    m_format = f"{minute} minute{'' if minute == 1 else 's'}" if minute > 0 else ""
    s_format = f"{second} second{'' if second == 1 else 's'}" if second > 0 else ""

    return f"{y_format}{', ' if year > 0 else ''}" \
           f"{d_format}{', ' if day > 0 else ''}" \
           f"{h_format}{' and ' if second == 0 and minute > 0  and hour > 0 or hour > 0 and minute == 0 and second > 0 else ', ' if hour > 0 and minute > 0 else ''}" \
           f"{m_format}{' and ' if second > 0 and minute > 0 else ''}" \
           f"{s_format}"


print(format_duration(37422240))

# 37422240
# test.assert_equals(format_duration(1), "1 second")
# test.assert_equals(format_duration(62), "1 minute and 2 seconds")
# test.assert_equals(format_duration(120), "2 minutes")
# test.assert_equals(format_duration(3600), "1 hour")
# test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
