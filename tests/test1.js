exports.a = 1;
exports.b = 2;
//console.log(exports,require,module,__filename,__dirname)
console.log('test1.js loaded', __filename, __dirname)
exports.aplusbic = function (a, b, c){
    return a+b+c;
}
