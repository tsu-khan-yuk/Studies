class View:

    @staticmethod
    def table_view(table_name, ctrl):
        data = ctrl.get_all_table_items(table_name)
        for item in data:
            print(item)

    @staticmethod
    def items_view(fields_name, conditions, ctrl):
        data = ctrl.find_items(fields_name, conditions)
        time = data.pop('timer')
        for data_type in data.keys():
            print('{} values:'.format(data_type))
            for result in data[data_type]:
                print('|%(value)10s|' % {'value': result})
        print('Time result: {} [ms]'.format(time))