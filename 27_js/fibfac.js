//Team lobo
//SoftDev pd5
//K27 - Basic functions in JavaScript
//2025-01-06


//JavaScript implementations of Day0 recursive Scheme functions

//factorial:
let fact = function(n){
    if(n == 0){
        return 1;
    }
    return n * fact(n - 1)
}

//TEST CALLS
fact(7) == 5040

//fib:
let fib = function(n){
    if(n < 2){
        return n;
    }
    return fib(n - 1) + fib(n - 2)
}

//TEST CALLS
fib(10) == 55
