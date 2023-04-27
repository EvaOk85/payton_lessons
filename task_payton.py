import uuid

# 1 вариант
def test_uuid():
    id_str = str(uuid.uuid4())
    id_str1 = 'autotest' + id_str[8:]
    return (id_str1)


# 2 вариант

def test_uuid1():
    id_str = str(uuid.uuid4())
    li = id_str.split('-')
    li[0] = 'autotest'
    return ('-'.join(li))

#3 вариант
def test_uuid2():
    id_str = str(uuid.uuid4())
    li1 = id_str.split('-')
    for i in range (len(li1)):
      if i==0:
         li1[i] = 'autotest'

    return ('-'.join(li1))


