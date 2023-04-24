import uuid


def test_uuid():
    id_str = uuid.uuid4().hex
    id_str = 'autotest' + id_str[24:]
    print(id_str)
