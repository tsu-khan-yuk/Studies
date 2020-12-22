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
        
        for i in data:
            print(i)

    def delete_item_view(self, **kwargs):
        data = self.ctrl.delete_item(**kwargs)
        if data is None:
            print('Not deleted')
            return None
        print('Deleted data:')
        for i in data:
            print(i)

    def update_items_view(self, **kwargs):
        data = self.ctrl.update_item(**kwargs)
        for i in data:
            print(i)

    def insert_item_view(self, **kwargs):
        data = self.ctrl.insert_item(**kwargs)
        print(f'Created data:\n' + str(data))
