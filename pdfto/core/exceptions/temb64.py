class Temb64Exception(Exception):

    def __init__(self):
        self.message = f'{self.__class__} base exception'

    def __str__(self):
        return self.message


class BrokenBase64(Temb64Exception):

    def __init__(self):
        self.message = 'Base64 may has been broken'
