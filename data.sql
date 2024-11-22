INSERT INTO author (author_id, author_name, author_dob, author_origin, about) VALUES
(1, 'J.K. Rowling', '1965-07-31', 'United Kingdom', 'Author of Harry Potter series'),
(2, 'George Orwell', '1903-06-25', 'India', 'Author of 1984 and Animal Farm'),
(3, 'Agatha Christie', '1890-09-15', 'United Kingdom', 'Queen of Mystery novels'),
(4, 'Mark Twain', '1835-11-30', 'United States', 'Author of Adventures of Huckleberry Finn'),
(5, 'Jane Austen', '1775-12-16', 'United Kingdom', 'Known for novels like Pride and Prejudice'),
(6, 'Charles Dickens', '1812-02-07', 'United Kingdom', 'Famous for Oliver Twist and A Christmas Carol'),
(7, 'Ernest Hemingway', '1899-07-21', 'United States', 'Nobel Prize-winning author'),
(8, 'Leo Tolstoy', '1828-09-09', 'Russia', 'Author of War and Peace'),
(9, 'Gabriel García Márquez', '1927-03-06', 'Colombia', 'Author of One Hundred Years of Solitude'),
(10, 'F. Scott Fitzgerald', '1896-09-24', 'United States', 'Author of The Great Gatsby');

INSERT INTO publisher (publisher_id, publisher_name, publisher_address, about) VALUES
(1, 'Penguin Random House', 'New York, USA', 'Leading global publisher'),
(2, 'HarperCollins', 'New York, USA', 'Publisher of fiction and non-fiction'),
(3, 'Macmillan Publishers', 'London, UK', 'One of the largest publishing companies'),
(4, 'Simon & Schuster', 'New York, USA', 'American publishing company'),
(5, 'Hachette Book Group', 'Paris, France', 'French-based publishing house'),
(6, 'Oxford University Press', 'Oxford, UK', 'University press and educational publisher'),
(7, 'Cambridge University Press', 'Cambridge, UK', 'Academic publisher'),
(8, 'Scholastic Corporation', 'New York, USA', 'Publisher of childrens books'),
(9, 'Bloomsbury Publishing', 'London, UK', 'Known for publishing Harry Potter'),
(10, 'Pearson Education', 'London, UK', 'Publisher of academic and educational books');

INSERT INTO shelf (shelf_id, quantity, shelf_floor, shelf_rows, shelf_cols) VALUES
(1, 100, 1, 10, 10),
(2, 80, 1, 8, 10),
(3, 120, 2, 12, 10),
(4, 60, 2, 6, 10),
(5, 90, 3, 9, 10),
(6, 110, 3, 11, 10),
(7, 75, 4, 7, 10),
(8, 50, 4, 5, 10),
(9, 95, 5, 9, 10),
(10, 105, 5, 10, 10);

INSERT INTO vendor (vendor_id, vendor_name, vendor_address, about) VALUES
(1, 'BookWorld', 'Delhi, India', 'Vendor for all genres of books'),
(2, 'Literature Hub', 'Mumbai, India', 'Specialized in novels and literature'),
(3, 'Education Plus', 'Pune, India', 'Deals in educational books'),
(4, 'Fiction Sphere', 'Chennai, India', 'Known for fiction novels'),
(5, 'TechBooks', 'Bangalore, India', 'Specialized in technology and engineering books'),
(6, 'History Makers', 'Kolkata, India', 'Focused on history and culture'),
(7, 'Science Universe', 'Hyderabad, India', 'Deals in science and research books'),
(8, 'Kids World', 'Delhi, India', 'Vendor for childrens books'),
(9, 'Academic Sources', 'Lucknow, India', 'Focused on academic publications'),
(10, 'Art & Design', 'Jaipur, India', 'Vendor for art and design books');

