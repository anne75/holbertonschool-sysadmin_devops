## Nginx Debugging
For these projects, a docker container was provided with Nginx running as a deamon.  
So entering the container, Nginx status was one of not running but it was actually listening to port 8080. 

For task 0: work was to make it listen to port 80 as well.  
For task 1: work was to do the same but also showing nginx as not running when checking its status. Some solutions are to look into the init.d/nginx file or to remove the pid file created just after starting nginx (look into `/var/run/nginx`).  
