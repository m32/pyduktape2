import os
from pyduktape2 import DuktapeContext, JSError, JSProxy, DuktapeThreadError
from . import module_loader

class Console(object):
    def __init__(self):
        pass

    def log(self, *args):
        print(args)

class Context(DuktapeContext):
    def __init__(self):
        super(Context, self).__init__()
        self.loader = module_loader.JSModuleLoader()

    def get_module(self, module_id, parent_id):
        parent_id = parent_id.decode('utf-8')
        module_id = module_id.decode('utf-8')
        #print('get_module', module_id, parent_id)
        res = self.loader.lookup(parent_id, module_id)
        res = res.encode('utf-8')
        #print('get_module=', res)
        return res

    def load_module(self, module_id):
        #print('load_module', module_id)
        with open(module_id, 'r', encoding='utf-8') as f:
            code = f.read()
        code = code.encode('utf-8')
        #print('load_module', len(code))
        return code
