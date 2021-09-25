Ride Sharing app

Actors
------
- Rider
- Driver

class Diagram

Person                      
-----                       
name                        
                            

Rider
-----
add_rider(name)
completed_rides()  

Driver
-----
add_driver(name)
completed_rides()


Ride
-----
id
origin
destination
no_of_seats
-------
create_ride(id, origin, destination, no_of_seats)
update_ride(id, origin, destination, no_of_seats)
withdraw_ride(id)
close_ride(id)


                            

