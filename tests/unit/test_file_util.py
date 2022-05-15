import pytest

from office_hierarchy.entity.EmployeeError import EmployeeIOError
from office_hierarchy.util.FileUtil import FileUtil


@pytest.mark.parametrize('input_file_path', ['tests/data/error_bad_json_format.json'])
def test_raise_json_decode_error(input_file_path):
    with pytest.raises(EmployeeIOError):
        FileUtil.load_employees_from_json(input_file_path)

