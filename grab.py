import requests

server_name = "example-server" # replace with the name of the server you want to check

url = f"https://servers-live.fivem.net/api/servers/single/{server_name}"

response = requests.get(url)

if response.status_code == 200:
    server_data = response.json()
    server_ip = server_data["ip"]
    print(f"The IP of the {server_name} server is {server_ip}.")
else:
    print("An error occurred while trying to retrieve the server information.")
