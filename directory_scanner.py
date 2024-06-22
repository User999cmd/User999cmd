import os
import fnmatch
from collections import Counter
import re

class DirectoryScanner:
    def __init__(self, root_directory):
        self.root_directory = root_directory
        self.word_counter = Counter()
        self.detection_patterns = []
        self.destruction_patterns = []

    def scan_directory(self):
        for dirpath, _, filenames in os.walk(self.root_directory):
            for pattern in self.detection_patterns:
                for filename in fnmatch.filter(filenames, pattern):
                    self._process_file(os.path.join(dirpath, filename))

    def _process_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                for line in file:
                    words = self._extract_words(line)
                    self.word_counter.update(words)
                    self._process_word_sequences(words)
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

    def _extract_words(self, line):
        return re.findall(r'\b\w+\b', line.lower())

    def _process_word_sequences(self, words):
        for i in range(len(words) - 1):
            bigram = (words[i], words[i + 1])
            self.word_counter[bigram] += 1
        for i in range(len(words) - 2):
            trigram = (words[i], words[i + 1], words[i + 2])
            self.word_counter[trigram] += 1

    def most_common_words(self, n=10):
        return self.word_counter.most_common(n)

    def delete_file(self, filepath):
        try:
            os.remove(filepath)
            print(f"Deleted file: {filepath}")
        except OSError as e:
            print(f"Error deleting {filepath}: {e}")

    def delete_files_matching_pattern(self):
        for dirpath, _, filenames in os.walk(self.root_directory):
            for pattern in self.destruction_patterns:
                for filename in fnmatch.filter(filenames, pattern):
                    self.delete_file(os.path.join(dirpath, filename))

    def set_detection_patterns(self, patterns):
        self.detection_patterns = patterns

    def set_destruction_patterns(self, patterns):
        self.destruction_patterns = patterns
