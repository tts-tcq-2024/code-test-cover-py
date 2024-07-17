MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def get_color_from_pair_number(pair_number):
    pair_number -= 1
    major = MAJOR_COLORS[pair_number // len(MINOR_COLORS)]
    minor = MINOR_COLORS[pair_number % len(MINOR_COLORS)]
    return major, minor

def get_pair_number_from_color(major, minor):
    try:
        major_index = MAJOR_COLORS.index(major)
        minor_index = MINOR_COLORS.index(minor)
    except ValueError:
        raise Exception('Index out of range')
    return major_index * len(MINOR_COLORS) + minor_index + 1

def test_number_to_pair(pair_number, major, minor):
    assert get_color_from_pair_number(pair_number) == (major, minor)

def test_pair_to_number(major, minor, pair_number):
    assert get_pair_number_from_color(major, minor) == pair_number

if __name__ == '__main__':
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    print('Done :)')
