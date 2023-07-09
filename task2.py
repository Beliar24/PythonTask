class FileManager:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_name, self.file_mode)
            return self.file
        except IOError:
            print("Wrong file")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with FileManager("file.txt", 'r') as file:
    if file:
        for f in file:
            print(f)
