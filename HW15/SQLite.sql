-- SQLite
-- CREATE TABLE authors (
--     id INT PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50)
-- );

-- CREATE TABLE books (
--     id INT PRIMARY KEY,
--     title VARCHAR(100),
--     author_id INT,
--     publication_year INT,
--     FOREIGN KEY (author_id) REFERENCES authors(id)
-- );

-- CREATE TABLE sales (
--     id INT PRIMARY KEY,
--     book_id INT,
--     quantity INT,
--     FOREIGN KEY (book_id) REFERENCES books(id)
-- );

-- INSERT INTO authors (id, first_name, last_name) VALUES
-- (4, 'Александр', 'Пушкин');
-- (1, 'Лев', 'Толстой'),
-- (2, 'Федор', 'Достоевский'),
-- (3, 'Антон', 'Чехов');

-- INSERT INTO books (id, title, author_id) VALUES
-- (6, 'Мастер и Маргарита', NULL);
-- (1, 'Война и мир', 1),
-- (2, 'Преступление и наказание', 2),
-- (3, 'Чайка', 3),
-- (4, 'Анна Каренина', 1),
-- (5, 'Идиот', 2);

-- INSERT INTO sales (id, book_id, quantity) VALUES
-- (1, 1, 150),
-- (2, 2, 200),
-- (3, 3, 75),
-- (4, 4, 100),
-- (5, 5, 120);

-- SELECT books.title,
-- authors.first_name,
-- authors.last_name
-- FROM books
-- INNER JOIN authors on books.author_id = authors.id;

-- SELECT books.title,
-- authors.first_name,
-- authors.last_name
-- FROM authors
-- LEFT JOIN books on books.author_id = authors.id;

-- SELECT books.title,
-- authors.first_name,
-- authors.last_name
-- FROM books
-- INNER JOIN authors on books.author_id = authors.id;

-- SELECT 
--     authors.first_name,
--     authors.last_name,
--     books.title,
--     sales.quantity
-- FROM 
--     authors
-- INNER JOIN 
--     books ON authors.id = books.author_id
-- INNER JOIN 
--     sales ON books.id = sales.book_id;

-- SELECT 
--     authors.first_name,
--     authors.last_name,
--     books.title,
--     sales.quantity
-- FROM 
--     authors
-- LEFT JOIN 
--     books ON authors.id = books.author_id
-- LEFT JOIN 
--     sales ON books.id = sales.book_id;

