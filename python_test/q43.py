import string
def freq_file2(file_path):
    try:
        with open(file_path,'r') as file:
            content=file.read()
            w=content.split()
            m={t:w.count(t) for t in set(w)}
            # m_k=max(m,key= lambda k:m[k])
            mcnt=max(m.values())
            return [k for k,c in m.items() if c==mcnt]
    except FileNotFoundError: return "File not found!"
file_path="m.txt"
print(freq_file2(file_path))