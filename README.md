# Flask Example App

This is a simple Flask app that shows how to have a button run a specific Python function, along with an API retrieval route.

99% of the existing Flask tutorials focus on building database apps, which over complicates the process of learning Flask.

I was only able to learn how to use Flask after building an application that focused purely on a processing task.

## Quick Start

Install the python requirements by running `pip install -r requirements.txt`.

Run `python app.py` to start the flask server.

Access the processing app by navigating to `127.0.0.1:5001` in a web browser.

Access the API example by navigating to `127.0.0.1:5001/api/v1/planes`. You can view a specific data field by using one of the plane models like so: `127.0.0.1:5001/api/v1/planes/787`.

## Next Step

If you want to learn more about building APIs in Flask, read the API chapter from Miguel Grinberg's [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis).

Additionally, I have an open source Flask API framework, called [flasker](https://github.com/camisatx/flasker), that you can explore and use for projects. It includes a few example routes, including a full featured user account setup.
