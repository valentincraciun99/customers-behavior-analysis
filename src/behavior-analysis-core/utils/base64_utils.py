import binascii


def Decode(input):
    base64_input_bytes = binascii.a2b_base64(input)
    return base64_input_bytes
