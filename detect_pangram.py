import string

pangrams = [
    "The quick brown fox jumps over the lazy dog.",
    "Cwm fjord bank glyphs vext quiz",
    "Pack my box with five dozen liquor jugs.",
    "How quickly daft jumping zebras vex.",
    "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ",
]

non_pangrams = [
    "This isn't a pangram!",
    "abcdefghijklm opqrstuvwxyz",
    "Aacdefghijklmnopqrstuvwxyz",
]


def is_pangram():
    for item in pangrams:
        return set(string.ascii_lowercase) <= set(item.lower())


if __name__ == "__main__":
    is_pangram()
