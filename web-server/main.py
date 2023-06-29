import store
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4,5,6,7,8,9]

@app.get('/contact')
def get_list():
    return {'name':'Monica', 'email':'monibrav3@gmail.com'}


def run():
    store.get_categories()

if __name__ == '__main__':
    run()