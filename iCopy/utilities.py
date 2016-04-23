import os


def list_contents(path='.', full_list=None, recursive=True):
    path = os.path.abspath(path)
    contents = os.listdir(path)

    if not recursive:
        full_list = []
        for entry in contents:
            cur_path = os.path.join(path, entry)
            if os.path.isdir(cur_path):
                cur_path += os.path.sep
            full_list.append(cur_path)
        full_list.sort()
        return full_list

    if full_list is None:
        full_list = []
    for entry in contents:
        cur_path = os.path.join(path, entry)
        if os.path.isfile(cur_path):
            full_list.append(cur_path)
        elif os.path.isdir(cur_path):
            list_contents(cur_path, full_list)
        else:
            print "%s failed." % (cur_path)
    full_list.sort()
    return full_list
