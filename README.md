1)	Run generator.py file
Give datapath of the directory where you want to store the logs of 1000 servers.
Example command: python generator.py  <Datapath>

2)	Run query.py file
Give datapath of the directory where the logs of 1000 servers are stored.

3)	Input query
Example: QUERY 192.168.0.1 1 2014-10-31 00:00 2014-10-31 00:05
Example: EXIT



 

Note: If running on Linux OS
Enter commands : chmod 755 generator.py
                 chmod 755 query.py
./generator.py <Datapath>
./query.py <Datapath>



