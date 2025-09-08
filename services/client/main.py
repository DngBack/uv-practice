from src.client import Client, ClientInput

if __name__ == "__main__":
    client = Client()
    input_data = ClientInput(client_id="987654321", client_secret="new_client_secret")
    output_data = client.process(input_data)
    print(f"Access Token: {output_data.access_token}")
    print(f"Refresh Token: {output_data.refresh_token}")