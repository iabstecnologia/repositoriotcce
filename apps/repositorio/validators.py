import re
from django.core.exceptions import ValidationError


def validate_isbn(value):
    # Remove hifens e espaços
    code = re.sub(r'[- ]', '', value)

    if len(code) == 10:
        # Lógica ISBN-10
        sum_val = 0
        for i in range(9):
            if not code[i].isdigit():
                raise ValidationError("ISBN-10 inválido.")
            sum_val += int(code[i]) * (10 - i)

        last_char = code[9].upper()
        check_digit = 10 if last_char == 'X' else int(last_char)

        if (sum_val + check_digit) % 11 != 0:
            raise ValidationError("Dígito verificador do ISBN-10 incorreto.")

    elif len(code) == 13:
        # Lógica ISBN-13
        if not code.isdigit():
            raise ValidationError("ISBN-13 deve conter apenas números.")

        sum_val = 0
        for i in range(12):
            factor = 1 if i % 2 == 0 else 3
            sum_val += int(code[i]) * factor

        check_digit = (10 - (sum_val % 10)) % 10
        if int(code[12]) != check_digit:
            raise ValidationError("Dígito verificador do ISBN-13 incorreto.")
    else:
        raise ValidationError("O ISBN deve ter 10 ou 13 caracteres.")