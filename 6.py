print(*sorted(set(word.strip(',') for word in input().lower().split())), sep=', ')
