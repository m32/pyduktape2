#!/usr/bin/env vpython3
import xenv
import duktape

ctx = duktape.Context()
ctx.set_globals(console=duktape.Console())
ctx.loader.register_path('..')
ctx.eval_js_file('../tests/test0.js')
ctx.eval_js('require("tests/test2")')
try:
    ctx.eval_js('require("/test2")')
except duktape.JSError as err:
    print('error=',err)
print('done')
vv = ctx.eval_js('var test1 = require("tests/test1"); test1')
print('vv = ', vv)
print('vv.aplusbic(1, 2, 3)=', vv.aplusbic(1, 2, 3))
v = ctx.get_global('test1')
print('v = ', v)
print('v.aplusbic(1, 2, 3)=', v.aplusbic(1, 2, 3))
