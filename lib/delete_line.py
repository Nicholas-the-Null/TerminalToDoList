def delete(file,linea):
    a_file = open(file, "r")
    lines = a_file.readlines()
    a_file.close()
    del lines[linea-1]
    new_file = open(file, "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()




