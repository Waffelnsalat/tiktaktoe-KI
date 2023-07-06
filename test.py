import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def change_password(ip_address, old_password, new_password):
    url = f"https://{ip_address}/api.cgi?cmd=Login"
    
    payload = [{
        "cmd": "Login",
        "param": {
            "User": {
                "userName": "admin",
                "password": old_password,
                "Version": "0"
            }
        }
    }]
    
    try:
        response = requests.post(url, json=payload, verify=False)
        response.raise_for_status()
        json_response = response.json()
        json_response = json_response[0]
        if json_response.get("code") != 0:
            raise Exception(f"API Error: {json_response.get('code')}")
        token = json_response.get("value").get("Token").get("name")
        
        url = f"https://{ip_address}/api.cgi?cmd=ModifyUser&token={token}"
        payload = [{
            "cmd": "ModifyUser",
            "action": 0,
            "param": {
                "User": {
                    "userName": "admin",
                    "newPassword": new_password,
                    "oldPassword": old_password
                }
            }
        }]
        response = requests.post(url, json=payload, verify=False)
        response.raise_for_status()
        json_response = response.json()
        json_response = json_response[0]
        if json_response.get("code") != 0:
            raise Exception(f"API Error: {json_response.get('code')}")
        print("Password changed successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except ValueError:
        print("Invalid JSON response. Actual response:", response.text)
    except Exception as e:
        print(e)

change_password("10.30.2.31", "new_password",  "J/7@zIEX2e4m")
