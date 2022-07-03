#!/usr/bin/python3
"""program called console.py that contains the entry point of the command interpreter"""

import cmd
import sys, string
from models import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Cmd class
    """

    def __init__(self):
        """
        init
        """

        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "
        
    def do_quit(self, arg):
        """
        quit
        """
        sys.exit(1)

    def do_EOF(self, arg):
        """
        eof
        """
        sys.exit(1)

    def help_quit(self):
        print("syntax: quit")
        print("-- terminates the application")

    def help_EOF(self):
        print("syntax: EOF")
        print("-- terminates the application")

    def do_create(self, arg):
        """
        create class name
        """
        if arg == "":
            print("** class name missing **")
        elif arg not in storage.class_list():
            print("** class doesn't exist **")
        else:
            x = eval(arg)()
            x.save()
            print(x.id)

    def do_show(self, args):
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif (tokens[0] not in storage.class_list()):
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        else:
            k = tokens[0] + "." + tokens[1]
            dic = storage.all()
            try:
                print(dic[k])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, args):
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in storage.class_list():
            print("** class doesn't exist **")
        elif tokens[1] is None:
            print("** instance id missing **")
        else:
            k = tokens[0] + "." + tokens[1]
            dic = storage.all()
            try:
                storage.delete(k)
            except Exception:
                print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances"""
        tokens = arg.split()
        if len(tokens) == 0:
            l = list()
            for k, v in storage.all().items():
                l.append(str(v))
            print(l)
        else:
            if tokens[0] not in storage.class_list():
                print("** class doesn't exist **")
            else:
                l = list()
                for k, v in storage.all().items():
                    if v.__class__.__name__ == tokens[0]:
                        l.append(str(v))
                print(l)
    
    def do_update(self, args):
        """ Updates an instance based on the class name and id"""
        tokens = args.split()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in storage.class_list():
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        else:
            s = tokens[0] + "." + tokens[1]
            dic = storage.all()
            try:
                value = dic[s]
            except Exception:
                print("** no instance found **")
            if len(tokens) == 2:
                print("** attribute name missing **")
            elif value.tokens[2] is None:
                print("** value missing **")
            else:
                setattr(value, tokens[2], tokens[3])
                
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
