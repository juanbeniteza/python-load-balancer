# Custom Load Balancer Python

This project demonstrates a simple load balancer built with Flask that uses the least connections algorithm to distribute requests across multiple backend servers. The load balancer also includes reverse proxy functionality to forward requests to the appropriate backend server and handle responses.

Additionally, the project includes a script to run multiple HTTP requests concurrently for testing purposes.

## Prerequisites
- Python 3.12 or higher
- [Poetry](https://python-poetry.org/) for installing the packages


## Installation

1. Clone repository

```bash
git clone https://github.com/juanbeniteza/python-load-balancer.git
cd python-load-balancer
```

2. Install dependencies

You can install the required dependencies using `Poetry`

```bash
poetry install
```

Otherwise you can use `pip` and install them as follow

```bash
pip install -r requirements.txt
```

## How to run

Run the servers in different terminals

```bash
# Terminal 1
python servers/server1.py
```

```bash
# Terminal 2
python servers/server2.py
```

```bash
# Terminal 3
python servers/server3.py
```

Run the load balancer

```bash
# Terminal 4
python balancer.py
```

After this any request you made to the load balancer will be proxied to one of the other severs according to the least connections algorithm.


If you want an easy way to run multiple request in paraller you can run in a new terminal

```bash
# Terminal 5
python run.py
```


## How to improve this code further?

- Checking if the servers are live before proxing the request
- Handle errors
- Implement others load balancer algorithms

---

_**NOTE**: This code is not production ready and it is far beyond that, this is just a custom implementation of a load balancer in Python, please use production ready software for your needs._
