from os import path
from .cursor_based_list import CursorBasedList


class TextEditor:
    """A text editor based on implementation fo cursor based lists"""

    def __init__(self, text_file: str) -> None:
        if not path.exists(text_file):
            raise FileNotFoundError
        self.text_as_list: CursorBasedList = CursorBasedList()
        with open(text_file) as f:
            for line in f:
                self.text_as_list.insertAfter(line)
        if not self.text_as_list.isEmpty():
            # Reset to the first element
            self.text_as_list.first()

    def display_first_line(self) -> str:
        """Navigate to and display the first line."""
        if self.text_as_list.isEmpty():
            print("WARNING: Text file is currently empty")
            return
        self.text_as_list.first()
        return self.text_as_list.getCurrent()

    def display_last_line(self) -> str:
        """Navigate to and display the last line."""
        if self.text_as_list.isEmpty():
            print("WARNING: Text file is currently empty")
            return
        self.text_as_list.last()
        return self.text_as_list.getCurrent()

    def display_next_line(self) -> str:
        """Navigate and display the next line. If there is no next line, tell the user and don't change the current line."""
        if not self.text_as_list.hasNext():
            print("WARNING: Currently at the last line.")
            return self.text_as_list.getCurrent()
        self.text_as_list.next()
        return self.text_as_list.getCurrent()

    def display_previous_line(self) -> str:
        """Navigate and display the previous line."""
        if not self.text_as_list.hasPrevious():
            print("WARNING: Currently at the first line.")
            return self.text_as_list.getCurrent()
        self.text_as_list.previous()
        return self.text_as_list.getCurrent()

    def insert_new_line_before(self, new_line: str) -> str:
        """Insert a new line before the current line."""
        self.text_as_list.insertBefore(new_line)
        return self.text_as_list.getCurrent()

    def insert_new_line_after(self, new_line: str) -> str:
        """Insert a new line after the current line."""
        self.text_as_list.insertAfter(new_line)
        return self.text_as_list.getCurrent()

    def delete_current_line(self) -> str:
        """Delete the current line and have the line following become the current line. If there is no following line, the current line should be the last line."""
        self.text_as_list.remove()
        if not self.text_as_list.isEmpty():
            print("UPDATE: A line has been deleted. Currently on the next line")
        else:
            print("UPDATE: Currently on last line.")
        return self.text_as_list.getCurrent()

    def replace_current_line(self, new_line: str) -> str:
        """Replace the current line with a new line."""
        self.text_as_list.replace(new_line)
        return self.text_as_list.getCurrent()

    def copy_and_paste_line(self) -> str:
        """Insert a new line after the current line with the same line."""
        current_line = self.text_as_list.getCurrent()
        self.text_as_list.insertAfter(current_line)
        return self.text_as_list.getCurrent()

    def replace_word_in_line(self, old_word: str, new_word: str) -> str:
        """Replace a word input by the user in the current line by the new input word."""
        current_line = self.text_as_list.getCurrent()
        new_line = current_line.replace(old_word, new_word)
        self.replace_current_line(new_line)
        return self.text_as_list.getCurrent()

    def save_to_txt_file(self, output_file: str) -> None:
        """Save the current list back to a text file."""
        if not path.exists(output_file):
            raise FileNotFoundError
        with open(output_file, mode="w+") as f:
            # Go to the beginning of the list
            self.text_as_list.first()
            for i in range(len(self.text_as_list)):
                current_line = self.text_as_list.getCurrent()
                if not current_line.endswith("\n"):
                    f.write(self.text_as_list.getCurrent() + "\n")
                else:
                    f.write(self.text_as_list.getCurrent())
                # Update list pointer for all but the last iteration
                if i != len(self.text_as_list)-1:
                    self.text_as_list.next()
        print("File has been written.")
