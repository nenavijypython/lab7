db = {"hospital_name": "Больница первая", "address": "ул. Бо-бо, 228",
  "patients": [{"id": 1, "name": "Пушкин Сергей", "age": 31, "disability": "Умер", "contacts": {"email": "fuckdantes@gmail.com", "phone": "+77777777"}, "class_id": 1},
    {"id": 2, "name": "Роберт Кеков", "age": 58, "disability": "Грыжа", "contacts": {"email": "rob@gmail.com", "phone": "+3546861"}, "class_id": 2},
    {"id": 3, "name": "Николай Второй", "age": 65, "disability": "Рвота", "contacts": {"email": "kolyasecond@gmail.com", "phone": "+35465454"}, "class_id": 1},
    {"id": 4, "name": "Сидоров Петр", "age": 45, "disability": "Кашель", "contacts": {"email": "sidorov@lol.com", "phone": "+8787878798"}, "class_id": 2}],
  "classes": [{"id": 1, "number": 301, "letter": "A", "class_doctor_id": 1, "students_id": [1, 3], "courses_id": [1, 2, 3]},
    {"id": 2, "number": 301, "letter": "Б", "class_doctor_id": 2, "students_id": [2, 4], "courses_id": [1, 3]}],
  "doctors": [{"id": 1, "name": "Малышева Елена", "classes_id": [1, 2], "contacts": {"email": "lifeisgood@gmail.com", "phone": "+1122334455"}},
    {"id": 2, "name": "Сарычев Андрей", "classes_id": [3], "contacts": {"email": "lightweightbaby@example.com", "phone": "+9988776655"}},
    {"id": 3, "name": "Спасокукоцкий Юрий", "classes_id": [3], "contacts": {"email": "cheatingisgreat@gmaill.com", "phone": "+45684684"}}]}