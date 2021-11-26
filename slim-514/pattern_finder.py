import re

def load_patterns(file_name):
    re_template = r'''\b{word}\b'''
    with open(file_name, 'rt') as f:
        patterns = f.read().split()

    return [
        re.compile(re_template.format(word=word))
        for word in patterns
    ]
    


def extract_column(file_name):
    column_list = []
    with open(file_name, 'rt') as f:
        for line in f:
            words = line.split(",")
            _, _, col3, _ = words
            column_list.append(col3)

    return column_list
            

def find_matches(column_list, patterns):
    for row in column_list:
        for pattern in patterns:
            if pattern.search(row):
                result = pattern.search(row)
                print(result.group(), '->', row)
                # Adding break to only allow first priority
                break


if __name__ == "__main__":
    pattern_list = load_patterns('word_list.csv')
    column_list = extract_column('data.csv')
    find_matches(column_list, pattern_list)