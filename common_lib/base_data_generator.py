import os
import random
import string


class BaseDataGenerator:
    @staticmethod
    def generate_random_string(string_length):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(string_length))

    @staticmethod
    def generate_random_num(digit_number=5):
        start = int('1' + '0'*(digit_number-1))
        end = int('9' + '9' * (digit_number - 1))
        return random.randint(start, end)