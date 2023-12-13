class RkDataBase:

    def __init__(self):
        self.__data = dict()

    def add_key_value(self, key, value):
        self.__data[key] = value

    @staticmethod
    def create_rk_string():
        return str

    @staticmethod
    def save_as_rk_data(rk_sting, path):
        if isinstance(rk_sting, str):
            with open(path, "w") as data_str:
                data_str.write(rk_sting)
        else:
            raise TypeError

    @staticmethod
    def get_rk_data_as_pydict():
        return dict
