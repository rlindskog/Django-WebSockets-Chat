**About**

This is a simple example of using WebSockets with Django Channels and Redis.

**Setup**

    > pip install channels
    > python manage.py migrate
  
  **Run**
Run the redis server.  If you're on mac, you can install it with 
  

    > brew install redis
    
and run it in a separate terminal with

    > redis-server
    
then run this in another terminal

    > python manage.py runserver 0.0.0.0:8000 --noworker
    
then run this in another terminal

    > python manage.py runworker

You should be able to open http://0.0.0.0:8000 in two separate windows (or computers on the same LAN) and watch the live chat.
