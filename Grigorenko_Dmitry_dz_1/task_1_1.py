duration = int(input())
days = duration // 86400
hours = (duration - days*86400)//3600
minutes = (duration - days*86400 - hours*3600)//60
seconds = duration - days*86400 - hours*3600 - minutes*60
print(days,'дн',hours,'час',minutes,'мин',seconds,'сек')