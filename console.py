#!/usr/bin/python3
"""
entry point of the command interpreter
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter
    """

    prompt = "(hbnb) "

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

HBNBCommand().cmdloop()
