# Data Encoding - Run-Length Encoding (RLE) Compression
text = "aannnnjjjjeeeekooooopppgkuuuuurxcvjtaaaaaapooppp"
def run_length_encoding(text):
    if not text:
        return "" 
    encoded_str = ""
    count = 1 
    for i in range(1, len(text)):
        if text[i] == text[i - 1]: 
            count += 1
        else:
            encoded_str += text[i - 1] + (str(count) if count > 1 else "")
            count = 1 
    encoded_str += text[-1] + (str(count) if count > 1 else "")
    return encoded_str

print(run_length_encoding(text))


