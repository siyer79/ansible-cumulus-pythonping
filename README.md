# ansible-cumulus-pythonping

This ansible script will create three cumulus linux (CL) virtual machines.  The main one (playserver) will have a python script and a ping list file copied to it.
The other 2 machines running CL will be brought up just to test the python ping script (switch01 and switch02).  The file pinglist contains 4 entries.
The first three are the 3 machines that are up and last one is just to test the script feature, it is an IP address that doesn't exist.

1) After the machines are up, go to the playserver (vagrant ssh playserver).  

2) In the /home/vagrant directory, run pingall.py to see the python ping script function.
