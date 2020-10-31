function return1to255() {
    var arr = [];
    for(var i = 1; i <=255; i++){    
        arr.push(i);
    }
    return arr;
}

console.log(return1to255());

/*-----------------------------------------*/

function sumOfEvens() {
    var sum = 0;
    for(var i = 1; i <= 1000; i++){ 
        if(i % 2 == 0){
            sum += i;
        } 
    }

    return sum;
}

console.log(sumOfEvens());

/*-----------------------------------------*/

function sumOfOdds() {
    var sum = 0;
    for(var i = 1; i <= 5000; i++){ 
        if(i % 2 != 0){
            sum += i;
        } 
    }

    return sum;
}

console.log(sumOfOdds());

/*-----------------------------------------*/

function iteratenArray(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }

    return sum;
}

console.log(iteratenArray([1,2,3,4]));

/*-----------------------------------------*/


function findMax(arr) {
    var max = arr[0];
    for (var i = 1; i < arr.length; i++) {
        if (max < arr[i]) {
            max = arr[i];
        }
    }
    return max;
}

console.log(findMax([10,1,2,3,4]));

/*-----------------------------------------*/

function findAverage(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    console.log(sum);
    console.log(arr.length);
    return (sum / arr.length);
}

console.log(findAverage([10,10,10]));

/*-----------------------------------------*/

function arrayOdds() {
    var arr = [];
    for (var i = 1; i <= 50; i++) {
        if (i % 2 != 0) {
            arr.push(i);
        }
    }

    return arr;
}

console.log(arrayOdds());

/*-----------------------------------------*/

function greaterThanY(arr, y) {
    var counter = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > y) {
            counter++;
        }
    }

    return counter;
}

console.log(greaterThanY([1,6,9,10,123], 9));

/*-----------------------------------------*/

function squareArrayVals(arr) {
    for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i] * arr[i];
    }
    return arr;
}

console.log(squareArrayVals([1,6,9,10,123]));

/*-----------------------------------------*/

function negatives(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            arr[i] = 0;
        }
    }
    return arr;
}

console.log(negatives([1,-16,9,-10,123]));

/*---------------------------------------*/

function maxMinAverageArrayVals(arr) {
    var newArr = [];
    newArr.push(findMax(arr));
    var min = arr[0];
    for (var i = 1; i < arr.length; i++) {
        if (min > arr[i]) {
            min = arr[i];
        }
    }
    newArr.push(min);
    newArr.push(findAverage(arr));
    return newArr;
}


console.log(maxMinAverageArrayVals([1,2,3]));

/*---------------------------------------*/

function swap(arr) {
    var tmp = arr[0];
    arr[0] = arr[arr.length - 1];
    arr[arr.length - 1] = tmp;
}

var arr = [1,2,3];
swap(arr);
console.log(arr);

/*---------------------------------------*/

function numberToString(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            arr[i] = 'Dojo';
        }
    }
}

var arr = [-1,2,-3];
numberToString(arr);
console.log(arr);