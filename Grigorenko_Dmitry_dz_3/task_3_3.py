def thesaurus(*args):
    dict_out = {}
    for arg in args:
        key = arg[0].capitalize()
        if key not in dict_out:
            dict_out[key] = []
        dict_out[key].append(arg)
    return dict_out

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Борис", "Ирина", "Михаил", "Игнат", "Игорь"))