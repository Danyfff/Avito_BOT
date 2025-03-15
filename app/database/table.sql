CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url VARCHAR,
    name VARCHAR,
    last_update_time DATA
);
-- 1 Задание

SELECT 
    CONCAT(p.last_name, ' ', p.first_name) AS "ФИО пациента",
    e.create_date AS "Дата обращения",
    a.name AS "Название действия"
FROM 
    Patients p
INNER JOIN 
    Events e ON p.id = e.patient_id
INNER JOIN 
    Actions a ON e.id = a.event_id
WHERE 
    p.last_name = 'Иванов' 
    AND p.first_name = 'Иван';


-- 2 Задание

ALTER TABLE Patients
ADD COLUMN sex TINYINT(1) DEFAULT 0 NOT NULL COMMENT '0-неопределено, 1-М, 2-Ж';

UPDATE Patients p
SET p.sex = CASE 
   
    WHEN p.patronymic LIKE '%ович' OR p.patronymic LIKE '%евич' THEN 1
    WHEN p.patronymic LIKE '%овна' OR p.patronymic LIKE '%евна' THEN 2 
    WHEN (p.patronymic = '' OR p.patronymic NOT LIKE '%ович' AND p.patronymic NOT LIKE '%евич' 
          AND p.patronymic NOT LIKE '%овна' AND p.patronymic NOT LIKE '%евна')
         AND (p.last_name LIKE '%ов' OR p.last_name LIKE '%ев') THEN 1 
    WHEN (p.patronymic = '' OR p.patronymic NOT LIKE '%ович' AND p.patronymic NOT LIKE '%евич' 
          AND p.patronymic NOT LIKE '%овна' AND p.patronymic NOT LIKE '%евна')
         AND (p.last_name LIKE '%ова' OR p.last_name LIKE '%ева') THEN 2
    ELSE 0
END
WHERE p.deleted = 0;

