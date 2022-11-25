#!/usr/bin/env python3

from paginator import Paginator

objects = [
 "Lauren Vickers",
 "Shazia Darby",
 "Zara Cain",
 "Edna Bradbury Parsons",
 "Clair Newton",
 "April Bruce Cain Kieran",
 "Timothy Bower",
 "Tracie Atkin Stanton",
 "Mabel Meadows",
 "Helen Rolfe",
 "Catriona Sampson"
]


items_per_page = 3
paginator = Paginator(objects, items_per_page)

print("total count objects: " + str(paginator.count))
print("number of pages:" + str(paginator.number_pages))

page1 = paginator.page(1)

print("page 1 objet list: " + str(page1.object_list))
print("page 1 has next page: " + str(page1.has_next()))
print("page 1 has previous: " + str(page1.has_previous()))

page2 = paginator.page(2)

print("page 2 objet list: " + str(page2.object_list))
print("page 2 has next page: " + str(page2.has_next()))
print("page 2 has previous: " + str(page2.has_previous()))