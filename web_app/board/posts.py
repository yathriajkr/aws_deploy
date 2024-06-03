from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
)

from board.database import get_db_connection

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]

        if message:
            conn = get_db_connection()
            db = conn.cursor()
            db.execute(
                "INSERT INTO posts (author, message) VALUES (%s, %s)",
                (author, message),
            )
            conn.commit()
            db.close()
            conn.close()
            return redirect(url_for("posts.posts"))
        
    return render_template("posts/create.html")

@bp.route("/posts")
def posts():
    conn = get_db_connection()
    db = conn.cursor()
    db.execute(
        "SELECT author, message, created FROM posts ORDER BY created DESC"
    )
    posts = db.fetchall()
    temp=[]
    for post in posts:
        temp_dict={}
        temp_dict['author']=post[0]
        temp_dict['message']=post[1]
        temp_dict['created']=post[2]
        temp.append(temp_dict)
    posts = temp
    print(posts)
    db.close()
    conn.close()
    return render_template("posts/posts.html", posts=posts)
