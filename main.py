from views.view import app
import uvicorn
@app.get('/')
def penis():
    return 1

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)