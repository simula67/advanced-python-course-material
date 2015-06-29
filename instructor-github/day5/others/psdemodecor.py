__author__ = 'ravi'

def backup(f):
    def do_backup(*args, **kwargs):
        return f
    return do_backup


def inbox(param_decor=None):
    def handle_args(f):

       if param_decor:
            return f

       def do_decor(*args):
            return "{}\n{}\n{}".format('v'*5, f(args[0]), '^'*5)

       return do_decor
    return handle_args

@inbox(True)
def action(string_content):
    return string_content.title()

#print action
print action('peter pan')
