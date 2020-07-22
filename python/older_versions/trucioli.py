codes = tuple((g, hex(ord(g))) for g in s)
for c in codes:
    print('char:', c[0], ' | codepoint:', c[1])
