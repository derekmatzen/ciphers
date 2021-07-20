import re


# input to encode
user_sentence = 'The quick brown fox jumps over the lazy dog.'
# shift sequence for encoding - accepts values: 1-25
base_adjuster = 3

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_list = list(alphabet)
# regex for non-alphanumeric values
regex = re.compile('[^0-9a-zA-Z]+')


def encode_string(input, interval):
    # encodes a message based on the base_adjuster shift sequence

    output = []
    message = list(input.upper())
    index_val = 0
    adjusted_val = ''

    for i in message:
        if regex.search(i):
            # adds non-alphanumeric value to output message
            output.append(i)

        for j in alpha_list:
            if j == i:
                index_val = alpha_list.index(i) + interval

                # resets index if input value is at end of alphabet sequence
                if index_val >= len(alpha_list):
                    index_val = index_val - len(alpha_list)

                adjusted_val = alpha_list[index_val]
                output.append(adjusted_val)

    encoded_text = ' '.join([str(i) for i in output])

    return encoded_text


def decode_string(input, interval):
    # decodes a message based on the base_adjuster shift sequence
    
    output = []
    message = list(input.upper())
    index_val = 0
    adjusted_val = ''

    for i in message:
        if regex.search(i):
            # adds non-alphanumeric value to output message
            output.append(i)

        for j in alpha_list:
            if j == i:
                index_val = alpha_list.index(i) - interval
                adjusted_val = alpha_list[index_val]
                output.append(adjusted_val)

    decoded_text = ''.join([str(i) for i in output])

    return decoded_text



encoded_message = encode_string(user_sentence, base_adjuster)
decoded_message = decode_string(encoded_message, base_adjuster)

print(encoded_message)
print(decoded_message)
