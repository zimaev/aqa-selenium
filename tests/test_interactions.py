from pages.interactions_page import SortablePage


class TestInteractions:

    def test_sortable_list(self, driver):
        sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
        sortable_page.open()
        order_before, order_after = sortable_page.change_list_order()
        assert order_before != order_after

    def test_sortable_grid(self, driver):
        sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
        sortable_page.open()
        order_before, order_after = sortable_page.change_grid_order()
        assert order_before != order_after
