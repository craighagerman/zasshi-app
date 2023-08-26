import os


class DevData:

    def data_dir(self):
        return "/Users/chagerman/MyProjects/Zasshi-2023/Code/Data"

    def dev_data_dir(self):
        return os.path.join(self.data_dir(), "dev_data")

