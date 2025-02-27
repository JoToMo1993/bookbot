from stats import word_count, char_count
import sys


def main(path):
    book_report(path)

def book_report(file_name):
    print(f'--- Begin report of {file_name} ---')
    with open(file_name) as f:
        file_contents = f.read()
        print(f'{word_count(file_contents)} words found in the document\n')
        for char, count in sorted(char_count(file_contents).items(), key=lambda x: x[1], reverse=True):
            if 'a' <= char <= 'z':
                print(f"'{char}: {count}'")
        print('--- End report ---')

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

main(sys.argv[1])