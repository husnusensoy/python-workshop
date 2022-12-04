import json
from json.decoder import JSONDecodeError
from typing import List, Tuple

from .excp import JsonFileNotFound


def read_json(json_filename: str) -> dict:
    try:
        with open(json_filename) as fp:
            return json.load(fp)
    except FileNotFoundError:
        raise JsonFileNotFound(json_filename)
    except JSONDecodeError as j_error:
        print(j_error)
        return {}


def read_txt(txt_filename: str, sep: str = ",") -> List[Tuple]:
    try:
        with open(txt_filename) as fp:
            return [tuple(line.split(sep)) for line in fp]
    except FileNotFoundError:
        raise TxtFileNotFound(txt_filename)
