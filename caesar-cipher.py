import re


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_list = list(alphabet)
base_adjuster = 3
regex = re.compile('[^0-9a-zA-Z]+')


def encode_string(input, interval):
    output = []
    message = list(input.upper())
    index_val = 0
    adjusted_val = ''

    for i in message:
        if regex.search(i):
            output.append(i)
        for j in alpha_list:
            if j == i:
                index_val = alpha_list.index(i) + base_adjuster
                if index_val >= len(alpha_list):
                    index_val = index_val - len(alpha_list)
                adjusted_val = alpha_list[index_val]
                output.append(adjusted_val)

    return str(output)


def decode_string(input, interval):
    output = ''
    return output



encoded_message = encode_string('Hello, how have you been?', base_adjuster)
decoded_message = decode_string(encoded_message, base_adjuster)

print(encoded_message)
