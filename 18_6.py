def line(s, t):
    if '+' in s:
        equation = float(s[:s.find('x')]) * float(t[:t.find(';')]) + float(s[s.find('+'):])
    else:
        aaa = s[s.find('x'):]
        equation = float(s[:s.find('x')]) * float(t[:t.find(';')]) + float(aaa[aaa.find('-'):])
    if float(t[t.find(';') + 1:]) == equation:
        print(True)
    else:
        print(False)
