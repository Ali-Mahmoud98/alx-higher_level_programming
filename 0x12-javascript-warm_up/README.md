# 0x12. JavaScript - Warm up

Nice To read:
* [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Storing the information you need — Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
* [JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
* [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Operator precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
* [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
* [Functions — reusable blocks of code](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
* [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Module patterns](https://darrenderidder.github.io/talks/ModulePatterns/#/)
* [Video: var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
* [Videos: JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

Read:
* [JavaScript semistandard](https://github.com/standard/semistandard)

## files:
1- [0-javascript_is_amazing.js](0-javascript_is_amazing.js)
2- [1-multi_languages.js](1-multi_languages.js)
3- [2-arguments.js](2-arguments.js)
4- [3-value_argument.js](3-value_argument.js)
5- [4-concat.js](4-concat.js)
6- [5-to_integer.js](5-to_integer.js)
7- [6-multi_languages_loop.js](6-multi_languages_loop.js)
8- [7-multi_c.js](7-multi_c.js)
9- [8-square.js](8-square.js)
10- [9-add.js](9-add.js)
11- [10-factorial.js](10-factorial.js)
12- [11-second_biggest.js](11-second_biggest.js)
13- [12-object.js](12-object.js)
14- [13-main.js](13-main.js)
15- [13-add.js](13-add.js)
16- [100-main.js](100-main.js)
17- [100-let_me_const.js](100-let_me_const.js)

## 15. Call me Moby
**Files:** [101-call_me_moby.js](101-call_me_moby.js) | [101-main.js](101-main.js)

Write a function that executes `x` times a function.
* The function must be visible from outside
* Prototype: `function (x, theFunction)`
* You are not allowed to use `var`
```
guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ 
```
## 16. Add me maybe
**Files:** [102-add_me_maybe.js](102-add_me_maybe.js) | [102-main.js](102-main.js)

Write a function that increments and calls a function.
* The function must be visible from outside
* Prototype: `function (number, theFunction)`
* You are not allowed to use `var`
```
guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$ 
```
## 17. Increment object
**Files:** [103-object_fct.js](103-object_fct.js)

Update this script by adding a new function `incr` that increments the integer `value`.
* You are not allowed to use `var`
```
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$ 
```
