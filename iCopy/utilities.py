import os


def list_contents(path, full_list=None, recursive=True):
    """
    List the contents of path.

    path:      [string]  The path to the file or dtrectory to list.
    full_list: [list]    A pre-populated list of files for the new list to
                         append to.
    recursive: [boolean] Choose whether to do a recursive listing of the
                         contents or list the contents of the path only.
    """
    path = os.path.abspath(path)

    if os.path.isfile(path):
        return [path]

    if full_list is None:
        full_list = []

    contents = os.listdir(path)

    if not recursive:
        for entry in contents:
            cur_path = os.path.join(path, entry)
            if os.path.isdir(cur_path):
                cur_path += os.path.sep
            full_list.append(cur_path)
    else:
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
