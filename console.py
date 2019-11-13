#!/usr/bin/python3
"""
Command interpreter for the Hbnb
"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter
    """

    prompt = "(hbnb) "
    checkclass = ['BaseModel', 'User', 'State', 'City',
                  'Amenity', 'Place', 'Review']
    commands = ['create', 'show', 'update', 'all', 'destroy']

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        End of files exit
        """
        return True

    def emptyline(self):
        """
        Empty line don't execute anything
        """
        pass

    def do_create(self, args):
        """Create a new BaseModel, save to Json
        and print its id
        """
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.checkclass:
            print("** class doesn't exist **'")
        else:
            dic = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}
            command = dic[args]()
            print(command.id)
            command.save()

    def do_show(self, args):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        token = args.split()
        obj = storage.all()
        if len(token) == 0:
            print("** class name missing **")
            return
        if token[0] in HBNBCommand.checkclass:
            if len(token) > 1:
                key = token[0] + "." + token[1]
                if key in obj:
                    ob = obj[key]
                    print(ob)
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
         Deletes an instance based on the class name
         and id (save the change into the JSON file)
        """
        if not args:
            print("** class name missing **")
            return
        token = args.split(" ")
        objects = storage.all
        if args[0] not in HBNBCommand.checkclass:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            for key in objects.keys():
                if key == token[1]:
                    del objects[key]
                    storage.save()
                    break
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
         Prints all string representation of all
         instances based or not on the class name
        """
        token = args.split()
        objects = storage.all()
        for key in objects.keys():
            if token:
                if token[0] not in HBNBCommand.checkclass:
                    print("** class doesn't exist ** ")
                    return
                if token[0] == objects[key].__dict__['__class__']:
                    print(objects[key])
            else:
                print(objects[key])

    def do_update(self, args):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute (save the change
        into the JSON file)
        """
        if not args:
            print("** class name missing **")
            return
        token = args.split(" ")
        objects = storage.all()
        if token[0] not in HBNBCommand.checkclass:
            print("** class doesn't exist **")
            return
        if len(token) < 2:
            print("** instance id missing **")
            return
        name = token[0] + "." + token[1]
        if name not in objects:
            print("** no instance found **")
            return
        elif name in objects:
            obj = objects[name]
            nomod = ["id", "created_at", "updated_at"]
            if obj:
                if len(token) < 3:
                    print("** attribute name missing **")
                elif len(token) < 4:
                    print("** value missing **")
                elif token[2] not in nomod:
                    obj.__dict__[token[2]] = token[3]
                    obj.updated_at = datetime.now()
                    storage.save()
        else:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
