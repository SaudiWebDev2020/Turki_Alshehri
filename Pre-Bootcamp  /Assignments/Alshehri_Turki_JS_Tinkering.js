function displayIfChildIsAbleToRideTheRollerCoaster(childHeight) {
    if (childHeight > 52) {
        console.log("Get on that ride, kiddo!");
    }
    else {
        console.log("Sorry kiddo. Maybe next year");
    }
}

var childHeight = 52;
displayIfChildIsAbleToRideTheRollerCoaster(childHeight);