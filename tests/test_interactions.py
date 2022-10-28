import time
import pytest
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


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

    def test_simple_drop(self, driver):
        drop_page = DroppablePage(driver, "https://demoqa.com/droppable")
        drop_page.open()
        text, color = drop_page.drop_simple()
        assert text == 'Dropped!'
        assert color == 'rgba(70, 130, 180, 1)'

    @pytest.mark.parametrize('drag', ['Acceptable', "Not  Acceptable"])
    def test_accept_drop(self, driver, drag):
        drop_page = DroppablePage(driver, "https://demoqa.com/droppable")
        drop_page.open()
        text, color = drop_page.drop_accept(drag)
        if drag == 'Acceptable':
            assert text == 'Dropped!'
            assert color == 'rgba(70, 130, 180, 1)'
        elif drag == 'Not  Acceptable':
            assert text == 'Drop here'
            assert color == 'rgba(0, 0, 0, 0)'

    def test_prevent_propogation_drop(self, driver):
        drop_page = DroppablePage(driver, "https://demoqa.com/droppable")
        drop_page.open()
        not_greedy_box, not_greedy_inner_box, greedy_box, greedy_inner_box = drop_page.drop_prevent_propogation()
        assert not_greedy_box == 'Dropped!'
        assert not_greedy_inner_box == 'Dropped!'
        assert greedy_box == 'Outer droppable'
        assert greedy_inner_box == 'Dropped!'

    @pytest.mark.parametrize('revert', ['Will Revert', 'Not Revert'])
    def test_revert_draggable_drop(self, driver, revert):
        drop_page = DroppablePage(driver, "https://demoqa.com/droppable")
        drop_page.open()
        drop_page.drop_revent_draggable(revert)

