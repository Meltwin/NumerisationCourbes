# Process List
from typing import Tuple

COLUMNS = {"num": "N", "name": "Name"}
COLUMNS_SIZE = {"num": 20, "name": 170}

MULTIPLE = True
CATEGORIES = {
    "load": ("Image Loading", not MULTIPLE),
    "img_proc": ("Image Processing", MULTIPLE),
    "conv": ("Image -> Points", not MULTIPLE),
    "ptn_proc": ("Point Processing", MULTIPLE),
    "export": ("Exporting", MULTIPLE)
}
DEFAULT_PROC = [
    ("img_proc", "test1", "Process Img 1"),
    ("img_proc", "test2", "Process Img 2"),
    ("ptn_proc", "test3", "Process Ptn 1"),
]
CATEGORY_TAG = "cat"


def get_columns():
    return tuple([k for k in COLUMNS])


def get_categories() -> Tuple[str, str, bool]:
    """
    Iterator on categories

    :return: (cat_id, cat_name, allow sub)
    """
    for cid in CATEGORIES:
        yield cid, CATEGORIES[cid][0], CATEGORIES[cid][1]


def get_col_config():
    for col_id in COLUMNS:
        yield col_id, COLUMNS[col_id], COLUMNS_SIZE[col_id]
