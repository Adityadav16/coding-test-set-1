def create_paginator(items, page_size):
    """
    Generates pages of items with the given page size.
    """

    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]



if __name__ == "__main__":

    items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    page_size = 3

    paginator = create_paginator(items, page_size)

    print("Pages:")

    for page in paginator:
        print(page)
