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
        data = self.ctrl.find_items(**kwargs)
        if data is None:
            print('No items found')
        else:
            print('Found items')
            for i in data:
                print(i)

    def delete_item_view(self, **kwargs):
        data = self.ctrl.delete_item(**kwargs)
        if data is None:
            print('Not deleted')
        else:
            print('Deleted data:')
            for i in data:
                print(i)

    def update_items_view(self, **kwargs):
        data = self.ctrl.update_item(**kwargs)
        if data is None:
            print('No updated data')
        else:
            print('Data updated')

    def insert_item_view(self, **kwargs):
        data = self.ctrl.insert_item(**kwargs)
        if data is None:
            print('New data not created')
        else:
            print(f'Created data:\n' + data)
