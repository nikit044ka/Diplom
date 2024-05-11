CREATE TABLE patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    surname VARCHAR(100),
    patrony VARCHAR(100),
    passport VARCHAR(100),
    meeting VARCHAR(100),
    gender VARCHAR(100),
    adress VARCHAR(100),
    num_telefone VARCHAR(100),
    email VARCHAR(100),
    num_card VARCHAR(100),
    data_meeting INT NOT NULL DEFAULT (strftime('%s','now')),
    data_last INT NOT NULL DEFAULT (strftime('%s','now')),
    data_next INT NOT NULL DEFAULT (strftime('%s','now')),
    num_polis VARCHAR(100),
    data_stop_polis INT NOT NULL DEFAULT (strftime('%s','now'))
);

CREATE TABLE events(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_event INT NOT NULL DEFAULT (strftime('%s','now')),
    doctor VARCHAR(100),
    name_event VARCHAR(100),
    results VARCHAR(100)
);

CREATE TABLE doctors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    password VARCHAR(100)
);




INSERT INTO patients (name, surname, patrony, passport, meeting, gender, adress, num_telefone, email, num_card, num_polis)
VALUES
('John', 'Doe', 'Smith', 'AB1234567', 'General Checkup', 'Male', '123 Main St', '555-1234', 'john.doe@email.com', '1234 5678 9012 3456', 'PL1234567'),
('Alice', 'Johnson', 'Anne', 'CD2345678', 'Vaccination', 'Female', '456 Elm St', '555-5678', 'alice.johnson@email.com', '5678 9012 3456 7890', 'PL2345678'),
('Michael', 'Williams', 'David', 'EF3456789', 'Dental Cleaning', 'Male', '789 Oak St', '555-9012', 'michael.williams@email.com', '9012 3456 7890 1234', 'PL3456789'),
('Sarah', 'Brown', 'Jane', 'GH4567890', 'Eye Exam', 'Female', '321 Pine St', '555-3456', 'sarah.brown@email.com', '3456 7890 1234 5678', 'PL4567890'),
('James', 'Davis', 'Robert', 'IJ5678901', 'Physical Therapy', 'Male', '654 Birch St', '555-7890', 'james.davis@email.com', '6789 0123 4567 8901', 'PL5678901'),
('Emma', 'Wilson', 'Grace', 'KL6789012', 'Allergy Testing', 'Female', '987 Maple St', '555-2345', 'emma.wilson@email.com', '2345 6789 0123 4567', 'PL6789012'),
('Daniel', 'Martinez', 'Carlos', 'MN7890123', 'X-ray', 'Male', '210 Cedar St', '555-6789', 'daniel.martinez@email.com', '7890 1234 5678 9012', 'PL7890123'),
('Olivia', 'Garcia', 'Maria', 'OP8901234', 'Blood Test', 'Female', '543 Walnut St', '555-1234', 'olivia.garcia@email.com', '1234 5678 9012 3456', 'PL8901234'),
('William', 'Lopez', 'Juan', 'QR9012345', 'MRI Scan', 'Male', '876 Sycamore St', '555-5678', 'william.lopez@email.com', '5678 9012 3456 7890', 'PL9012345'),
('Sophia', 'Rodriguez', 'Ana', 'ST0123456', 'Ultrasound', 'Female', '109 Pinecrest St', '555-9012', 'sophia.rodriguez@email.com', '9012 3456 7890 1234', 'PL0123456');

INSERT INTO events (data_event, doctor, name_event, results)
VALUES
(strftime('%s', 'now'), 'Dr. Smith', 'Checkup', 'Normal'),
(strftime('%s', 'now'), 'Dr. Johnson', 'Vaccination', 'Completed'),
(strftime('%s', 'now'), 'Dr. Williams', 'Cleaning', 'No Issues'),
(strftime('%s', 'now'), 'Dr. Brown', 'Exam', 'Slight Prescription'),
(strftime('%s', 'now'), 'Dr. Davis', 'Therapy', 'Improving'),
(strftime('%s', 'now'), 'Dr. Wilson', 'Testing', 'As Expected'),
(strftime('%s', 'now'), 'Dr. Martinez', 'Scan', 'Detailed Report Pending'),
(strftime('%s', 'now'), 'Dr. Garcia', 'Test', 'Pending Results'),
(strftime('%s', 'now'), 'Dr. Lopez', 'Scan', 'Clear Images'),
(strftime('%s', 'now'), 'Dr. Rodriguez', 'Ultrasound', 'Healthy Fetus');

INSERT INTO doctors (name, password)
VALUES
('admin', 'admin'),
('doc1', 'doc1'),
('doc2', 'doc2');
