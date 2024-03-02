#!/usr/bin/python3
"""Console"""
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd
import json


class HBNBCommand(cmd.Cmd):
    """Hbnb console"""
    prompt = "(hbnb) "

    class_names = ["BaseModel", "User", "State",
                   "City", "Amenity", "Place", "Review"]

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
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return

        parts = line.split()

        if parts[0] not in self.class_names:
            print("** class doesn't exist **")
            return

        if len(parts) < 2:
            print("** instance id missing **")
            return

        class_name, instance_id = parts[0], parts[1]

        try:
            with open("file.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        key_to_show = "{}.{}".format(class_name, instance_id)

        if key_to_show not in data:
            print("** no instance found **")
            return

        value = eval(key_to_show.split(".")[0])(**data[key_to_show])
        print(value)

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return

        parts = line.split()

        if parts[0] not in self.class_names:
            print("** class doesn't exist **")
            return

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

    def do_all(self, line):
        if not line:
            try:
                with open("file.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = {}

            arr = []
            for k in data.keys():
                value = eval(k.split(".")[0])(**data[k])
                arr.append(value.__str__())

            print(arr)
        else:
            try:
                with open("file.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = {}

            arr = []
            if line not in self.class_names:
                print("** class doesn't exist **")
                return

            for k in data.keys():
                if (k.split(".")[0] == line):
                    value = eval(k.split(".")[0])(**data[k])
                    arr.append(value.__str__())

            print(arr)

    def do_update(self, line):
        if not line:
            print("** class name missing **")
            return

        parts = line.split()

        if parts[0] not in self.class_names:
            print("** class doesn't exist **")
            return
        if len(parts) < 2:
            print("** instance id missing **")
            return
        if len(parts) < 3:
            print("** attribute name missing **")
            return
        if len(parts) < 4:
            print("** value missing **")
            return

        class_name, id_val, attribute, value = (parts[0], parts[1],
                                                parts[2], parts[3])

        try:
            with open("file.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        key_for_find = "{}.{}".format(class_name, id_val)
        if key_for_find not in data:
            print("** no instance found **")
            return

        obj = eval(key_for_find.split(".")[0])(**data[key_for_find])
        setattr(obj, attribute, value.strip('"'))

        data[key_for_find] = obj.to_dict()
        with open("file.json", "w") as f:
            json.dump(data, f)

    def default(self, line):
        tokens = line.split('.')
        if len(tokens) == 2:
            class_name = tokens[0]
            if class_name in self.class_names:
                if tokens[1] == "all()":
                    self.do_all(class_name)
                elif tokens[1] == "count()":
                    count = 0
                    for k in storage.all().keys():
                        if (class_name == k.split(".")[0]):
                            count += 1
                    print(count)
                
                elif tokens[1].startswith("show"):
                    instance_id = tokens[1].split("(")[1].split(")")[0]
                    self.do_show(tokens[0] + " " + instance_id)
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax:", line)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
