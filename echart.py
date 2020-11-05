from app import create_app, db


app = create_app()

@app.route('/')
def hello_world():
    return 'hello world'

if __name__ == "__main__":
    app.run()