## Nginx Debugging
For these projects, a docker container was provided with Nginx running as a deamon.  
So entering the container, Nginx status was one of not running but it was actually listening to port 8080. 
Trying to stop Nginx would trigger an error about `pid` not matching.  
At this point, looking into Nginx `/init.d/` file for where the `pid` was supposed to be stored, we could find that this file was missing.  

For task 0: work was to make it listen to port 80 as well.  
For task 1: work was to do the same but also showing nginx as not running when checking its status. Some solutions are to look into the init.d/nginx file or to remove the pid file created just after starting nginx (look into `/var/run/nginx`).  
