def lists_sum(*args, unique=False):
    if unique:
        for_non_rep = []
        [[for_non_rep.append(int(it[i])) for i in range(len(it))] for it in args]
        return sum(set(for_non_rep))
    else:
        return sum([sum([int(it[i]) for i in range(len(it))]) for it in args])
