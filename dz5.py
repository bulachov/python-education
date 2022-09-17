txt = 'text_for_5dz.txt'
_trg = 'abc'
res = None
with open(txt, 'r') as fr:
    res = [word for word in fr.read().split() if not _trg in word]
with open('out_txt.txt', 'w') as wrt: wrt.write(' '.join(res))


