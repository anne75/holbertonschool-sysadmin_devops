## Nginx Debugging
For these projects, a docker container was provided with Nginx running as a deamon.
So entering the container, Nginx status was one of not running but it was actually listening to port 8080.  
For task 0: work was to make it listen to port 80 too.  
Fort task 1: work was to start nginx but showing it as not running when checking the status. Some solutions are to look into the init.d/nginx file or to remove the pid just created after starting nginx (look into /var/run/nginx).  
