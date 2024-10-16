import requests

def gather_info(target):
    print(f"Gathering information about {target}")
    # Add reconnaissance logic here
    # Example: Using requests to fetch metadata, etc.
    response = requests.get(target)
    print(response.text)

if __name__ == "__main__":
    target_url = input("Enter target URL: ")
    gather_info(target_url)
