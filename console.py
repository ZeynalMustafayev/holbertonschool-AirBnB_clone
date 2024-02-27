#!/usr/bin/python3
"""Console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Hbnb console"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        return True
    
    def help_quit(self):
        print("Quit command to exit the program")
    
    def do_EOF(self, line):
        return True
    
    def emptyline(self):
        pass
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()