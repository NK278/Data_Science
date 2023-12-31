import binascii
def bin_hex(file_path,f2):
    with open(file_path,'rb') as file:
        bin_data=file.read()
        hex_data=binascii.hexlify(bin_data).decode()
    with open(f2,'w') as f:
        for i in hex_data: f.write(i)
bin_hex("Lato-Regular.bin","hex.txt")