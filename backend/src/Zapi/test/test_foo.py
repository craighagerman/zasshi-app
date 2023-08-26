import inspect
import json
import pytest
import os
from dev.data_path import DevData

class TestFoo:

    def test_dev_data(self):
        data_dir = DevData().data_dir()
        dev_data_dir = DevData().dev_data_dir()
        print(f"\ndata_dir: {data_dir}")
        print(f"dev_data_dir: {dev_data_dir}")


if __name__ == '__main__':
    pytest.main()
