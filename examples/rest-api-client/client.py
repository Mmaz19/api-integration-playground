import requests


API_URL = "https://jsonplaceholder.typicode.com/users"


def call_api():
    """
    Execute a REST API call and return the response data.
    This example uses a placeholder generator, view the expected payload at the URL
    """

    try:
        response = requests.get(API_URL, timeout=10)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print(f"API communication error: {error}")
        return None


def process_users(users):
    """
    Process API response data.
    """

    for user in users:
        print(
            f"User: {user['name']} | "
            f"Email: {user['email']}"
        )


if __name__ == "__main__":

    users = call_api()

    if users:
        process_users(users)