from .textEditor import TextEditor

from os import path


def display_options():
    print("""
    Display first line: (f)
    Display last line: (l)
    Display next line: (n)
    Display previous line: (p)
    Insert new line before: (b)
    Insert new line after: (a)
    Delete current line: (d)
    Replace current line: (r)
    Copy and paste line: (c)
    Replace word in line: (x)
    Save to text file: (s)
    Exit program: (q)
    """)


def main():
    while True:
        # Get filename from user
        text_file = input("Please input the path to the text file: ")
        if not text_file.endswith(".txt"):
            print("File does not end in .txt, please use valid ending")
        elif not path.exists(text_file):
            print("Could not find existing file with that name, writing new file: ")
            with open(text_file, mode="w") as _:
                pass
            break
        else:
            break

    # Instantiate the TextEditor
    text_editor = TextEditor(text_file=text_file)

    # Main event loop
    while True:
        display_options()
        cmd = input("Please input your command: ")
        if cmd == "f":
            print("Current line shows: ", text_editor.display_first_line())
        elif cmd == "l":
            print("Current line shows: ", text_editor.display_last_line())
        elif cmd == "n":
            print("Current line shows: ", text_editor.display_next_line())
        elif cmd == "p":
            print("Current line shows: ", text_editor.display_previous_line())
        elif cmd == "b":
            new_line = input("Please input the new line: ")
            print("Current line shows: ",
                  text_editor.insert_new_line_before(new_line))
        elif cmd == "a":
            new_line = input("Please input the new line: ")
            print("Current line shows: ",
                  text_editor.insert_new_line_after(new_line))
        elif cmd == "d":
            print("Current line shows: ", text_editor.delete_current_line())
        elif cmd == "r":
            new_line = input("Please input new line to replace with: ")
            print("Current line shows: ",
                  text_editor.replace_current_line(new_line))
        elif cmd == "c":
            print("Current line shows: ", text_editor.copy_and_paste_line())
        elif cmd == "x":
            old_word = input("Please input old word: ")
            new_word = input("Please input new word to replace with: ")
            print("Current line shows: ",
                  text_editor.replace_word_in_line(old_word, new_word))
        elif cmd == "s":
            text_editor.save_to_txt_file(text_file)
            print("File has been saved.")
        else:  # cmd == "q"
            print("Exiting")
            return


if __name__ == "__main__":
    main()
