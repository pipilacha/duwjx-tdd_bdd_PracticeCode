import requests
from unittest import mock
"""
changes the return value of the function
"""
def imdb_info(title: str):
    """Get results for a movie title"""
    print(f"Searching IMDB for {title}")
    results = requests.get(f"https://imdb-api.com/API/SearchTitle/{title}")
    return results.json()

def imdb_info2(title: str):
    """Get results for a movie title"""
    print(f"Searching IMDB for {title} - 500 response")
    results = requests.get(f"https://imdb-api.com/API/SearchTitle/{title}") #will patch resquest.get
    return results #remove json since request is patched and result is no longer json

if __name__ == '__main__':
    """Run some mock tests"""
    with mock.patch('__main__.imdb_info', return_value= {'status_code': 200}) as imdb:
        print(imdb_info("Bambi"))

    with mock.patch('__main__.imdb_info') as imdb2:
        imdb2.return_value = {'status_code': 404}
        print(imdb_info("Bambi"))

    with mock.patch('requests.get', return_value= {'status_code': 500}) as dummy:
        print(imdb_info2("Bambi"))

