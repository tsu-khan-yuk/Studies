class View:

    @staticmethod
    def table_view(table_name, ctrl):
        data = ctrl.get_all_table_items(table_name)
        for item in data:
            print(i)

    @staticmethod
    def items_view(fields_name, ctrl):
        data = ctrl.find_items(fields_name)
        for item in data:
            print(item)
