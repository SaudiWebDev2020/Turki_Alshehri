function sigma(num) {
    var sum = 0;
    var counter = num;
    while(counter > 0) {
        sum += counter;
        counter--;
    }
    console.log(sum);
}

sigma(6);

// -------------------------

function factorial(num) {
    var result = 1;
    for (var index = 1; index <= num; index++) {
        result *= index;
    }
    console.log(result);
}

factorial(3);

//-------------------------

function secondToLast(arr) {
    if (arr.length > 1) {
        return arr[arr.length - 2]
    } 
    else {
        return null;
    }
}

console.log(secondToLast([4,2]));

//-------------------------

function nthToLast(arr, n) {
    if (arr.length > 1 && (arr.length - n) > 1) {
        return arr[arr.length - n]
    } 
    else {
        return null;
    }
}

console.log(nthToLast([5,2,3,6,4,9,7],3));


//-------------------------

function secondLargest(arr) {
    var max = arr[0];
    var secondMax = arr[arr.length - 1];

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > secondMax &&  arr[i] != max) {
            secondMax = arr[i];
        }
    }
    return secondMax;
}

console.log(secondLargest([554,456,3,23244,55,3,66,72]));

//-------------------------

function doubleTrouble(arr) {
    var newArr = [];
    var j = 0;
    for (let i = 0; i < arr.length; i++) {
        newArr[j++] = arr[i];
        newArr[j++] = arr[i];
    }

    console.log(newArr);
}

doubleTrouble(["hello",1,2,3, "Dojos"]);


//-------------------------

