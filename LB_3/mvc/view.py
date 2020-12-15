from mvc.controller import Controller


class View:
    ctrl = Controller()

    def table_view(self, **kwargs):
        data = self.ctrl.get_all_table_items(**kwargs)
        if data == []:
            print('Table is empty')
            return None
        for item in data:
            print(item)

    def items_view(self, **kwargs):
        self.ctrl.find_items(**kwargs)

    def delete_item_view(self, **kwargs):
        self.ctrl.delete_item(**kwargs)

    def update_items_view(self, **kwargs):
        self.ctrl.update_item(**kwargs)

    def insert_random_items_view(self, **kwargs):
        self.ctrl.insert_random_item(**kwargs)

    def insert_item_view(self, **kwargs):
        self.ctrl.insert_item(**kwargs)
