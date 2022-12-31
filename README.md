# Identification-of-Fake-Products-using-Blockchain

In this project we aim to identify counterfeit products in the market with the help of distinctive QR codes and consensus algorithms. A website was made for the same to show the working of the application and a hash key returned with the result as “found” or “not found”. It is based on the principle of blockchain. 

### Instructions to run:

Clone the project, 
```sh
$ git clone https://github.com/sanika-karwa/Identification-of-Fake-Products-using-Blockchain.git
```

Install the dependencies, 
```sh
$ pip install -r requirements.txt
```

Start a blockchain node server,
```sh
$ export FLASK_APP = node_server.py
$ flask run --port 8000
```

```sh
$ set LANG = C.UTF-8
$ set FLASK_APP = node_server.py
$ flask run --port 8000
```
One instance of our blockchain node is now up and running at port 8000.

Run the application on a different terminal session,

```sh
$ python run_app.py
```

```sh
$ set LANG = C.UTF-8
$ set FLASK_APP = run_app.py
$ flask run --port 8000
```

The application should be up and running at [http://localhost:5000](http://localhost:5000).
