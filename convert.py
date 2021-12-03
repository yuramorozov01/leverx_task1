import sys
from json import JSONDecodeError

import xmltodict

from exceptions.format_error import FormatError
from serializers.json_serializer import JsonSerializer
from serializers.xml_serializer import XmlSerializer


def get_serializer_class(input_format):
    '''Determine serializer class by a data format.
    Can be 2 formats:
        - JSON
        - XML
    '''
    formats = {
        'json': JsonSerializer,
        'xml': XmlSerializer,
    }
    return formats.get(input_format)


def get_dict_of_json_data(serializer, path):
    '''Loading data in dictionary format with specified serializer and from specified path.'''
    try:
        dict_data = serializer.load(path)
        return dict_data
    except FileNotFoundError as e:
        sys.exit(f'Cannot find file {path}')
    except FormatError as e:
        sys.exit(str(e))
    except JSONDecodeError as e:
        sys.exit(str(e))
    except xmltodict.expat.ExpatError as e:
        sys.exit(str(e))


def convert_data(students, rooms):
    '''Extending rooms information by a list of students in this rooms.'''
    students_in_rooms = {}
    for student in students:
        room_id = student.get('room')
        if room_id not in students_in_rooms:
            students_in_rooms[room_id] = []
        student_id = student.get('id')
        if student_id is not None:
            students_in_rooms[room_id].append(student_id)

    extended_rooms = rooms.copy()
    for room in extended_rooms:
        room_id = room.get('id')
        if room_id is not None:
            list_of_students = students_in_rooms.get(room_id)
            if list_of_students is not None:
                room['students'] = list_of_students

    return extended_rooms


def save_joined_data(serializer, data, path):
    '''Save processed data with specified serializer to file with path "path"'''
    try:
        serializer.save(data, path)
    except FileNotFoundError as e:
        sys.exit(str(e))
    except FormatError as e:
        sys.exit(str(e))
    except JSONDecodeError as e:
        sys.exit(str(e))
    except xmltodict.expat.ExpatError as e:
        sys.exit(str(e))


if __name__ == '__main__':
    if len(sys.argv) != 5:
        sys.exit(f'Format of executing: '
                 f'python3 {sys.argv[0]} path/to/students.json path/to/rooms.json format path/to/save')

    path_to_students = sys.argv[1]
    path_to_rooms = sys.argv[2]
    format_ = sys.argv[3]
    path_to_save = sys.argv[4]

    serializer_class = get_serializer_class(format_)
    if not serializer_class:
        sys.exit(f'Unknown format: {format_}')

    serializer = serializer_class()
    dict_students = get_dict_of_json_data(serializer, path_to_students)
    dict_rooms = get_dict_of_json_data(serializer, path_to_rooms)

    joined_data = convert_data(dict_students, dict_rooms)
    save_joined_data(serializer, joined_data, path_to_save)
    print(f'File has been successfully saved to {path_to_save}')
