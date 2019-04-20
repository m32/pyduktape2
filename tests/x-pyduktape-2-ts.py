#!/usr/bin/env vpython3
import os
import xenv
import duktape

ctx = duktape.Context()
ctx.set_globals(
    console = duktape.Console(),
)
code = '''\
class Greeter {
    constructor(public greeting: string) { }
    greet() {
        return "<h1>" + this.greeting + "</h1>";
    }
};

var greeter = new Greeter("Hello, world!");
'''
options = {
#    'module': 'abc',
    'target': 5,
    'newLine': 2,
}
result = duktape.compiler.typescript(ctx, code, **options)
print('*'*20, 'code='); print(code)
print('*'*20, 'result='); print(result)
