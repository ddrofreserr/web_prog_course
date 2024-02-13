import datetime as dt


def gift_count(*args, **kwargs):
    if args:
        budget, month, bds = args
    else:
        budget, month, bds = kwargs['budget'], kwargs['month'], kwargs['birthdays']
    
    bdpeople = {k: v for k, v in bds.items() if v.month == month}
    bdpeople_sorted = {k: v for k, v in sorted(bdpeople.items(), key=lambda x: x[1].day)}
    if len(bdpeople):
        to_insert = ', '.join([f'{k} ({dt.datetime.strftime(v, "%d.%m.%Y")})' for k, v in bdpeople_sorted.items()])
        print(f'''Именинники в месяце {month}: {to_insert}. 
              При бюджете {budget} они получат по {budget//len(bdpeople)} рублей.''')
    else:
        print('В этом месяце нет именинников.')
