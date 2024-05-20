CREATE TABLE kinds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50)
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50)
);

CREATE TABLE breeds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    kind_id INT,
    FOREIGN KEY (kind_id) REFERENCES kind_id(id)
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio VARCHAR(100),
    phone INT,
    addres VARCHAR(255),
    email VARCHAR(50),
    login VARCHAR(50),
    password VARCHAR(50),
    post_id INT,
    FOREIGN KEY (post_id) REFERENCES posts(id),
    UNIQUE (password) ON CONFLICT IGNORE
);

CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name  VARCHAR(100),
    date_birth DATA,
    kind_id INT,
    breed_id INT,
    FOREIGN KEY (kind_id) REFERENCES kinds(id),
    FOREIGN KEY (breed_id) REFERENCES breeds(id)
);

CREATE TABLE procedures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name  VARCHAR(100),
    comment TEXT,
    price INT
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATA,
    comment TEXT,
    procedure_id INT,
    user_id INT,
    patient_id INT,
    FOREIGN KEY (procedure_id) REFERENCES procedures(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (patient_id) REFERENCES patients(id)
);


INSERT INTO kinds (id, name) VALUES 
(1, 'Собака'),
(2, 'Кошка'),
(3, 'Птица');

INSERT INTO posts (id, name) VALUES
(1, 'Главный врач'),
(2, 'Доктор');

INSERT INTO breeds (name, kind_id) VALUES 
('Лабрадор ретривер', 1),
('Немецкая овчарка', 1),
('Бигль', 1),
('Немецкий шпиц', 1),
('чихуахуа', 1),
('Йоркширский терьер', 1),
('Лабрадор-ретривер', 1),
('Пудель', 1),
('Бостон-терьер', 1),
('Мейн-кун', 2),
('Сфинкс', 2),
('Британская кошка', 2),
('Шотландская кошка', 2),
('Сиамская кошка', 2),
('Ориентальная кошка', 2),
('Бенгальская кошка', 2),
('Попугай', 3),
('Чижик', 3),
('Соловей', 3),
('Канарейка', 3);

INSERT INTO users (fio, phone, addres, email, login, password, post_id) VALUES
('Иванов Иван Иванович', 79464918206, 'ул. Пушкина, 10', 'ivanov@example.com', 'admin', 'admin', 1),
('Сидоров Александр Тимурович', 79464918206, 'Трудовая ул., 24', 'sidorov@example.com', 'doctor1', 'doctor1', 2),
('Лебедев Тимур Даниилович', 79434578206, 'Юбилейная ул., 12', 'lebedev@example.com', 'doctor2', 'doctor2', 2),
('Петров Петр Петрович', 7946394746, 'Лесная ул., 3', 'petrov@example.com', 'doctor3', 'doctor3', 2);

INSERT INTO procedures (name, comment, price) VALUES
('Общий осмотр', 'Комплексное обследование питомца', 800),
('Прививка от бешенства', 'Процедура вакцинации от бешенства', 600),
('Ультразвуковое исследование животного', 'Исследование органов при помощи ультразвука', 1200),
('Кастрация кота', 'Хирургическое удаление половых органов у кота', 1500),
('Стрижка когтей', 'Подрезание когтей у животного', 200),
('Экстренная операция', 'Неотложная операция при острой патологии', 2500),
('Диагностика паразитарных заболеваний', 'Анализ и лечение паразитов', 700),
('Зубная чистка', 'Процедура гигиенической чистки зубов у животного', 900),
('Лечение кожных заболеваний', 'Лечение и обработка кожных заболеваний', 1000),
('Физиотерапия', 'Процедуры физического воздействия для лечения', 800),
('ЭКГ', 'Электрокардиография для исследования сердца', 1300),
('Рентген', 'Исследование органов при помощи рентгеновского излучения', 1200),
('Анализ крови', 'Общий анализ крови для диагностики заболеваний', 400),
('УЗИ брюшной полости', 'Ультразвуковое исследование органов брюшной полости', 1000),
('Лечение инфекционных заболеваний', 'Процедуры по лечению инфекционных заболеваний', 900),
('Иммуносупрессивная терапия', 'Терапия для подавления иммунной реакции', 1100),
('Лазерная терапия', 'Терапевтическое воздействие лазерным излучением', 800),
('Гнойная хирургия', 'Хирургическое вмешательство при гнойных процессах', 1300),
('Лечение опорно-двигательной системы', 'Процедуры восстановления опорно-двигательной системы', 1000),
('Травматология', 'Лечение травм и переломов у животных', 1200);