#!/usr/bin/python3
"""contains the entry point of the command interpreter:"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter for performing
    quick actions on the hbnb web app"""
    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'Place',
               'State', 'City', 'Amenity', 'Review']

    def do_quit(sef, args):
        """exits the interpreter"""
        return True

    def do_EOF(self, args):
        """same as quit, but responds to ^d from the keyboard"""
        return True

    def emptyline(self):
        """overrides the default action when an empty line is passed"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        elif args[0] == 'BaseModel':
            b = BaseModel()
            print(b.id)
            b.save()
        elif args[0] == 'User':
            b = User()
            print(b.id)
            b.save()
        elif args[0] == 'City':
            b = City()
            print(b.id)
            b.save()
        elif args[0] == 'Amenity':
            b = Amenity()
            print(b.id)
            b.save()
        elif args[0] == 'State':
            b = State()
            print(b.id)
            b.save()
        elif args[0] == 'Place':
            b = Place()
            print(b.id)
            b.save()
        elif args[0] == 'Review':
            b = Review()
            print(b.id)
            b.save()

    def do_show(self, args):
        """Prints the string representation
        of an instance based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj = f"{args[0]}.{args[1]}"
            instances = storage.all()
            if obj in instances.keys():
                actual_obj = instances[obj]
                print(actual_obj)
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class
        name and id (save the change into the JSON file)."""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj = f"{args[0]}.{args[1]}"
            instances = storage.all()
            if obj in instances.keys():
                del instances[obj]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all
        instances based or not on the class name. """
        if args != '' and args not in self.__class__.classes:
            print("** class doesn't exist **")
            return
        instances = storage.all()
        attributes = []
        if args == '':
            attributes = list(instances.values())
        else:
            for i in instances.values():
                if i.__class__.__name__ == args:
                    attributes.append(i)
        strrep = []
        for attr in attributes:
            strrep.append(str(attr))
        print(strrep)

    def do_update(self, args):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        args = args.split()
        larg = len(args)
        if larg == 0:
            print("** class name missing **")
        elif args[0] not in self.__class__.classes:
            print("** class doesn't exist **")
        elif larg < 2:
            print("** instance id missing **")
        elif larg < 3:
            print("** attribute name missing **")
        elif larg < 4:
            print("** value missing **")
        else:
            obj = f"{args[0]}.{args[1]}"
            instances = storage.all()
            if obj in instances.keys():
                actual_obj = instances[obj]
                if args[3].startswith('"') or args[3].startswith("'"):
                    new_attr = str()
                    for i in args[3:]:
                        new_attr = f"{new_attr} {i}"
                        if i.endswith("'") or i.endswith('"'):
                            break
                    new_attr = new_attr[2:-1]
                    actual_obj.__dict__[args[2]] = new_attr
                else:
                    actual_obj.__dict__[args[2]] = args[3]
                storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
