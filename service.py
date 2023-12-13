import json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["doctors"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["doctors"]


def update_one_by_id(id, doctor):
    db = json_service.get_database()

    for i, elem in enumerate(db["doctors"]):
        if elem["id"] == id:

            elem["name"] = doctor["name"]
            elem["contacts"] = doctor["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["patients"]):
        if elem["id"] == id:

            candidate = db["patients"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(patient):
    db = json_service.get_database()

    last_doctor_id = get_all()[-1]["id"]
    db["teachers"].append({"id": last_doctor_id + 1, **patient})

    json_service.set_database(db)
def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["patients"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["patients"]


def update_one_by_id(id, patient):
    db = json_service.get_database()

    for i, elem in enumerate(db["doctors"]):
        if elem["id"] == id:

            elem["name"] = patient["name"]
            elem["contacts"] = patient["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id2(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["patients"]):
        if elem["id"] == id:

            candidate = db["patients"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(patient):
    db = json_service.get_database()

    last_doctor_id = get_all()[-1]["id"]
    db["patients"].append({"id": last_doctor_id + 1, **patient})

    json_service.set_database(db)