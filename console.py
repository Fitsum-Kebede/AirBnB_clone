#!/usr/bin/python3
""" entry point for the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage

class_list = {
    "BaseModel": BaseModel
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id

        args:
            line: inputline containing the create command followed by
            the name of the class (BaseModel)
        """
        if not line:
            print("** class name missing **")
            return False
        if line in class_list:
            class_obj = class_list[line]()
            class_obj.save()
            print(class_obj.id)
        else:
            print("** class doesn't exist **")
            return False

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id

        args:
            line: input line  format (show className instanceid)
        """
        if not line:
            print("** class name missing **")
            return False
        else:
            args = line.split(" ")
            if args[0] in class_list:
                if len(args) != 2:
                    print("** instance id missing **")
                    return False
                data = storage.all()
                obj = ""
                for obj_id in data.keys():
                    instance_id = obj_id.split(".")[1]
                    if args[1] == instance_id:
                        obj = data[obj_id]
                        break
                if obj:
                    print(obj)
                else:
                    print("** no instance found **")
                    return False
            else:
                print("** class doesn't exist **")
                return False

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        if not line:
            print("** class name missing **")
            return False
        else:
            args = line.split(" ")
            if args[0] in class_list:
                if len(args) != 2:
                    print("** instance id missing **")
                    return False
                data = storage.all()
                is_deleted = False
                for obj_id in data.keys():
                    instance_id = obj_id.split(".")[1]
                    if args[1] == instance_id:
                        del data[obj_id]
                        storage.save()
                        is_deleted = True
                        break
                if not is_deleted:
                    print("** no instance found **")
                    return False
            else:
                print("** class doesn't exist **")
                return False

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name. Ex: $ all BaseModel or $ all.
        """
        args = line.split(" ")
        data = storage.all()
        result = []
        if line:
            if args[0] in class_list:
                pass
            else:
                print("** class doesn't exist **")
                return False
        for obj in data.keys():
            instance_type = obj.split(".")[0]
            if args[0] and args[0] == instance_type:
                result.append(str(data[obj]))
            else:
                result.append(str(data[obj]))
        print(result)

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
