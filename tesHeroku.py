import sys

while True:
    quest = input("apakah anda ingin belajar Heroku? (yes/no)\n")
    if quest == "yes":
        print("Hello World!!!")
        break
    elif quest == "no":
        sys.exit("bye!!!")
    else:
        print("ulangi jawaban anda!!!")

