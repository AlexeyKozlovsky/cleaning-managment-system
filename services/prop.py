from configs import db
from models.prop import Property


async def get_prop_by_id_service(id: str):
    """Метод для получения информации о свойстве из БД по ID
    id: ID свойства из БД"""
    pass


async def get_prop_by_name_service(name: str):
    """Метод для получения информации о свойстве из БД по названию
    name: название свойства"""
    pass


async def get_props_service(page_number: int, page_limit: int):
    """Метод для получения информации о свойствах из БД
    page_number: номер страницы
    page_limit: количество элементов на странице"""
    pass


async def add_new_prop_service(prop: Property):
    """Метод для добавления нового свойства в БД
    prop: модель свойства (в контексте БД)"""
    pass


async def update_prop_service(prop_id: str, prop: Property):
    """Метод для обновления информации о свойстве, которое уже есть в БД
    prop_id: ID свойства из БД
    prop: модель свойства (в контексте БД)"""
    pass


async def delete_prop_service(prop_id: str):
    """Метод для удаления свойства из БД
    prop_id: ID свойства из БД"""
    pass
