import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


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

    def test_selectable(self, driver):
        selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
        selectable_page.open()
        s_list = selectable_page.select_list_item()
        s_grid = selectable_page.select_grid_item()
        assert len(s_list) > 0
        assert len(s_grid) > 0

    def test_resizable(self, driver):
        resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
        resizable_page.open()
        max_size_box, min_size_box = resizable_page.change_size_resizable_box()
        max_size_resize, min_size_resize = resizable_page.change_size_resizable()
        assert ('500px', '300px') == max_size_box
        assert ('150px', '150px') == min_size_box
        assert max_size_resize != min_size_resize



