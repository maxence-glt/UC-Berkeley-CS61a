CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-- Q1
CREATE TABLE by_parent_height AS
  SELECT child
  FROM parents, dogs
  WHERE parent = name
  ORDER BY height DESC;

SELECT * FROM by_parent_height;





-- Q2
CREATE TABLE siblings AS
  SELECT a.name as sibling1, b.name as sibling2, a.height as height1, b.height as height2
  FROM dogs as a, dogs as b, parents as c, parents as d
  WHERE a.name != b.name AND a.name = c.child AND b.name = d.child AND c.parent = d.parent AND a.name < b.name;

CREATE TABLE sentences AS
  SELECT s.sibling1 || " and "  || s.sibling2 || " are " || a.size || " siblings"
  FROM siblings as s, sizes as a, sizes as b
  WHERE (height1 >= a.min AND height1 <= a.max) AND (height2 >= b.min AND height2 <= b.max) AND a.size = b.size;
