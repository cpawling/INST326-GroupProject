with open("group_project.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)