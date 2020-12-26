from flask import request
from app import app, db
from models.classes import Classes


@app.route('/classes', methods=['POST'])
def add():
    name = request.form.get('name', None)
    section = request.form.get('section', None)

    if not name:
        return {"message": "You must provide class name"}, 404

    if not section:
        return {"message": "You must provide class section"}, 404

    if Classes.query.filter_by(name=name, section=section).first():
        return {"message": "Class with given section already taken"}, 404
    else:
        class_obj = Classes(name=name, section=section)
        db.session.add(class_obj)
        db.session.commit()
        return {"message": "Data inserted successfully"}, 200


@app.route('/classes', methods=['GET'])
def get():
    import collections
    classes = Classes.query.all()
    print(classes)

    if classes:
        class_dic = collections.defaultdict(list)
        for cla in classes:
            class_dic[cla.name].append(cla.section)
        res = []
        for k, v in class_dic.items():
            res.append({'class': k, 'sections': v})
        return {"classes": res}, 200

    else:
        return {"message": "No classes available"}, 404


@app.route('/classes-details', methods=['GET'])
def details():
    classes = Classes.query.all()
    res = []

    if classes:
        for cls in classes:
            obj = {"class_id": cls.id, "class_name": cls.name, "class_section": cls.section, "teacher_id": cls.teacher_id}
            res.append(obj)
        return {"message": res}, 200
    else:
        return {"message": "No classes created yet"}, 404
