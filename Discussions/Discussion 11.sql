-- Discussion 11 of UC Berkeley's cs61a spring 2020 course
-- https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/disc11.pdf

CREATE TABLE records AS
  SELECT "Ben Bitdiddle" AS name, "Computer" AS division, "Wizard" AS title, 60000 AS salary, "Oliver Warbucks" AS supervisor UNION
  SELECT "Alyssa P Hacker", "Computer", "Programmer", 40000, "Ben Bitdiddle" UNION
  SELECT "Cy D Fect", "Computer", "Programmer", 35000, "Ben Bitdiddle" UNION
  SELECT "Lem E Tweakit", "Computer", "Technician", 25000, "Ben Bitdiddle" UNION
  SELECT "Louis Reasoner", "Computer", "Programmer Trainee", 30000, "Ben Bitdiddle" UNION
  SELECT "Oliver Warbucks", "Administration", "Big Wheel", 150000, "Oliver Warbucks" UNION
  SELECT "Eben Scrooge", "Accounting", "Chief Accountant", 75000, "Oliver Warbucks" UNION
  SELECT "Robert Cratchet", "Accounting", "Scrivener", 18000, "Eben Scrooge";

CREATE TABLE meetings AS
  SELECT "Accounting" AS division, "Monday" AS day, "9am" AS time UNION
  SELECT "Computer", "Wednesday", "4pm" UNION 
  SELECT "Administration", "Monday", "11am" UNION 
  SELECT "Administration", "Wednesday", "4pm";

-- 2
SELECT * 
  FROM records 
  WHERE supervisor = "Oliver Warbucks";

SELECT * 
  FROM records
   WHERE supervisor = name;

SELECT * 
  FROM records 
  WHERE salary > 50000 
  ORDER BY name;





-- 3
SELECT day, time 
  FROM records, meetings 
  WHERE supervisor = "Oliver Warbucks";

SELECT a.name
  FROM records AS a, records AS b
  WHERE a.supervisor = b.name and b.division != a.division;

SELECT a.name, b.name 
  FROM records AS a, records AS b, meetings AS c, meetings AS d
  WHERE ((a.division = c.division) AND (b.division = d.division)) 
        AND (c.time = d.time)
        AND a.name != b.name
        AND a.name < b.name;





-- 4
SELECT supervisor, SUM(salary)
  FROM records
  GROUP BY supervisor;

-- SELECT day
--   FROM records, meetings
--   GROUP BY day
--   HAVING COUNT(*) < 5

SELECT division
  FROM records
  GROUP BY division
  HAVING SUM(salary) < 100000
         AND COUNT(*) > 1;
