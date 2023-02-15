class FileWriter:
    def __init__(self, fullpath) -> None:
        self.fullpath = fullpath

    def write(self, image):
        image.save(self.fullpath)