

def tsv_read(file_name, encode):
    file = open(file_name, encoding=encode)
    list_of_lines = list()
    for line in file:
        # params = line.split("\t")
        params = line.rstrip().split("\t")
        list_of_lines.append(params)
        # print(list_of_lines)
    return list_of_lines
