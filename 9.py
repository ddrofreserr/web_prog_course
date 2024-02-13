import datetime as dt

inp_nums = [int(i) for i in input().split('-')]
day = dt.date(inp_nums[2], inp_nums[1], inp_nums[0])
ans_day = day - dt.timedelta(days=day.weekday())
print(dt.datetime.strftime(ans_day, '%d-%m-%Y'))
