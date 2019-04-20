#!/usr/bin/env vpython3
import xenv
import duktape

ctx = duktape.Context()
ctx.set_globals(console=duktape.Console())
ctx.eval_js('str = "Hello, World!";')
res = ctx.get_global('str')
print('js global var str=', res)
