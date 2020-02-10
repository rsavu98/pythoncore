def areYouPlayingBanjo(name):
    if name.startswith(('R', 'r')):
       return name + " plays banjo"
    else:
        return name + " does not play banjo"