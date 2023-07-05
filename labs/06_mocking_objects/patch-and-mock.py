import requests
from unittest.mock import patch, MagicMock

def imdb_info(title: str):
    """Get results for a movie title"""
    print(f"Searching IMDB for {title}")
    results = requests.get(f"https://imdb-api.com/API/SearchTitle/{title}")
    if results.status_code == 200:
        return results.json()
    return {}

if __name__ == '__main__':
    with patch('__main__.requests.get') as imdb_mock:
        imdb_mock.return_value = MagicMock(
            spec=requests.Response,
            status_code=200,
            content='{"error":"Not Found"',
            json= MagicMock(return_value={"title": "Bambi", "year": "1942"})
        )
        print(imdb_info("Bambi"))