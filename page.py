class Page:

    def __init__(self, object_list: list[str], page_number: int, total_pages: int) -> None:
        self.object_list = object_list
        self.page_number = page_number
        self.total_pages = total_pages

    def has_next(self) -> bool:
        return self.page_number < self.total_pages

    def has_previous(self) -> bool:
        return self.page_number > 1
