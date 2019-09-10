#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i, weight in enumerate(weights):
        pair_limit = limit - weight
        have_pair = hash_table_retrieve(ht, pair_limit)

        if have_pair is not None:
            if (i > have_pair):
                return (i, have_pair)
            else:
                return (have_pair, i)
        else:
            hash_table_insert(ht, weight, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
