import cmd

class Interface(cmd.Cmd):
    prompt = 'Command: '

    def do_foo(self, arg):
        print(arg)

interface = Interface()
interface.cmdloop()
