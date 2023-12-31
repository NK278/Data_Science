import string
def freq_file(file_path):
    try:
        with open(file_path,'r') as file:
            content=file.read()
            words=[word.strip(string.punctuation) for word in content.split()]
            longest_word=max(words, key=len)
            return longest_word
    except FileNotFoundError: return "File not found"
file_path="wrd.txt"
res=freq_file(file_path)
if res!= "File not found": print(f"longest word is: {res}")
else: print(res)
