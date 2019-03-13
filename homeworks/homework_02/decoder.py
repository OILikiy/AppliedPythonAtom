import os
import tabletext

encodings_list = ["utf8", "utf16", "cp1251"]
path_to_files = "/home/oleg/projects/AppliedPythonAtom/" +\
                "homeworks/homework_02/files/"
list_of_files = os.listdir(path_to_files)
# print(list_of_files)


def encoding_file(file_name, encodings):
    for encode in encodings:
        f = open(file_name, encoding=encode)
        try:
            f.read()
            return file_name, encode
        except UnicodeError:
            continue


# def draw_tsv(list_of_list):
#     col = list()
#     len_of_col = list()
#     for i in range(len(list_of_list[0])):
#         col.append([])
#         # len_of_col.append([])
#         for j in range(len(list_of_list)):
#             col[i].append(list_of_list[j][i])
#         # len_of_col[i].append(len(max(col[i], key=len)))
#         len_of_col.append(len(max(col[i], key=len)))
#     print(col)
#     print(len_of_col)
#     print(len_of_col[0][0])


# print(encoding_file(path_to_files + list_of_files[1], encodings_list))
# filename, encode = encoding_file(path_to_files + list_of_files[2],
#                                  encodings_list)
# tsv_read(filename, encode)
# list_of_list = tsv_read(filename, encode)
# print(list_of_list)
# list_of_list = json_read(filename, encode)
# print(list_of_list)
# print(tabletext.to_text(list_of_list))
