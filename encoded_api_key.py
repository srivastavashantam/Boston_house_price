import base64

api_key = "3edaf3fd-934c-41db-afef-1e8c94338e4a"
encoded_api_key = base64.b64encode(api_key.encode()).decode()

print(encoded_api_key)
