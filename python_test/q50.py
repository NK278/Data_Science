import string
def freq_cnt(in_f,out_f):
    try:
        with open(in_f,'r') as f, open(out_f,'w') as o:
            wrd=f.read().split()
            mp={t: wrd.count(t) for t in set(wrd)}
            v=[k for k,c in mp.items() if c==max(mp.values())]
            for i in v: o.write(i+ " ")
    except FileNotFoundError: return "File not found!"

freq_cnt("m.txt", "out.txt")
