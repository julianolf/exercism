import itertools


def rails_iterator(rails):
    indexes = list(range(rails))
    it = itertools.cycle(indexes + indexes[1:-1][::-1])

    return it


def create_rail_fence(chars, rails):
    rail_fence = [""] * rails

    for rail, char in zip(rails_iterator(rails), list(chars)):
        rail_fence[rail] += char

    return rail_fence


def encode(message, rails):
    rail_fence = create_rail_fence(message, rails)

    return "".join(rail_fence)


def decode(encoded_message, rails):
    message_length = len(encoded_message)
    message_mask = "?" * message_length
    rail_fence = create_rail_fence(message_mask, rails)
    start_index = 0

    for idx, rail in enumerate(rail_fence):
        rail_length = len(rail)
        stop_index = start_index + rail_length
        rail_fence[idx] = list(encoded_message[start_index:stop_index])
        start_index += rail_length

    decoded_message = ""

    for idx in itertools.islice(rails_iterator(rails), message_length):
        decoded_message += rail_fence[idx].pop(0)

    return decoded_message
