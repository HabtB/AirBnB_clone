#!/usr/bin/python3
""" a simple command line interface for the the BaseModel """
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)  "

    def do_quit(self, line):
        """Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """EOF command exits the program """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
