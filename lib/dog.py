from models import Dog


def create_table(base, engine):
    base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    query = session.query(Dog).all()
    return query


def find_by_name(session, name):
    query = session.query(Dog.name).filter(Dog.name.like(f"%{name}%")).all()[0]
    return query


def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id).all()[0]
    return query


def find_by_name_and_breed(session, name, breed):
    query = (
        session.query(Dog).filter((Dog.name == name) and (Dog.breed == breed)).all()[0]
    )
    return query


def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()