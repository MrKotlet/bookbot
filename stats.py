def get_num_words(text):
    split = text.split()
    return len(split)

def count_letters(text):
    low = ''.join(text.lower().split());
    lib = {}

    for l in low:
        if l in lib:
            lib[l] += 1
        else:
            lib[l] = 1

    return lib
def sort_letters(let_lib):
    arr = []
    for l in let_lib:
        arr.append({"l": l, "count": let_lib[l]})

    def get_count(letter):
        return letter["count"]

    arr.sort(key=get_count, reverse=True)
    return arr
