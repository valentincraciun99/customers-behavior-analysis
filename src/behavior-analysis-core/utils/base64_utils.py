import base64
import binascii


def Decode(input):
    base64_input_bytes = binascii.a2b_base64(input)
    return base64_input_bytes


def Array_To_Base64_String(array) -> str:
    sample_string = "".join([str(item) + "," for item in array])
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    return base64_string
