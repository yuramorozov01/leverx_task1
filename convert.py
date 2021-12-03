from serializers.xml_serializer import XmlSerializer
from serializers.json_serializer import JsonSerializer

import sys


def get_serializer_class(input_format):
    formats = {
        'json': JsonSerializer,
        'xml': XmlSerializer,
    }
    return formats.get(format_)

def get_dict_of_json_data(serializer, path):
    try:
        dict_data = serializer.load(path)
        return dict_data
    except FileNotFoundError as e:
        sys.exit(f'Cannot find file {path}')


def convert_data(students, rooms):
    pass


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(f'Format of executing: python3 {sys.argv[0]} path/to/students.json path/to/rooms.json format')

    path_to_students = sys.argv[1]
    path_to_rooms = sys.argv[2]
    format_ = sys.argv[3]

    serializer_class = get_serializer_class(format_)
    if not serializer_class:
        sys.exit(f'Unknown format: {format_}')

    serializer = serializer_class()
    dict_students = get_dict_of_json_data(serializer, path_to_students)
    dict_rooms = get_dict_of_json_data(serializer, path_to_rooms)
