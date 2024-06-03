import psycopg2
import click
from flask import current_app, g

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()
        
@click.command("init-db")
def init_db_command():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))

    click.echo("You successfully initialized the database!")

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def get_db_connection():
    conn = psycopg2.connect(host='10.10.0.60', port='5432', database='test',user='webapp', password='webapp')
    return conn

def get_data_postgres():
    if "db" not in g:
        g.db = get_db_connection
    return g.db

