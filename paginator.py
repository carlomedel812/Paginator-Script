from page import Page

class Paginator:
    def __init__(self, items: list[str], items_per_page: int) -> None:
        self.pages: list[Page] = []
        self.list_of_items_per_page: list[list[str]] = self.split(items, items_per_page)
        self.count = len(items)
        self.number_pages = len(self.list_of_items_per_page)
    
        for index, lst in enumerate(self.list_of_items_per_page):
            self.pages.append(Page(lst, index + 1, len(self.list_of_items_per_page)))

    def split(self, lst: list[str], n: int) -> list[list[str]]:
        self.split_list = []
        n = max(1, n)

        for i in range(0, len(lst), n):
           self.split_list.append(lst[i:i+n])

        return self.split_list

    def page(self, page_number: int) -> Page:
        # Start at index 1
        return self.pages[page_number - 1]