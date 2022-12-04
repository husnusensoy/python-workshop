from pathlib import Path

import editdistance as ed


def similarity(tu):
    return tu[1]

class JsonFileNotFound(Exception):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

        path = Path(self.file_name)

        self.all_sims = sorted([
            (js, ed.eval(file_name, str(js))) for js in Path(path.parent).glob("*.json")
        ],key=similarity)
        # print(all_json)

    def __str__(self) -> str:
        return f"No such file or directory: '{self.file_name}'. Did you mean {str(self.all_sims[0][0])} ?"

class TxtFileNotFound(Exception):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

        path = Path(self.file_name)

        self.all_sims = sorted([
            (js, ed.eval(file_name, str(js))) for js in Path(path.parent).glob("*.txt")
        ],key=similarity)
        # print(all_json)

    def __str__(self) -> str:
        return f"No such file or directory: '{self.file_name}'. Did you mean {str(self.all_sims[0][0])} ?"