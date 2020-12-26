from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__, static_url_path='')
app.config.from_object(Config)
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

from api import assignment, attendance, classes, solution, student, enquiry, teacher, tc
from models.student import Student
from models.attendance import Attendance
from models.solution import Solution
from models.assignment import Assignment
from models.enquiry import Enquiry
from models.tc import Tc

if __name__ == '__main__':
    app.run(debug=True)
