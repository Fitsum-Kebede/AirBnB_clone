#!/usr/bin/python3
""" entry point for the command interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, line):
        """quit the console"""
        return True

    def do_EOF(self, line):
        """ quit the console"""
        print("")
        return True

    def emptyline(self):
        """ does not excute anything """
        pass

    def help_quit(self):
        """ Quit command to exit the program """
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
