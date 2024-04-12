INSERT INTO Members (first_name, last_name, email, password, weight, height)
VALUES 
('Kina', 'Zhan', 'kinazhan@gmail.com', 'password', 70, 170),
('Peien', 'Liu', 'peienliu@gmail.com', '1234', 78.4, 184),
('Steve', 'Williams', 'stevewilliams@gmail.com', 'qwer', 80.4, 175);

INSERT INTO Trainers (first_name, last_name, email, password)
VALUES 
('Emma', 'Johnson', 'emma.johnson@example.com', 'pass123'),
('James', 'Smith', 'james.smith@example.com', 'pass456'),
('Sophia', 'Williams', 'sophia.williams@example.com', 'pass789');

INSERT INTO AdministrativeStaff (first_name, last_name, email, password)
VALUES 
('Oliver', 'Brown', 'oliver.brown@example.com', 'admin123'),
('Ava', 'Taylor', 'ava.taylor@example.com', 'admin456'),
('Lucas', 'Miller', 'lucas.miller@example.com', 'admin789');

INSERT INTO Goals (member_id, exercise, goal_weight, goal_time, reached)
VALUES 
(1, 'Squat', 150, null, FALSE),
(2, 'Treadmill', null, 30, TRUE),
(3, 'Bench Press',100, null, FALSE);

INSERT INTO Availabilities (trainer_id, day, start_time, end_time)
VALUES 
(1, 'Monday', '09:00:00', '17:00:00'),
(2, 'Tuesday', '10:00:00', '18:00:00'),
(3, 'Wednesday', '11:00:00', '19:00:00');

INSERT INTO TrainingSessions (member_id, trainer_id, day, session_start_time, session_end_time)
VALUES 
(1, 1, 'Monday', '10:00:00', '11:00:00'),
(2, 2, 'Tuesday', '11:00:00', '12:00:00'),
(3, 3, 'Wednesday', '12:00:00', '12:30:00');

INSERT INTO FitnessClasses (trainer_id, day, class_start_time, class_end_time, admin_staff_id)
VALUES 
(1, 'Monday', '09:00:00', '10:00:00', 1),
(2, 'Tuesday', '13:00:00', '14:00:00', 2),
(3, 'Wednesday', '15:00:00', '16:30:00', 3);

INSERT INTO FitnessClassMembers (class_id, member_id)
VALUES 
(1, 1),
(2, 2),
(3, 3);

INSERT INTO RoomBookings (room_number, date, booking_start_time, booking_end_time, admin_staff_id)
VALUES 
(101, '2024-01-01', '09:00:00', '10:00:00', 1),
(102, '2024-02-01', '10:00:00', '13:00:00', 2),
(103, '2024-03-01', '11:00:00', '11:30:00', 3);

INSERT INTO Equipments (equipment_name, last_maintenance, next_maintenance, admin_staff_id)
VALUES 
('Treadmill', '2024-01-01', '2024-07-01', 1),
('Dumbbell', '2024-02-01', '2024-08-01', 2),
('Bike', '2024-03-01', '2024-09-01', 3);

INSERT INTO Payments (member_id, amount, payment_date, posted)
VALUES 
(1, 100.00, '2024-01-01', TRUE),
(2, 150.00, '2024-02-01', TRUE),
(3, 200.00, '2024-03-01', FALSE);