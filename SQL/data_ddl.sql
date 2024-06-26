CREATE TABLE Members
(
    member_id  SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name  VARCHAR(255) NOT NULL,
    email      VARCHAR(255) NOT NULL,
    password   VARCHAR(255) NOT NULL,
    weight     NUMERIC,
    height     NUMERIC,
    account_balance NUMERIC DEFAULT 0
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
    day  VARCHAR(255) NOT NULL,
    trainer_id   INT NOT NULL,
    session_start_time TIME,
    session_end_time   TIME,
    FOREIGN KEY (member_id)
        REFERENCES Members (member_id),
    FOREIGN KEY (trainer_id)
        REFERENCES Trainers (trainer_id)
);

CREATE TABLE FitnessClasses
(
    class_id   SERIAL PRIMARY KEY,
    trainer_id INT NOT NULL,
    day  VARCHAR(255) NOT NULL,
    class_start_time TIME,
    class_end_time   TIME,
    admin_staff_id INT NOT NULL,
    FOREIGN KEY (trainer_id)
        REFERENCES Trainers (trainer_id),
    FOREIGN KEY (admin_staff_id)
        REFERENCES AdministrativeStaff (admin_staff_id)
);

CREATE TABLE FitnessClassMembers
(
    id SERIAL PRIMARY KEY,
    class_id  INT NOT NULL,
    member_id INT NOT NULL,
    FOREIGN KEY (class_id)
        REFERENCES FitnessClasses (class_id),
    FOREIGN KEY (member_id)
        REFERENCES Members (member_id)
);

CREATE TABLE RoomBookings
(
    booking_id     SERIAL PRIMARY KEY,
    room_number    INT NOT NULL,
    date DATE NOT NULL,
    booking_start_time   TIME,
    booking_end_time   TIME,
    admin_staff_id INT NOT NULL,
    FOREIGN KEY (admin_staff_id)
        REFERENCES AdministrativeStaff (admin_staff_id)
);

CREATE TABLE Equipments
(
    equipment_id     SERIAL PRIMARY KEY,
    equipment_name   VARCHAR(255) NOT NULL,
    last_maintenance DATE         NOT NULL,
    next_maintenance DATE         NOT NULL,
    admin_staff_id INT NOT NULL,
    FOREIGN KEY (admin_staff_id)
        REFERENCES AdministrativeStaff (admin_staff_id)
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