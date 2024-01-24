// if (5>9) {
//     console.log('yes')
// } else {
//     console.log('no')
// }
// if (5>8) console.log('fgfdgf')

// if (5>9) {
//     console.log('yes')
// } else if (3<7) {
//     console.log('no')
// } else if (18+5 > 16){
//     console.log('fdfsfsdf')
// } else {
//     console.log('sfgdhfnmgjmhngfd')
// }

// let a = 1;
// switch (a){
//     case 1:
//         console.log(1);
//         break;
//     case 2:
//         console.log(2);
//         break;
//     case 3:
//         console.log(3);
//         break;
//     default:
//         console.log('error')

// }


// a = 15 if a>5 else 0

// let state = 9 + 15 < 3;
// let a = state  ? console.log('yes') :
//     (2 > 6) ? console.log('jdlgjoa') :
//     (2 * 9 == 3) ? console.log('sdhfdsjdt') : console.log(false)



// let i = 0 ;
// while (i< 6) console.log(i++)
// do {
//     console.log(i--)

// }while(i>0)


// for (var i = 0; i<10; i++){
//     console.log(i);
// };


// let array = [45 , 34 , 65 , 23 , 56 ]
// let array = {
//     'name' : 'Vasya',
//     'age' : 18,
//     'email' : 'dgfhgdgg.ru'
// }
// for (let i in array){
//     if (i==2){
//         continue;
//     }
//     console.log(i,array[i]);
// }

// for (let i = 0; i<5; i++){
//     first: for (let j=0; j<10; j++);
// }


// def summ(a,b)
//   return a+b]

// function first(x){
//     return  x
// }
// function second(x){
//     return  x
// }
// console.log(summ(2, 3 , first , second ))
// var rez;
// function summ (a=0,b=0,first,second){
//     var one, two;

//     one = first(a);
//     two = second(b)
//     rez = one+two;
//     return one+two
// }
// console.log

// Function Declaration
function sum(a,b){
    return a+b
}

let a = sum
console.log(a(5,9))

// Function Expression

let sum2 = function (a , b){
    return a+b

}
console.log(sum2(1,2))

// Arrow Function

let sum3 = (a , b) => {
    return a+b
}

console.log(sum3(8,2))

// setTimeout(sum,1000,2,3)
let f = setInterval(sum, 1000,2,3)