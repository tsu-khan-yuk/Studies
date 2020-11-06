class View:

    @staticmethod
    def table_output(table_name, ctrl):
        # # TODO: rewrite cool output
        data = ctrl.get_all_table_items(table_name)
        for i in data:
            print(i)

    @staticmethod
    def item_output(data):
        pass
