# Library Management system
A Library Management System is a software built to handle the primary housekeeping functions of a library. Libraries rely on library management systems to manage asset collections as well as relationships with their members. Library management systems help libraries keep track of the books and their checkouts, as well as members’ subscriptions and profiles.

Library management systems also involve maintaining the database for entering new books and recording books that have been borrowed with their respective due dates.

## System Requirements:
1. Library member should be able to search book by title, authors, subject and publication date
2. Book will have unique id, category and rack number.
3. There can be multiple copies of the same book.
4. Onboard the members and books
5. Retrive information like who took books and books checkout by specfic members.
6. Max limit on how many books (5) each members can checkout.
7. Max limit on how many days book (10) can be kept and fine after that (1/day)
8. Members should be able to reserve the books that are not currently available.
9. The system should send notification whenever the reserved books become available, as well as when the book is not returned in the due date.

# Usecase Diagram
Main actors:
1. Librarian : CRUD books, book items and users. Issue, reverve return books
2. Member : search books, reserve books, renew books and return books
3. System : send notifications for overdue books, cancel reservation

Top usecases:
1. CRUD books
2. Search catalog - by title, authors, subject and publication date
3. Register member / cancel member
4. Checkout book: borrow book
5. Reserve book: reserve book which is not available
6. Return book
8. Renew book
9. Send notification for overdue books

# Class diagram:
1. Library
2. Book
3. BookItem
4. Account: librarian, member
5. LibraryCard
6. BookReservation
7. BookLending
8. Catalog
9. Fine
10. Author
11. Rack
12. Notification

Interfaces:
-------
Account
Person
Book

Activity Diagram



