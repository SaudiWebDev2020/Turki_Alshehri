var users = [
        {
            name: "Michael",
            age: 37
        },
        {
            name: "John",
            age: 30
        },
        {
            name: "David",
            age: 27
        }
    ];

    for (a in users) {
        console.log(users[a].name, " - ", users[a].age);
    }