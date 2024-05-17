#!/usr/bin/python3
import cmd
import re
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class.
    """
    prompt = '(hbnb) '
    valid_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True
    
    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        return True

    def emptyline(self):
        """
        Do nothing when receiving an empty line
        """
        pass


    def default(self, line):
        """
        Method to be called when the command prefix is not recognized on an input line
        """
        if len(line) == 0:
            return
        match = re.match(r'(\w+)\.(\w+)\("([^"]*)"\)', line)
        if match:
            class_name, command, id = match.groups()
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return
            if command == "show":
                self.do_show(class_name + " " + id)
            elif command == "destroy":
                self.do_destroy(class_name + " " + id)
        else:
            match = re.match(r'(\w+)\.(\w+)\("([^"]*)", ({.*})\)', line)
            if match:
                class_name, command, id, attribute_dict = match.groups()
                if class_name not in self.valid_classes:
                    print("** class doesn't exist **")
                    return
                if command == "update":
                    try:
                        attribute_dict = eval(attribute_dict)
                        if not isinstance(attribute_dict, dict):
                            raise Exception()
                    except:
                        print("** attribute dictionary is invalid **")
                        return
                    for attribute_name, attribute_value in attribute_dict.items():
                        self.do_update(class_name + " " + id + " " + attribute_name + " " + str(attribute_value))
            else:
                print("** command not recognized **")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg in self.valid_classes:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key not in all_objs:
                print("** no instance found **")
            else:
                print(all_objs[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key not in all_objs:
                print("** no instance found **")
            else:
                del all_objs[key]
                storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        if arg and arg not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            for obj_id in all_objs:
                if not arg or arg == obj_id.split(".")[0]:
                    print(all_objs[obj_id])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = all_objs[key]
                try:
                    attr_type = type(getattr(obj, args[2]))
                    value = attr_type(args[3])
                except AttributeError:
                    try:
                        value = int(args[3])
                    except ValueError:
                        try:
                            value = float(args[3])
                        except ValueError:
                            value = str(args[3])
                setattr(obj, args[2], value)
                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

