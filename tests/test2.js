try {
    console.log("require('test1')");
    var test1 = require('test1');
    console.log("test1=", test1.a, test1.b);
    var res = test1.a + test1.b;
    console.log("res=", res);
} catch ( e ) {
    console.log("error=", e);
}
