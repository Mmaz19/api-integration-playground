import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

API_URL = "https://jsonplaceholder.typicode.com/users"

try:
    logging.info("Calling API...")

    response = requests.get(API_URL, timeout=10)

    response.raise_for_status()

    logging.info(
        "API call completed successfully (%s)",
        response.status_code
    )

    users = response.json()

    logging.info(
        "Retrieved %d users",
        len(users)
    )

except requests.exceptions.Timeout:
    logging.error("Request timeout")

except requests.exceptions.ConnectionError:
    logging.error("Connection error")

except requests.exceptions.HTTPError as error:
    logging.error("HTTP Error: %s", error)

except requests.exceptions.RequestException as error:
    logging.error("Unexpected error: %s", error)