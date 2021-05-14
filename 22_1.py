def encrypt_caesar(msg, shift=3):
    lowercase_char_1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    uppercase_char_1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    shift = shift % len(lowercase_char_1)
    lowercase_char_2 = lowercase_char_1[shift:] + lowercase_char_1[:shift]
    uppercase_char_2 = uppercase_char_1[shift:] + uppercase_char_1[:shift]
    translation = msg.maketrans(lowercase_char_1 + uppercase_char_1, lowercase_char_2 + uppercase_char_2)
    return msg.translate(translation)


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -1 * shift)
