def open_subs_file(subs_file):
    subs = open(subs_file, 'r')
    return subs


def close_subs_file(subs_file):
    subs_file.close()


def get_sub_list(subs_file):
    subs = open_subs_file(subs_file)
    sub_list = []
    for line in subs:
        mod_line = line[:len(line) - 1]
        sub_list.append(mod_line)
    close_subs_file(subs)
    return sub_list

