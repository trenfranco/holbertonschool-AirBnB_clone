#!/usr/bin/python3
"""program called console.py that contains the entry point of the command interpreter"""

import cmd
import sys, string
from models.base_model import BaseModel

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
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            x = eval(arg)()
            x.save()
            print(x.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
