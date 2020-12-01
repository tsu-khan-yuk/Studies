from mvc.controller import Controller


class View:
    ctrl = Controller()

    def table_view(self, table_name):
        data = self.ctrl.get_all_table_items(table_name)
        for item in data:
            print(item)

    def items_view(self, fields_name, conditions):
        data = self.ctrl.find_items(fields_name, conditions)
        time = data.pop('timer')
        for data_type in data.keys():
            print('{} values:'.format(data_type))
            for result in data[data_type]:
                print('|%(value)10s|' % {'value': result})
        print('Time result: {} [ms]'.format(time))

    def delete_item_view(self, entity: str, attribute: str, value: str):
        self.ctrl.delete_item(entity, attribute, value)

    def update_items_view(self):
        self.ctrl.update_item(table_name, attribute_to_change, new_value, key_attribute, key_value)

    def insert_random_items_view(self, table_name, rows_amount):
        self.ctrl.insert_random_item(table_name, rows_amount)

    def insert_item_view(self, table_name):
        self.ctrl.insert_item(table_name)