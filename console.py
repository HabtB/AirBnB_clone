#!/usr/bin/python3
""" a simple command line interface for the the BaseModel """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)  "

    def do_quit(self, line):
        """Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """EOF command exits the program """
        return True

    def do_create(self, line):
        """Create command creates a new instance of the BaseModel \
saves it (to the JSON file) and prints the id.
        """
        class_name = line.strip()

        if not line:
            print("** class name missing **")
        elif class_name not in storage.class_def():
            print("** class doesn't exist **")
        else:
            class_type = storage.class_def()[class_name]
            instance = class_type()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Show command prints the string representation of an instance \
based on the class name and id"""

        if not line:
            print("** class name missing **")
        else:
            class_list = line.split()
                
            if class_list[0] not in storage.class_def():
                print("** class doesn't exist **")
            elif (len(class_list) < 2):
                    print("** instance id missing **")
            else: 
                key = f"{class_list[0]}.{class_list[1]}"
                instance = storage.all().get(key)

                if not instance:
                    print("** no instance found **")
                else:
                    print(instance)

    def do_destroy(self, line):
        """Destroy command deletes the instance based on the class name and id
        """

    def do_all(self, line):
        """All command prints string representation of all instances"""

    def do_update(self, line):
        """Update command updates instances based on the class name and id"""
if __name__ == "__main__":
    HBNBCommand().cmdloop()
