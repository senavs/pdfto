class MyPDFException(Exception):

    def __init__(self):
        self.message = f'{self.__class__} base exception'

    def __str__(self):
        return self.message


class MyPDFFileError(MyPDFException):

    def __init__(self):
        self.message = 'File not found or file is not a PDF'
