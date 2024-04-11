CREATE TABLE Members
(
    member_id  SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name  VARCHAR(255) NOT NULL,
    email      VARCHAR(255) NOT NULL,
    password   VARCHAR(255) NOT NULL,
    weight     NUMERIC,
    height     NUMERIC
);

CREATE TABLE Trainers
(
    trainer_id   SERIAL PRIMARY KEY,
    first_name   VARCHAR(255) NOT NULL,
    last_name    VARCHAR(255) NOT NULL,
    email        VARCHAR(255) NOT NULL,
    password     VARCHAR(255) NOT NULL
);

CREATE TABLE AdministrativeStaff
(
    admin_staff_id SERIAL PRIMARY KEY,
    first_name     VARCHAR(255) NOT NULL,
    last_name      VARCHAR(255) NOT NULL,
    email          VARCHAR(255) NOT NULL,
    password       VARCHAR(255) NOT NULL
);

CREATE TABLE Goals
(
    goal_id     SERIAL PRIMARY KEY,
    member_id   INT NOT NULL,
    exercise    VARCHAR(255) NOT NULL,
    goal_weight NUMERIC,
    goal_time   NUMERIC,
    reached     BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (member_id)
        REFERENCES Members (member_id)
);

CREATE TABLE Availabilities
(
    availability_id  SERIAL PRIMARY KEY,
    trainer_id       INT NOT NULL,
    day              VARCHAR(255) NOT NULL,
    start_time       TIME,
    end_time         TIME,
    FOREIGN KEY (trainer_id)
        REFERENCES Trainers (trainer_id)
);

CREATE TABLE TrainingSessions
(
    session_id   SERIAL PRIMARY KEY,
    member_id    INT NOT NULL,
    trainer_id   INT NOT NULL,
    session_time TIME,
    FOREIGN KEY (member_id)
        REFERENCES Members (member_id),
    FOREIGN KEY (trainer_id)
        REFERENCES Trainers (trainer_id)
);

CREATE TABLE FitnessClasses
(
    class_id   SERIAL PRIMARY KEY,
    trainer_id INT NOT NULL,
    class_time TIME,
    FOREIGN KEY (trainer_id)
        REFERENCES Trainers (trainer_id)
);

CREATE TABLE FitnessClassMembers
(
    class_id  INT,
    member_id INT NOT NULL,
    FOREIGN KEY (member_id)
        REFERENCES Members (member_id)
);

CREATE TABLE RoomBookings
(
    booking_id     SERIAL PRIMARY KEY,
    room_number    INT NOT NULL,
    booking_time   TIME,
    admin_staff_id INT NOT NULL,
    FOREIGN KEY (admin_staff_id)
        REFERENCES AdministrativeStaff (admin_staff_id)
);

CREATE TABLE Equipments
(
    equipment_id     SERIAL PRIMARY KEY,
    equipment_name   VARCHAR(255) NOT NULL,
    last_maintenance DATE         NOT NULL,
    next_maintenance DATE         NOT NULL
);

CREATE TABLE Payments
(
    payment_id   SERIAL PRIMARY KEY,
    member_id    INT     NOT NULL,
    amount       NUMERIC NOT NULL,
    payment_date DATE    NOT NULL,
    posted       BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (member_id)
        REFERENCES Members (member_id)
);