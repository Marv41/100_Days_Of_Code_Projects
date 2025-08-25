#FileNotFound

# try:
#     file = open("aFile.txt")
#     adict = {"key" : "value"}
#     print(adict["key"])
# except FileNotFoundError:
#     file = open("afile.txt", "w")
#     file.write("somthing")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("THis is an error that I made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight / height ** 2



