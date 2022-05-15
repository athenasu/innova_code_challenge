"""
FileReaderService used for collecting files
"""
from office_hierarchy.util.FileUtil import FileUtil


class FileReaderService:
    """
    FileReaderService used for collecting files
    """

    def collect_json_file(self, file_path: str) -> list[dict]:
        """
        Call FileUtil to load json file
        Set internal variable to hold parsed list of dictionaries
        Cannot have empty json objects

        :param file_path: str
        :return: list[dict]
        """
        dataset = FileUtil.load_employees_from_json(file_path=file_path)
        if not dataset:
            raise TypeError('File is empty')
        else:
            return dataset
