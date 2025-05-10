from homework.src._internals.count_words import count_words
from homework.src._internals.parse_args import parse_args
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_into_words
from homework.src._internals.write_word_counts import write_word_counts


def main():
    input_dir, output_dir = parse_args()
    all_lines = read_all_lines(input_dir)
    all_lines = preprocess_lines(all_lines)
    words = split_into_words(all_lines)
    word_counts = count_words(words)
    write_word_counts(word_counts, output_dir)