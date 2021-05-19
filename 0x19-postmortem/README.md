# Issue Summary
On Monday, from 8:00 PM to 10:20 PM, our whole site was down. Every part of our app was not functional and 100% of our users couldn't access any of the services we offer, right from payments to bookings. This was caused by an overload of users on our server hence leading to the site's crash.

# Issue Timeline
8:05 PM - A regular user reaches out to the team saying he couldn't reach the site <br />
8:10 PM - Our representative advises the user to restart his internet internet router <br /> 
8:20 PM - 10 more similar complaints are reported from different complaints <br />
8:22 PM - Representative forwards complaint to system administrator <br />
8:25 PM - System administrator officially declares the site down due to server overload and forwards recommendations to reinforce our infrastructure with one more server plus a load balancer <br />
9:30 PM - Load balancer and server acquired and configurations begin <br />
10:20 PM - Configurations and tests complete. Site brought back up <br />

# Issue reason and resolution
The outage was caused by a sudden large number of requests being made to our server. This was caused by our inability to factor in the probability  of our users rapidly growing in size in the initial stags of our business. The issue was resolved by adding a load balancer to our infrastructure plus one more server. Users' request are first sent to the load balancer before being sent to either of the server through a round-robin algorithm.

# Preventive measures
Consistently track user analytics and scale the site accordingly.  
