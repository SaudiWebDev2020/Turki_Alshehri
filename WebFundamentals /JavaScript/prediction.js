


/* Predict 1 */
for(var num = 0; num < 15; num++){
    console.log(num);
}

//------> prints numbers from 0 - 14


/* Predict 1 */
for(var i = 1; i < 10; i+=2){
    if(i % 3 == 0){
        console.log(i);
    }
}

//------> Prints the numbers that are divisable by 3 -- (3,9)


/* Predict 3 */
for(var j = 1; j <= 15; j++){
    if(j % 2 == 0){
        j+=2;
    }
    else if(j % 3 == 0){
        j++;
    }
    console.log(j);
}

//------> it checks if j is divisable by 2, it will be incremented by 2 and prints j, otherwise if it is devisable by 3 then it will be incremented by 1 and prints j
// 1, 4, 5, 8, 10, 11, 14, 16