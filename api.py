import json
import requests
from settings import VALID_PASSWORD, VALID_EMAIL, PET_ID_FOR_COMMENT


class Pets:
    """ API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'
        self.my_token = self.get_token()[0]

    """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
    def get_token(self) -> json:
        data = {"email": VALID_EMAIL,
                "password": VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    """Запрос к Swagger сайта для получения ID своего профиля"""
    def get_user_id(self) -> json:
        headers = {'Authorization': f'Bearer {self.my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json()
        return status, amount

    """Запрос к Swagger сайта для создания питомца"""
    def post_pet(self) -> json:
        my_id = self.get_token()[2]
        headers = {'Authorization': f'Bearer {self.my_token}'}
        data = {"name": 'Zog', "type": 'reptile', "age": 11, "gender": 'Male', "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    """Запрос к Swagger сайта для добавления фото питомца"""
    def post_pet_photo(self, pet_id):
        headers = {'Authorization': f'Bearer {self.my_token}'}
        files = {'pic': ('image', open(r'../tests/photos/zog.jpg', 'rb'), 'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    """Запрос к Swagger сайта для получение информации о питомце"""
    def get_pet(self) -> json:
        pet_id = self.post_pet()[0]
        headers = {'Authorization': f'Bearer {self.my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        pet_info = res.json()['pet']
        pet_name = pet_info['name']
        pet_gender = pet_info['gender']
        pet_age = pet_info['age']
        pet_type = pet_info['type']
        owner_id = pet_info['owner_id']
        owner_name = pet_info['owner_name']
        status = res.status_code
        return pet_name, pet_gender, pet_age, pet_type, owner_id, owner_name, status

    """Запрос к Swagger сайта для удаления питомца"""
    def delete_pet(self):
        pet_id = self.post_pet()[0]
        headers = {'Authorization': f'Bearer {self.my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    """Запрос к Swagger сайта для получения списка питомцев"""
    def post_pets_list(self):
        my_id = self.get_token()[2]
        headers = {'Authorization': f'Bearer {self.my_token}'}
        data = {"user_id": my_id}
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        pets_list = res.json()['list']
        return status, pets_list

    """Запрос к Swagger сайта для изменения питомца"""
    def patch_pet(self, pet_id) -> json:
        my_id = self.get_token()[2]
        data = {"id": pet_id, "name": 'GG', "type": 'dog', "age": 22, "gender": 'Female', "owner_id": my_id}
        headers = {'Authorization': f'Bearer {self.my_token}'}
        res = requests.patch(self.base_url + f'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        pet_id = res.json()['id']
        return status, pet_id

    """Запрос к Swagger сайта оставить комментарий питомцу"""
    def put_pet_comment(self) -> json:
        pet_id = PET_ID_FOR_COMMENT
        data = {'pet_id': PET_ID_FOR_COMMENT, 'message': 'WOW!'}
        headers = {'Authorization': f'Bearer {self.my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        id_comment = res.json()['id']
        return status, id_comment

    """Запрос к Swagger сайта поставить лайк питомцу, вместо pet_id введите любой ID питомца"""
    def put_pet_like(self) -> json:
        pet_id = PET_ID_FOR_COMMENT
        headers = {'Authorization': f'Bearer {self.my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = res.status_code
        return status

    """Запрос к Swagger сайта для удаления всех питомцев"""
    def delete_pets(self, pet_id):
        headers = {'Authorization': f'Bearer {self.my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

# Pets().post_pet()
# Pets().get_pet()
# Pets().post_pet_photo()
# Pets().delete_pet()
# Pets().post_pets_list()
# Pets().patch_pet()
# Pets().put_pet_comment()
# Pets().put_pet_like()
