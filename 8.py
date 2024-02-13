words = list(word.strip(',') for word in input().lower().split())
dict = {key: words.count(key) for key in set(words)}
print(*[f'{k}: {v}' for k, v in sorted(dict.items(), key=lambda it: it[1], reverse=True)[:3]], sep='\n')
