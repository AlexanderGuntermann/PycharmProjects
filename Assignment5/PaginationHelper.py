
# I had to import math for the using of the ceiling function used to round up for page count
import math


class PaginationHelper:
    # The constructor t akes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        # rounds the number up one page if we have a decimal value.
        return int(math.ceil(1.0 * self.item_count() / (self.items_per_page)))

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):

        # if the index+1 * items per page is less than or equal to total items, then return the items per page set in constructor
        if (page_index + 1) * self.items_per_page <= self.item_count():
            return self.items_per_page
        # if the page index * the items per page is less than the item count and the page
        # index +1 * items per page is greater than the item count then return
        # the item count modulus items per page (the remainder)
        if page_index * self.items_per_page < self.item_count():
            if(page_index + 1) * self.items_per_page > self.item_count():
                return self.item_count() % self.items_per_page
        return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for PaginationHelper.pyitem_index values that are out of range
    def page_index(self, item_index):

        # if the item index is less than the total number of items and the item index is greater than 0,
        # then return the index divided by the number of items per page
        if item_index < self.item_count():
            if item_index >= 0:
                return item_index / self.items_per_page
        return -1


with open("Characters_read.txt", "r") as inFile:
    myLine = inFile.readline()
    collection = myLine.split(',')

    helper = PaginationHelper(collection, 5)
    print(collection)
    print("There are " + str(collection.__len__()) + " items in the list\n")
    print(helper.page_count())
    print(helper.item_count())
    print(helper.page_item_count(0))
    print(helper.page_item_count(1))
    print(helper.page_item_count(8))

    print(int(helper.page_index(5)))
    print(int((helper.page_index(2))))
    print((int(helper.page_index(20))))
    print(int(helper.page_index(-10)))
