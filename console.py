#!/usr/bin/python3
"""
program called console.py
"""

import cmd
import sys
import string
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import ast


class HBNBCommand(cmd.Cmd):
    """
    Cmd class
    """
    if sys.stdin and sys.stdin.isatty():
        prompt = "(hbnb) "

    else:
        prompt = "(hbnb) \n"

    def precmd(self, args):
        args = args.replace('"', "")
        return (args)

    def do_quit(self, arg):
        """
        quit
        """
        return True

    def do_EOF(self, arg):
        """
        eof
        """
        return True

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
            l2 = list()
            for k, v in storage.all().items():
                l2.append(str(v))
            print(l2)
        else:
            if tokens[0] not in storage.class_list():
                print("** class doesn't exist **")
            else:
                l2 = list()
                for k, v in storage.all().items():
                    if v.__class__.__name__ == tokens[0]:
                        l2.append(str(v))
                print(l2)

    def do_update(self, args):
        """ Updates an instance based on the class name and id"""
        tokens = args.split()
        dic = storage.all()
        if len(tokens) == 0:
            print("** class name missing **")
        elif tokens[0] not in storage.class_list():
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        else:
            s = tokens[0] + "." + tokens[1]
            try:
                value = dic[s]
            except Exception:
                print("** no instance found **")
            if len(tokens) == 2:
                print("** attribute name missing **")
            elif len(tokens) == 3:
                print("** value missing **")
            else:
                tokens[3].replace('"', "")
                setattr(dic[s], tokens[2], tokens[3])
                storage.save()

    def advanced(self, arg):
        """Method called when input does not match any do_* commands"""
        count = 0
        try:
            args = line.split('.')
            classs = args[0]
            command = args[1]
            if command == 'all()':
                self.do_all(classs)
                return
            elif command == 'count()':
                for instances in storage.all():
                    if instances.split(".")[0] == classs:
                        count += 1
                print(count)
                return
            return
        except Exception:
            print(f"*** Unknown syntax {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
