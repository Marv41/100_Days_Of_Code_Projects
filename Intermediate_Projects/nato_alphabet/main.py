import pandas

#Example
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#How to Loop through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

#Create Data Frame from dictionary
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key : new_value for (index, row) in df.iterrows()}


nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter : row.code for (index,row) in nato_alphabet.iterrows()}


while True:
    user_input = input("Please Type Any Word: ").upper()

    try:
        phonetic_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letter in the alphabet please")
    else:
        print(phonetic_list)
        break