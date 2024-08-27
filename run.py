import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# List of URLs to send requests to
urls = [
    'http://localhost:5004/test',
    'http://localhost:5004/test',
    'http://localhost:5004/test',
    'http://localhost:5004/test',
    'http://localhost:5004/test2',
    'http://localhost:5004/test2',
    'http://localhost:5004/test3',
    'http://localhost:5004/test',
    'http://localhost:5004/test',
    'http://localhost:5004/test3',
    'http://localhost:5004/test',
    'http://localhost:5004/test',
    'http://localhost:5004/test',
    'http://localhost:5004/tests',
    'http://localhost:5004/test',
    'http://localhost:5004/test4',
    'http://localhost:5004/test',
    'http://localhost:5004/test',
    # Add more URLs as needed
]

# Function to send a request and handle the response
def fetch_url(url):
    try:
        response = requests.get(url)
        return url, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return url, None, str(e)

# Function to run multiple requests concurrently
def run_concurrent_requests(urls):
    results = []
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        # Submit all the URLs to the executor
        future_to_url = {executor.submit(fetch_url, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                url, status_code, content = future.result()
                results.append((url, status_code, content))
            except Exception as e:
                results.append((url, None, str(e)))
    return results

if __name__ == "__main__":
    # Run the concurrent requests and print the results
    results = run_concurrent_requests(urls)
    for url, status_code, content in results:
        print(f"URL: {url}\nStatus Code: {status_code}\nContent: {content[:100]}...\n")
