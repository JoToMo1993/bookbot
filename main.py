from stats import word_count, char_count


def main():
    book_report('books/frankenstein.txt')

def book_report(file_name):
    print(f'--- Begin report of {file_name} ---')
    with open(file_name) as f:
        file_contents = f.read()
        print(f'{word_count(file_contents)} words found in the document\n')
        for char, count in sorted(char_count(file_contents).items(), key=lambda x: x[1], reverse=True):
            if 'a' <= char <= 'z':
                print(f"The '{char}' character was found {count} times")
        print('--- End report ---')

main()