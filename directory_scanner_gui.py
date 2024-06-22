import tkinter as tk
from tkinter import filedialog, messagebox
from directory_scanner import DirectoryScanner

class DirectoryScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Scanner")

        self.directory_path = tk.StringVar()
        self.detection_patterns = tk.StringVar()
        self.destruction_patterns = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select Directory:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.directory_path, width=50).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_directory).grid(row=0, column=2, padx=10, pady=5)

        tk.Label(self.root, text="Detection Patterns (comma separated):").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.detection_patterns, width=50).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Destruction Patterns (comma separated):").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.destruction_patterns, width=50).grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Scan Directory", command=self.scan_directory).grid(row=3, column=0, columnspan=3, pady=10)
        tk.Button(self.root, text="Delete Files", command=self.delete_files).grid(row=4, column=0, columnspan=3, pady=10)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_path.set(directory)

    def scan_directory(self):
        directory = self.directory_path.get()
        if not directory:
            messagebox.showerror("Error", "Please select a directory")
            return

        scanner = DirectoryScanner(directory)
        detection_patterns = self.detection_patterns.get().split(',')
        scanner.set_detection_patterns([pattern.strip() for pattern in detection_patterns])
        
        scanner.scan_directory()
        most_common_words = scanner.most_common_words(20)
        
        result = "\n".join([f"{word}: {count}" for word, count in most_common_words])
        messagebox.showinfo("Most Common Words", result)

    def delete_files(self):
        directory = self.directory_path.get()
        if not directory:
            messagebox.showerror("Error", "Please select a directory")
            return

        scanner = DirectoryScanner(directory)
        destruction_patterns = self.destruction_patterns.get().split(',')
        scanner.set_destruction_patterns([pattern.strip() for pattern in destruction_patterns])
        
        scanner.delete_files_matching_pattern()
        messagebox.showinfo("Delete Files", "Files matching the patterns have been deleted")

if __name__ == "__main__":
    root = tk.Tk()
    app = DirectoryScannerGUI(root)
    root.mainloop()
