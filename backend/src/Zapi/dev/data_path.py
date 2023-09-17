import os
from pathlib import Path

class DevData:

    def data_dir(self):
        cwd = os.getcwd()
        p = Path(cwd)
        project_dir = p.parent.parent.parent.parent
        data_dir = os.path.join(project_dir, "data")
        # i.e. '/Users/chagerman/MyProjects/Zasshi/data'
        return data_dir

    def dev_data_dir(self):
        return os.path.join(self.data_dir(), "dev_data")