INSERT INTO book (book_id, author_id, book_title, publisher_id, vendor_id, shelf_id, category, price, language_name, subject_name, genre, date_of_publishing, date_of_addition, availability, shelf_date, bought_on, cover_page) VALUES
(1, 1, 'Harry Potter and the Philosopher\'s Stone', 9, 1, 1, 'Fiction', 399.99, 'English', 'Fantasy', 'Fantasy', '1997-06-26', '2024-01-15', 10, '2024-01-16', '2024-01-14', NULL),
(2, 2, '1984', 2, 2, 2, 'Dystopian', 299.99, 'English', 'Fiction', 'Dystopian', '1949-06-08', '2024-02-12', 5, '2024-02-13', '2024-02-11', NULL),
(3, 3, 'Murder on the Orient Express', 1, 3, 3, 'Mystery', 199.99, 'English', 'Detective', 'Mystery', '1934-01-01', '2024-03-10', 8, '2024-03-11', '2024-03-09', NULL),
(4, 4, 'Adventures of Huckleberry Finn', 5, 4, 4, 'Classic', 249.99, 'English', 'Adventure', 'Classic', '1884-12-10', '2024-04-05', 6, '2024-04-06', '2024-04-04', NULL),
(5, 5, 'Pride and Prejudice', 6, 5, 5, 'Romance', 159.99, 'English', 'Romance', 'Classic', '1813-01-28', '2024-05-01', 12, '2024-05-02', '2024-04-30', NULL),
(6, 6, 'Oliver Twist', 4, 6, 6, 'Classic', 219.99, 'English', 'Drama', 'Classic', '1837-01-01', '2024-06-12', 7, '2024-06-13', '2024-06-11', NULL),
(7, 7, 'The Old Man and the Sea', 5, 7, 7, 'Literature', 279.99, 'English', 'Fiction', 'Drama', '1952-09-01', '2024-07-20', 4, '2024-07-21', '2024-07-19', NULL),
(8, 8, 'War and Peace', 7, 8, 8, 'Historical', 349.99, 'Russian', 'History', 'Historical', '1869-01-01', '2024-08-05', 5, '2024-08-06', '2024-08-04', NULL),
(9, 9, 'One Hundred Years of Solitude', 8, 9, 9, 'Fiction', 399.99, 'Spanish', 'Magic Realism', 'Magic Realism', '1967-06-05', '2024-09-01', 6, '2024-09-02', '2024-08-31', NULL),
(10, 10, 'The Great Gatsby', 10, 10, 10, 'Classic', 199.99, 'English', 'Fiction', 'Tragedy', '1925-04-10', '2024-10-10', 9, '2024-10-11', '2024-10-09', NULL),
(11, 1, 'Harry Potter and the Chamber of Secrets', 9, 1, 1, 'Fiction', 399.99, 'English', 'Fantasy', 'Fantasy', '1998-07-02', '2024-11-15', 7, '2024-11-16', '2024-11-14', NULL),
(12, 3, 'And Then There Were None', 1, 3, 3, 'Mystery', 249.99, 'English', 'Detective', 'Mystery', '1939-11-06', '2024-01-05', 10, '2024-01-06', '2024-01-04', NULL),
(13, 5, 'Sense and Sensibility', 6, 5, 5, 'Romance', 159.99, 'English', 'Romance', 'Classic', '1811-10-30', '2024-02-18', 6, '2024-02-19', '2024-02-17', NULL),
(14, 7, 'A Farewell to Arms', 5, 7, 7, 'War', 299.99, 'English', 'Drama', 'Classic', '1929-09-27', '2024-03-11', 7, '2024-03-12', '2024-03-10', NULL),
(15, 6, 'David Copperfield', 4, 6, 6, 'Classic', 279.99, 'English', 'Drama', 'Classic', '1850-05-01', '2024-04-25', 5, '2024-04-26', '2024-04-24', NULL),
(16, 8, 'Anna Karenina', 7, 8, 8, 'Romance', 399.99, 'Russian', 'Drama', 'Classic', '1877-01-01', '2024-05-30', 6, '2024-05-31', '2024-05-29', NULL),
(17, 9, 'Love in the Time of Cholera', 8, 9, 9, 'Fiction', 349.99, 'Spanish', 'Drama', 'Magic Realism', '1985-06-05', '2024-06-15', 8, '2024-06-16', '2024-06-14', NULL),
(18, 10, 'Tender is the Night', 10, 10, 10, 'Classic', 249.99, 'English', 'Drama', 'Tragedy', '1934-04-12', '2024-07-20', 10, '2024-07-21', '2024-07-19', NULL),
(19, 1, 'Harry Potter and the Prisoner of Azkaban', 9, 1, 1, 'Fiction', 399.99, 'English', 'Fantasy', 'Fantasy', '1999-07-08', '2024-08-22', 6, '2024-08-23', '2024-08-21', NULL),
(20, 2, 'Animal Farm', 2, 2, 2, 'Satire', 299.99, 'English', 'Fiction', 'Political', '1945-08-17', '2024-09-10', 9, '2024-09-11', '2024-09-09', NULL),
(21, 4, 'The Prince and the Pauper', 5, 4, 4, 'Classic', 229.99, 'English', 'Fiction', 'Classic', '1881-01-01', '2024-10-14', 8, '2024-10-15', '2024-10-13', NULL),
(22, 5, 'Emma', 6, 5, 5, 'Romance', 199.99, 'English', 'Drama', 'Classic', '1815-12-23', '2024-11-03', 7, '2024-11-04', '2024-11-02', NULL),
(23, 6, 'A Tale of Two Cities', 4, 6, 6, 'Classic', 319.99, 'English', 'Drama', 'Historical', '1859-04-30', '2024-12-05', 10, '2024-12-06', '2024-12-04', NULL),
(24, 7, 'For Whom the Bell Tolls', 5, 7, 7, 'War', 299.99, 'English', 'Drama', 'Historical', '1940-10-21', '2024-01-12', 4, '2024-01-13', '2024-01-11', NULL),
(25, 8, 'The Death of Ivan Ilyich', 7, 8, 8, 'Philosophy', 199.99, 'Russian', 'Fiction', 'Philosophy', '1886-01-01', '2024-02-20', 5, '2024-02-21', '2024-02-19', NULL);



