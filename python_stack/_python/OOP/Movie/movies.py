class Room:
    room_id = 1
    def __init__(self):
        self.room_id = Room.room_id
        Room.room_id += 1
        
    def info(self): 
        print ("room number:",self.room_id) 
    


class Schedule:
    schedule_ID = 0
    num_seats = 2
    def __init__(self, movie, start_time, end_time, room):
        self.movie = movie
        self.start_time = start_time
        self.end_time = end_time
        self.room = room
        Schedule.schedule_ID += 1
        self.num_seats = Schedule.num_seats

    def get_info(self):
        print("Movie Title:", self.movie.title, "| Start time:", self.start_time, "| End time:", self.end_time, "| Room number:", self.room.room_id, "| Avalibale seats:", self.num_seats)

    def avaliability(self):
        if self.num_seats > 0:
            self.get_info()
        else:
            print(self.movie.title,"SOLD OUT")


class Movie: 
    movie_ID=1 
    def __init__(self, title, gener): 
        self.title = title 
        self.gener = gener
        self.movie_ID=Movie.movie_ID
        Movie.movie_ID+=1 
    
    def info(self): 
        print (self.movie_ID,self.title) 




class Reservation:
    reservation_ID = 1
    def __init__(self,customer_name, schedule):
        self.id = Reservation.reservation_ID
        self.customer_name = customer_name
        self.schedule = schedule
        Reservation.reservation_ID += 1
        self.schedule.num_seats -= 1
    def get_info(self): 
        print("\n")
        print("-"*44,"Your Ticket Info", "-"*44)
        print ("\nReservation ID: ", self.id, "\nCustomer Name:", self.customer_name)
        # self.schedule.get_info() 
        print("Movie Title:", self.schedule.movie.title, "| Start time:", self.schedule.start_time, "| End time:", self.schedule.end_time, "| Room number:", self.schedule.room.room_id, "| seats:", seat_choice)

        print("\n")
        print("-"*106)

#------------------------------------------------------------------------------------------------------------------------

movieList = []

movieList.append(Movie("The dark ", "Action"))
movieList.append(Movie("The white", "Drama"))
movieList.append(Movie("Project  ", "Action"))
movieList.append(Movie("Old Guard", "Drama"))
movieList.append(Movie("Over Mood", "Animation"))


room1 = Room()
room2 = Room()

scheduleList = []

scheduleList.append(Schedule(movieList[0], "09:00pm","10:00pm", room1))
scheduleList.append(Schedule(movieList[1], "12:30pm", "01:30pm",room2))
scheduleList.append(Schedule(movieList[2], "07:25pm", "08:50pm",room1))
scheduleList.append(Schedule(movieList[3], "06:00pm", "07:30pm",room2))
scheduleList.append(Schedule(movieList[4], "09:00pm", "11:00pm",room2))

seats = [["1A","2A","3A","4A","5A","6A","7A"],["1B","2B","3B","4B","5B","6B","7B"],["1C","2C","3C","4C","5C","6C","7C"],
        ["1D","2D","3D","4D","5D","6D","7D"],["1E","2E","3E","4E","5E","6E","7E"]]

seat_choice = ""
# for i in seats:
#     print(i)

print('''
----------------------------------------------------------------------------------------------------------

                            WELCOME TO THE ONLINE MOVIE TICKET BOOKING

----------------------------------------------------------------------------------------------------------
''')
print("\n")
while (True):
    count = 0
    for i in range(0, len(scheduleList)):
        count += 1
        print(str(count)+"] ", end="")
        scheduleList[i].avaliability() 

    print('''
        Options:
        1) to make a reservation
        0) to exit
        ''')

    choice = input("        Your choice: ")

    if choice == '1':
        name = input("        Enter your name please: ")
        print('''        select a schedule (e.g 1,2): ''', end="")
        select = input()
        print("\n        select your seat\n")
        for i in seats:
            print("        \b",i)
        seat_choice = input("\n        Your seat choice: ")

        for i in seats:
            if seat_choice in i:
                i.remove(seat_choice)
        # for i in seats:
        #     print("        \b",i)
        reservation = Reservation(name, scheduleList[int(select)-1])
        reservation.get_info()
        print("\n")

        book_again = input("\nWould you like to make another reservation ? y or n: ")
        if book_again == 'n':
            break
    elif choice == '0':
        break
    else:
        print("uknown choice")
        break