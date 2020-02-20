# Products API
## Requirements
These are the versions they were created with so higher versions may still work
- Python @ 3.7.0
- PIP @ 10.0.1
- MySQL @ 15.1

## Install
In the command-line/terminal, navigate to repository root. Here ```>``` means a command-line/terminal command.

1. Make a virtual environment
```>py -m venv env```

2. Run virtual environment
```>env\Scripts\activate```

should say ```(env)``` on the left

3. Install flask
```>pip install flask```

4. Set environment variable (for Flask)
```>set FLASK_APP=app.py```

5. Install MySQL Connector
```>python -m pip install mysql-connector```

Note: To exit the virtual environment, you can type ```deactivate```.

## Set Database Config
In order to utilize a database (local/remote) we need to setup the credentials.

1. Navigate to the file 'adapters/database_adater.py' and open the file in an editor.

2. in the '__DatabaseAdapterConfig' sub class, you should see a couple of lines like this:
```
...
    self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
    )
    ...
```
Replace these with your own credentials or that of the database you wish to use and save the file.

Note: the default port here for MySQL is 3306

## Run/Configure
In our virtual environment, navigate to the root folder of the repository.

1. Run server
```>flask run```
Or for automatic reloading use:
```flask run --reload```

2. Configure the database
Now that the server is running, in the browser, navigate to '{server address}/configure' 
'server address' should be 'http://localhost:5000' but it will appear in the terminal/command-line when the server starts.

3. On the web page, click "Configure Database". Given a bit of time it should return a message like:"Database configured successfully". If so, then you're good to go.
(This sets up a database called 'ProductsRoderichDB' and populates it with some test data)


You can now naigate to the home address '/' or 'http://localhost:5000' to run the application.

Enjoy!

## Additional resources
There are some additional pages of interest:

- 'http://localhost:5000/design' - Outlines the design choices in building this app/API
- 'http://localhost:5000/configure' - Configure or drop the database (when done)