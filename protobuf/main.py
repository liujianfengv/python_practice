import json
import user_pb2


def print_hex(bytes_array):
    print("bytes size:", len(bytes_array))
    rows = []
    while bytes_array:
        rows.append(bytes_array[:8])
        bytes_array = bytes_array[8:]
    for row in rows:
        print(row.hex(' '))


def print_json():
    data = {'name': 'Mike',
            'age': 29,
            'sex': True,
            'phone': 'A123456'}
    print("json str:", json.dumps(data))
    hex_str = json.dumps(data).encode('utf-8')
    print_hex(hex_str)


def print_protobuf():
    user = user_pb2.UserInfo()
    user.name = "Mike"
    user.age = 29
    user.sex = True
    user.phone = "A123456"
    print("protobuf:", user.SerializeToString())
    print_hex(user.SerializeToString())


def test():
    print_json()
    print_protobuf()


if __name__ == '__main__':
    test()