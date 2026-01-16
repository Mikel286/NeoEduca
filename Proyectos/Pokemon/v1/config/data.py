
def data_read(file):
    try:
        return next(file)
    except StopIteration:
        return None
    
def line_decompress(line):
    if line != None:
        return line.strip().split(";")