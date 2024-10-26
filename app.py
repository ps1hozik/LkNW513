import json
import os

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
)

from models import (
    db,
    FormData,
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def forms():
    return render_template("forms.html")


@app.route("/submit_data", methods=["POST"])
def submit_data():
    inputs_data = json.dumps(request.form)
    form_data = FormData(data=inputs_data)
    db.session.add(form_data)
    db.session.commit()
    return redirect(url_for("get_data"))


@app.route("/json_data")
def get_json_data():
    form_data = db.session.execute(db.select(FormData)).scalars()
    data_list = [{"id": item.id, "data": json.loads(item.data)} for item in form_data]
    return data_list


@app.route("/data")
def get_data():
    data_list = get_json_data()
    return render_template("data.html", data_list=data_list)


if __name__ == "__main__":
    app.run(debug=True)
