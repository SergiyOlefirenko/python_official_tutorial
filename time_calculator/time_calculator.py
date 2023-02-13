def return_day(days_after: int, day_of_week: str = None):
    days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    result = []

    if day_of_week:
        current_day_num = days_of_week.index(day_of_week.lower())
        weeks, day_num = divmod(days_after, 7)
        result.append(days_of_week[(current_day_num+day_num)%7].capitalize())
    if days_after:
        result.append('(next day)' if days_after == 1 else f'({days_after} days later)')

    result = ' '.join(result)
    return ', ' + result if day_of_week else ' ' + result

def add_time(start: str, duration: str, day: str = None) -> str:
    final_hour = None
    num_of_days = None
    new_time = None

    # get start time, convert it to int, and transform it to 24 hours format
    start_time = list(map(int, start[:-3].split(':')))
    if 'PM' in start:
        start_time[0] += 12

    # get duration time and convert it to int
    duration_time = list(map(int, duration.split(':')))
    print(duration_time)

    # get number of full days in duration and hours that are left
    num_of_days, hours_left = divmod(duration_time[0], 24)

    # increment start time by number of full hours in the sum of start and duraiton minutes
    sum_minutes = start_time[1] + duration_time[1]
    if sum_minutes > 59:
        hours, sum_minutes = divmod(sum_minutes, 60)
        start_time[0] += hours

    # calculate final hours and mintes values
    days, final_hour = divmod(start_time[0] + hours_left, 24)
    num_of_days += days
    am_pm, final_hour = divmod(final_hour, 12)

    new_time = f'{12 if final_hour == 0 else final_hour}:{sum_minutes:0>2d} {"AM" if am_pm < 1 else "PM"}{return_day(num_of_days, day)}'

    return new_time.strip()
