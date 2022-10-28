import random
import time

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_item(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_item(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_item(self.locators.GRID_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, element):
        item_list = self.elements_are_visible(element)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(";")[0].split(":")[1].replace(" ", "")
        height = value_of_size.split(";")[1].split(":")[1].replace(" ", "")
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_visible(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
        self.drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                     random.randint(0, 300),
                                     random.randint(50, 150))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        self.drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE), -200, 1)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_simple(self):
        drag = self.element_is_visible(self.locators.SIMPLE_DRAG_ME)
        drop = self.element_is_visible(self.locators.SIMPLE_DROP_ME)
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        self.drag_and_drop_to_element(drag, drop)
        color = drop.value_of_css_property('background-color')
        return drop.text, color

    def drop_accept(self, drag):

        drag_list = {
            "Acceptable": self.locators.ACCEPTABLE,
            "Not  Acceptable": self.locators.NOT_ACCEPTABLE
        }
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        drag_a = self.element_is_visible(drag_list[drag])
        drop_a = self.element_is_visible(self.locators.ACCEPT_DROP_ME)
        self.drag_and_drop_to_element(drag_a, drop_a)
        color = drop_a.value_of_css_property('background-color')
        return drop_a.text, color

    def drop_prevent_propogation(self):
        self.element_is_visible(self.locators.PREVENT_PROPOGATION_TAB).click()
        drag = self.element_is_visible(self.locators.PREVENT_DRAG_ME)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        self.drag_and_drop_to_element(drag, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEX).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.drag_and_drop_to_element(drag, greedy_inner_box)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEX).text
        text_greedy_inner_box = not_greedy_inner_box.text

        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box

    def drop_revent_draggable(self, drag):
        drag_list = {
            "Will Revert": self.locators.WILL_REVERT,
            "Not Revert": self.locators.NOT_REVERT
        }

        self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB).click()
        will_revert = self.element_is_visible(drag_list[drag])
        drop = self.element_is_visible(self.locators.REVERT_DROP_ME)
        self.drag_and_drop_to_element(will_revert, drop)
        position_after_move = will_revert.get_attribute("style")
        time.sleep(2)
        position_after_rev = will_revert.get_attribute("style")
        return position_after_move, position_after_rev





