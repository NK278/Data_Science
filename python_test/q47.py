def txt_gen(file_path,v):
    with open(file_path,'w') as file:
        for i in v: file.write(i+"\n")
strings = ["Hello", "world", "how", "are", "you"]
txt_gen("ex.txt", strings)