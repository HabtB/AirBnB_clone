#!/usr/bin/python3
""" a simple command line interface for the the BaseModel """
import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ a simple command line interface for the the BaseModel """
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
        elif class_name not in storage.class_names():
            print("** class doesn't exist **")
        else:
            class_type = storage.class_names()[class_name]
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

            if class_list[0] not in storage.class_names():
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
        objdict = storage.all()
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in storage.class_names():
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(line[0], line[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(line[0], line[1])]
            storage.save()

    def do_all(self, line):
        """Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        objdict = storage.all()
        if line == "":
            for key, value in objdict.items():
                print(value)
        elif line in storage.class_names():
            for key, value in objdict.items():
                if line in key:
                    print(value)
        else:
            print("** class doesn't exist **")

    # def do_update(self, line):
    #     """Update command updates instances based on the class name and id"""
    #     objdict = storage.all()
    #     line = line.split()
    #     if len(line) == 0:
    #         print("** class name missing **")
    #     elif line[0] not in storage.class_names():
    #         print("** class doesn't exist **")
    #     elif len(line) == 1:
    #         print("** instance id missing **")
    #     elif "{}.{}".format(line[0], line[1]) not in objdict.keys():
    #         print("** no instance found **")
    #     elif len(line) == 2:
    #         print("** attribute name missing **")
    #     elif len(line) == 3:
    #         print("** value missing **")
    #     else:
    #         objdict["{}.{}".format(line[0], line[1])].__dict__[line[2]] = \
    #             line[3].replace("_", " ")
    #         storage.save()

    def do_update(self, line):
        """Update command updates instances based on the class name and id"""
        objdict = storage.all()
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in storage.class_names():
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(line[0], line[1]) not in objdict.keys():
            print("** no instance found **")
        elif len(line) == 2:
            print("** attribute name missing **")
        elif len(line) == 3:
            print("** value missing **")
        elif line[2] in ['id', 'created_at', 'updated_at']:
            print("** attribute name can't be updated **")
        elif len(line) > 4:
            print("** too many arguments **")
        else:
            instance = objdict["{}.{}".format(line[0], line[1])]
            try:
                # Check if the value is of string type
                if line[3].startswith('"') and line[3].endswith('"'):
                    value = line[3][1:-1]
                # Check if the value is of integer type
                elif line[3].isdigit():
                    value = int(line[3])
                # Check if the value is of float type
                else:
                    value = float(line[3])
            except ValueError:
                print("** value is not a valid type **")
            else:
                setattr(instance, line[2], value)
                instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
