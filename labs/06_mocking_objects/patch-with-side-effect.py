from unittest.mock import patch

def bye():
    return 'bye'
def hello():
    return 'hello'

@patch('__main__.hello', side_effect=bye)
def patched_hello(hello_mock):
    return hello()

if __name__ == '__main__':
    print(hello())
    print(bye())
    print(patched_hello())