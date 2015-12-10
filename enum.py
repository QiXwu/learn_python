# -*- coding: utf-8 -*-

def enum(**enums):
    return type('Enum', (), enums)

Numbers = enum(ONE=1,TWO=2,THREE='three')

print Numbers.ONE
print Numbers.THREE