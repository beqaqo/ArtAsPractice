import click
from flask.cli import with_appcontext
from src.ext import db
from src.models import Course, Mentor

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Initializing database...")
    db.drop_all()
    db.create_all()
    click.echo("Database initialized.")

@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Populating database")
    mentor1 = Mentor(name="Alice Johnson", about="Expert in Python", photo="alice.jpg")
    mentor2 = Mentor(name="Bob Smith", about="Data Science guru", photo="bob.jpg")
    db.session.add_all([mentor1, mentor2])
    db.session.commit()
    course1 = Course(
        title="Python Basics",
        description="Learn Python from scratch",
        type="programming",
        price=99.99,
        mentor_id=mentor1.id
    )
    course3 = Course(
        title="Web Development with Flask",
        description="Build websites using Flask framework",
        type="web",
        price=120.00,
        mentor=mentor1
    )
    db.session.add_all([course1, course3])
    db.session.commit()
    click.echo("Database populated.")