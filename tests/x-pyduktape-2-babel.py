#!/usr/bin/env vpython3
import xenv
import duktape

ctx = duktape.Context()
ctx.set_globals(
    console = duktape.Console(),
)
babeljs = 'babel-6.26.0'
ctx.eval_js('var bcc = require("%s")' % babeljs)
bcc = ctx.get_global('bcc')
presets = ['es2015']
bcc = ctx.get_global('bcc')
code = '''\
// Expression bodies
var odds = evens.map(v => v + 1);
var nums = evens.map((v, i) => v + i);
var pairs = evens.map(v => ({even: v, odd: v + 1}));

// Statement bodies
nums.forEach(v => {
  if (v % 5 === 0)
    fives.push(v);
});

// Lexical this
var bob = {
  _name: "Bob",
  _friends: [],
  printFriends() {
    this._friends.forEach(f =>
      console.log(this._name + " knows " + f));
  }
}
'''
if 0:
    result = bcc.transform(code, presets)
    print('dir result', dir(result))
    print('result.map', result.map)
    print('result.code', result.code)
bcc = ctx.set_globals(code=code)
ctx.eval_js('''
console.log('code='+code);
var options = {
    ast: false,
    code: true,
    presets: ["es2015", "es2016", "es2017"],
    plugins: ["transform-runtime"]
};
var bres = bcc.transform(code, options);
var res = {map: bres.map, code: bres.code};
console.log('map='+bres.map);
console.log('code='+bres.code);
''')
