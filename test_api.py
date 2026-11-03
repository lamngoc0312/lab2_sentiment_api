"""Exercise all three endpoints using the requests library."""

import requests

BASE_URL = "http://127.0.0.1:8000"


def check(name: str, response: requests.Response, expected_status: int):
    print(f"\n{name}")
    print("HTTP status:", response.status_code)
    print("Response:", response.json())
    assert response.status_code == expected_status, (
        f"Expected {expected_status}, got {response.status_code}"
    )


def main():
    check("GET /", requests.get(f"{BASE_URL}/", timeout=15), 200)
    check("GET /health", requests.get(f"{BASE_URL}/health", timeout=15), 200)

    examples = [
        "I love studying programming!",
        "This is the worst experience ever.",
    ]
    for text in examples:
        response = requests.post(
            f"{BASE_URL}/predict", json={"text": text}, timeout=60
        )
        check(f"POST /predict: {text}", response, 200)

    check(
        "Missing input",
        requests.post(f"{BASE_URL}/predict", json={}, timeout=15),
        422,
    )
    check(
        "Blank input",
        requests.post(f"{BASE_URL}/predict", json={"text": "   "}, timeout=15),
        422,
    )
    print("\nAll API tests passed!")


if __name__ == "__main__":
    try:
        main()
    except requests.RequestException as exc:
        print("Connection error. Is the FastAPI server running?", exc)
        raise
