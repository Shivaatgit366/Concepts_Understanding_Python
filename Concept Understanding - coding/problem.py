
list_input = [
  "/webapp/assets/html/a.html",
  "/webapp/assets/js/c.js",
  "/webapp/assets/css/d.css",
  "/webapp/index.html",
  "/webapp/assets/html/b.html",
  "/tmp/x.csv"
]


def list_enumerated(list_var):
    """
    Takes any list as an input ['webapp', 'assets', 'html', 'a.html']
    Returns the output as a list with tuples [(0, 'webapp'), (1, 'assets'), (2, 'html'), (3, 'a.html')]
    """
    result = []
    for (x,y) in enumerate(list_var):
        item = (x,y)
        result.append(item)
    return result


def item_to_list_with_placevalue(any_list):
    i = 0
    final_list = []

    while i < len(any_list):
        split_list = any_list[i].split("/")
        del split_list[0]
        tuple_list = list_enumerated(split_list)
        final_list.append(tuple_list)
        i = i + 1

    return final_list


def stringg_returner(intt, stringg):
    """
    returns a string with whitespaces equal to "intt" value.
    """
    i = 0
    space = "-"
    req_str = ""
    while i < intt:
        req_str = space + req_str
        i = i + 1
    return (req_str + stringg)


if __name__ == "__main__":
    A = item_to_list_with_placevalue(list_input)

    for m in A:
        for (x, y) in m:
            print(stringg_returner(x, y))
