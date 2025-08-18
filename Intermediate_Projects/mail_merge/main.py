


with open("./input/names/invited_names.txt", mode="r") as names:
    names = names.readlines()


with open("./input/letters/starting_letter.txt", mode="r") as letter:
    original_letter = letter.read()
    for name in names:
        fname = name.strip()
        updated_letter = original_letter.replace("[name]", fname)
        with open(f"./output/ready_to_send/letter_for_{fname}.txt", mode="w") as new_letter:
            new_letter.write(updated_letter)



