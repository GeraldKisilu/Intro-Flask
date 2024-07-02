from flask import Flask, render_template


app = Flask(__name__)

@app.route('/students')
def index():
    data= [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "gender": "Male"
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@example.com",
        "gender": "Female"
    },
    {
        "id": 3,
        "first_name": "Alex",
        "last_name": "Johnson",
        "email": "alex.johnson@example.com",
        "gender": "Non-binary"
    }
]

    return render_template('index.html', data=data)

@app.route('/')
def home():
    return{"msg":"Welcome to Phase 4!"}


@app.route('/about')
def about():
    return render_template('about.html')
