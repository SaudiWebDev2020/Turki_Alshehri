


function makeItBig(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            arr[i] = 'big';
        }
    }

    return arr;
}

console.log(makeItBig([1,-2,90,-3,-7]));

/* ------------------------------------------------ */

function printLowHigh(arr) {
    var high = arr[0];
    var low = arr[0];
    for (var i = 1; i < arr.length; i++) {
        if (high < arr[i]) {
            high = arr[i];
        }

        if (low > arr[i]) {
            low = arr[i];
        }
    }

    console.log("HIGH: ", high, " LOW: ", low);
}

printLowHigh([1,-2,90,-3,-7]);
/* ------------------------------------------------ */


/* ------------------------------------------------ */

function printOneReturnAnother(arr) {
    var odd = 0;
    for (var i = 0; i < arr.length; i++) {
        if (i >= 1) {
            console.log(arr[i])
        }

        if (odd == 0) {
            if (arr[i] % 2 != 0) {
                odd = arr[i];
            }
        }
    }
    console.log(odd);
}


printOneReturnAnother([2,4,5,6,7]);

/* ------------------------------------------------ */

/* ------------------------------------------------ */

function doubleVision(arr) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++) {
        newArr.push(arr[i] * 2);
    }

    return newArr;
}

console.log(doubleVision([2,4,5,6,7]));
/* ------------------------------------------------ */

/* ------------------------------------------------ */

function countPositives(arr) {
    var counter = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            counter++;
        }
    }
    arr[arr.length - 1] = counter;
    return arr;
}

console.log(countPositives([2,-4,5,6,7]));
/* ------------------------------------------------ */

/* ------------------------------------------------ */

function evensAndOdds(arr) {
    var oc = 0, ec = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 == 0) {
            ec++;
            oc = 0;
        } else {
            oc++
            ec = 0;
        }

        if (ec == 3) {
            console.log("Even more so!");
            ec = 0;
        }

        if (oc == 3) {
            console.log("That's odd!");
            oc = 0;
        }
    }
}

evensAndOdds([2,2,2,5,7,2,1,1,1]);

/* ------------------------------------------------ */

/* ------------------------------------------------ */

function incrementTheSeconds(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (i % 2 != 0) {
            arr[i] += 1;
        }
        console.log(arr[i]);
    }
    return arr;
}

incrementTheSeconds([1,2,3,4,5,6]);
/* ------------------------------------------------ */

/* ------------------------------------------------ */

function previousLengths(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
        arr[i] = arr[i - 1].length;
    }

    return arr;
}


previousLengths(["hello", "dojo", "awesome"]);
/* ------------------------------------------------ */

/* ------------------------------------------------ */

function addSeven(arr) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++) {
        newArr.push(arr[i] + 7)
    }

    return newArr;
}

console.log(addSeven([1,2,3]));

/* ------------------------------------------------ */

/* ------------------------------------------------ */

function reverse(arr) {
    for (var i = 0, j = arr.length - 1; i <= j; i++, j--) {
        var tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    return arr;
}


console.log(reverse([3,1,6,4,2]));
/* ------------------------------------------------ */

/* ------------------------------------------------ */

function outlookNegative(arr) {
    var newArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            newArr.push(arr[i] * -1)
        } else {
            newArr.push(arr[i])
        }
    }

    return newArr;
}


console.log(outlookNegative([-3,2,4]));
/* ------------------------------------------------ */

/* ------------------------------------------------ */

function alwaysHungry(arr) {
    var food = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] == 'food') {
            console.log("yummy")
            food = 1;
        } 
    }

    if (!food) {
        console.log("I'm hungry");
    }
}

alwaysHungry(['banna', 'no', 'fod']);

/* ------------------------------------------------ */

/* ------------------------------------------------ */

function swapTowardCenter(arr) {
    for (var i = 0, j = arr.length - 1; i <= j; i += 2, j -=2) {
        var tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
    return arr;
}
swapTowardCenter([true,42,"Ada",2,"pizza"]);

/* ------------------------------------------------ */

/* ------------------------------------------------ */

function scaleTheArray(arr, num) {
    for (var i = 0; i < arr.length; i++) {
        arr[i] *= num;
    }

    return arr;
}

console.log(scaleTheArray([1,2,3,4,5,6], 2));
/* ------------------------------------------------ */