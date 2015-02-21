# -*- coding: utf-8 -*-
# Takes options separated by 'or' and returns one by random.
# by andri
from random import choice

def decide(text):
    i = text.split(' or ')
    if len(i) > 1:
        return choice(i)
    else:
        return choice(["Yes", "No"])
