#!/usr/bin/python3
"""Console"""
import cmd
from models.base_model import BaseModel
import json


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

    def do_create(self, line):
        if line != "":
            try:
                new_cls = eval(line.split()[0])()
                new_cls.save()
                print(new_cls.id)
            except:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        if line == "":
            print("** class name missing **")
            return
        with open("file.json", "r") as f:
            for key, value in json.load(f).items():
                if key.split(".")[0] != line.split()[0]:
                    print("** class doesn't exist **")
                    return
                if len(line.split()) == 1:
                    print("** instance id missing **")
                    return
                if value["id"] != line.split()[1]:
                    print("** no instance found **")
                    return
                value = eval(key.split(".")[0])(**value)
                print(value)


    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return

        parts = line.split()
        if len(parts) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = parts[0], parts[1]

        try:
            with open("file.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        key_to_delete = "{}.{}".format(class_name, instance_id)

        if key_to_delete not in data:
            print("** no instance found **")
            return

        del data[key_to_delete]

        with open("file.json", "w") as f:
            json.dump(data, f)




    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
