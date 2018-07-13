""" Replace empty space in string with %20
    input is in form of list of characters as spec. """

def URLify(url, length):
    index = len(url)

    for i in reversed(range(length)):
        if url[i] == ' ':
            url[index - 3:index] = '%20'
            index -= 3
        else:
            url[index - 1] = url[i]
            index -= 1

    return url
