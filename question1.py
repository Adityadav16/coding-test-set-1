def create_paginator(items, page_size):
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]


items = [1,2,3,4,5,6,7,8]
page_size = 3

for page in create_paginator(items, page_size):
    print(page)
