from api import Pets
pt = Pets()


def test_get_token():
    result = pt.get_token()
    token = result[0]
    status = result[1]
    my_id = result[2]
    assert status == 200
    assert token
    assert my_id == 1208


def test_user_id():
    result = pt.get_user_id()
    status = result[0]
    amount = result[1]
    assert status == 200
    assert amount == 1208


def test_post_pet():
    result = pt.post_pet()
    pet_id = result[0]
    status = result[1]
    assert pet_id
    assert status == 200


def test_get_pet_photo():
    pet_id = pt.post_pet()[0]
    result = pt.post_pet_photo(pet_id)
    status = result[0]
    link = result[1]
    assert status == 200
    assert link


def test_get_pet():
    result = pt.get_pet()
    pet_name = result[0]
    pet_gender = result[1]
    pet_age = result[2]
    pet_type = result[3]
    owner_id = result[4]
    owner_name = result[5]
    status = result[6]
    assert status == 200
    assert pet_name == 'Zog'
    assert pet_age == 11
    assert pet_gender == 'Male'
    assert pet_type == 'reptile'
    assert owner_id == 1208
    assert owner_name == 'fir@mail.ru'


def test_delete_pet():
    result = pt.delete_pet()
    status = result
    assert status == 200


def test_post_pets_list():
    result = pt.post_pets_list()
    status = result[0]
    pets_list = result[1]
    assert status == 200
    assert len(pets_list) > 0


def test_patch_pet():
    pet_id = pt.post_pet()[0]
    result = pt.patch_pet(pet_id)
    status = result[0]
    pet_id = result[1]
    assert status == 200
    assert pet_id


def test_put_comment():
    result = pt.put_pet_comment()
    status = result[0]
    id_comment = result[1]
    assert status == 200
    assert id_comment


def test_put_like():
    result = pt.put_pet_like()
    status = result
    assert status == 403 or 200


def test_delete_all_pets():
    pets_list = pt.post_pets_list()[1]
    for pet in pets_list:
        pt.delete_pets(pet['id'])
    pets_list = pt.post_pets_list()[1]
    assert len(pets_list) == 0
