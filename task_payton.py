import uuid


def test_uuid():
    id_str = uuid.uuid4()
    id_str1 = str(uuid.uuid4())
    id_str1 = 'autotest' + id_str1[8:]
    print(id_str1)