#!/usr/bin/python3
import cmd
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
        inputs = line.split('.')
        class_name = inputs[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(inputs) > 1:
            command = inputs[1]
            if command == "all()":
                self.do_all(class_name)
            elif command == "count()":
                self.do_count(class_name)

    def do_count(self, arg):
        """
        To count the number of instances of a class
        """
        count = 0
        all_objs = storage.all()
        for obj_id in all_objs:
            if arg == obj_id.split(".")[0]:
                count += 1
        print(count)

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        if not arg:
            print("** class name missing **")
        elif arg in self.valid_classes:
            new_instance = globals()[arg]
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
        Updates an instance based on the class name and id by adding or updating attribute (save
        the change into the JSON file).
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key not in all_objs:
                print("** no instance found **")
            else:
                setattr(all_objs[key], args[2], args[3])
                all_objs[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
