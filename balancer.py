from flask import Flask, request, Response
import requests
import threading

app = Flask(__name__)

# List of backend servers with locks for thread safety
servers = [
    {'address': 'http://localhost:5001', 'connections': 0, 'lock': threading.Lock()},
    {'address': 'http://localhost:5002', 'connections': 0, 'lock': threading.Lock()},
    {'address': 'http://localhost:5003', 'connections': 0, 'lock': threading.Lock()},
]

# Function to select the server with the least connections
def get_least_connected_server(servers):
    servers = sorted(servers, key=lambda x: x['connections'])
    return servers[0]


def proxy_request(server, original_request):
    url = f"{server['address']}{original_request.path}"
    headers = {key: value for key, value in original_request.headers if key != 'Host'}
    
    with server['lock']:
        server['connections'] += 1
    
    try:
        # Forward the request to the selected server
        response = requests.request(
            method=original_request.method,
            url=url,
            headers=headers,
            data=original_request.get_data(),
            cookies=original_request.cookies,
            allow_redirects=False,
        )
        
        # Relay the response back to the client
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for name, value in response.raw.headers.items()
                   if name.lower() not in excluded_headers]
        return Response(response.content, response.status_code, headers)
    
    except requests.exceptions.RequestException as e:
        return Response(f"Error proxying request: {e}", status=502)
    
    finally:
        with server['lock']:
            server['connections'] -= 1


# Route to handle incoming requests and proxy them to the backend server
@app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def process_request(path):
    # Get the server with the least connections
    server = get_least_connected_server(servers)
    return proxy_request(server, request)


if __name__ == "__main__":
    # Run the Flask application with threading enabled
    app.run(host='localhost', port=5004, threaded=True)
