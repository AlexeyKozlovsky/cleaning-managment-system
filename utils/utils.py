from typing import List

import bson
import pymongo.collection


def make_proj_dict(projection_list: List[str]):
    result = {}
    for field in projection_list:
        result[field] = 1

    return result


def get_page_metadata(page_number: int, page_limit: int, count: int):
    skip = page_limit * (page_number - 1)
    pages_count = count // page_limit + 1

    return skip, pages_count


def get_paginate_with_projection(page_number: int, page_limit: int, projection: List[str],
                                 col: pymongo.collection.Collection):
    if projection:
        proj = make_proj_dict(projection)
    else: proj = None

    skip, pages_count = get_page_metadata(page_number, page_limit, col.count())

    result_cursor = col.find({}, projection=proj).skip(skip).limit(page_limit)
    result = []
    for obj in result_cursor:
        obj['_id'] = str(obj['_id'])
        result.append(obj)

    return {
        'message': 'success',
        'result': result
    }


def get_obj_with_projection(obj_id: str, projection: List[str],
                            col: pymongo.collection.Collection):
    proj = make_proj_dict(projection)

    result = col.find_one({'_id': bson.ObjectId(obj_id)}, projection=proj)
    result['_id'] = str(result['_id'])

    return {
        'message': 'success',
        'result': result
    }


def update_obj(obj_id: str, updated_params: dict,
               col: pymongo.collection.Collection):
    col.update_one({'_id': bson.ObjectId(obj_id)}, {
        '$set': updated_params
    })

    result = col.find_one({'_id': bson.ObjectId(obj_id)})
    result['_id'] = str(result['_id'])
    return {
        'message': 'success',
        'result': result
    }
