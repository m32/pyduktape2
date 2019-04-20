BABEL_COMPILER = 'babel-6.26.0.min.js'
COFFEE_COMPILER = 'coffeescript.js'
TSC_COMPILER = 'typescriptServices.js'
TSC_OPTIONS = '{ module: ts.ModuleKind.System, target: ts.ScriptTarget.ES5, newLine: 1 }'


def babel(ctx, source, **kwargs):
    """Compiles the given ``source`` from ES6 to ES5 usin Babeljs"""
    presets = kwargs.get('presets', ["es2015"])
    compiler = ctx.eval_js('require("%s")' % BABEL_COMPILER)
    result = compiler.transform(source, presets)
    return result


def jsx(ctx, source, **kwargs):
    kwargs['presets'] = ['es2015', 'react']
    return babel(ctx, source, **kwargs)['code']


def coffee(ctx, source):
    compiler = ctx.eval_js('require("%s")' % COFFEE_COMPILER)
    result = compiler.compile(source)
    return result


def typescript(ctx, source, **options):
    compiler = ctx.eval_js('require("%s")' % TSC_COMPILER)
    result = compiler.transpile(source, options, 'a.ts', True, 'aa')
    return result
