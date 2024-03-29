# Where To Go, by Nikhil Kolluri and Nicholas Chu
A web app that randomly selects a restaurant which fits the specifications of user-defined filters, including price range, food category, distance, and average ratings. Demo the app at https://www.idkwheretogo.com.

### How to Run Locally with Flask
Simply run `wtg_frontend.py`, and the Flask development server will start up.

### How to Run Locally through Docker
First, make sure you have Docker installed on your computer. If you don't have Docker, you can go [here](https://docs.docker.com/install/#supported-platforms) to learn more about how to do that. (P.S. If you don't have a professional version of Windows or don't meet the requirements of Docker CE, you must download [Docker Toolbox](https://docs.docker.com/toolbox/overview) to install Docker.)

Once you have Docker installed, open up a terminal in the project root directory and run `docker build -t wtg .` to build the Docker image.

After the build finishes, run `docker run -d -p 80:5000 wtg` to start the gunicorn production server.

Now, run `docker-machine ip` to get the IP address of where the server is hosted. Visit this address in a web browser to access the site (e.g. 192.168.99.100).

Congratulations, you have successfully hosted and ran the web app through Docker!

If you want to stop the server, use `docker ps` to get a list of running containers. Then, run `docker stop [container id]` to stop the container.
