from typing import List


def make_proj_dict(projection_list: List[str]):
    result = {}
    for field in projection_list:
        result[field] = 1

    return result


def get_page_metadata(page_number: int, page_limit: int, count: int):
    skip = page_limit * (page_number - 1)
    pages_count = count // page_limit + 1

    return skip, pages_count
