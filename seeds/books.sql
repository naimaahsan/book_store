-- -------------------------------------------------------------
-- TablePlus 7.2.2(722)
--
-- https://tableplus.com/
--
-- Database: book_store_app
-- Generation Time: 2026-07-02 09:01:58.4160
-- -------------------------------------------------------------


DROP TABLE IF EXISTS "public"."books";
-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS books_id_seq;

-- Table Definition
CREATE TABLE "public"."books" (
    "id" int4 NOT NULL DEFAULT nextval('books_id_seq'::regclass),
    "title" text,
    "author" text,
    "image_url" text,
    PRIMARY KEY ("id")
);

TRUNCATE table books;

INSERT INTO "public"."books" ("title", "author", "image_url") VALUES
('The Gruffalo', 'Julia Donaldson', 'https://voxblock.co.uk/cdn/shop/files/the-gruffalo-audiobook-character.webp?v=1714987686'),
('Ada Twist, Scientist', 'Andrea Beaty', 'https://m.media-amazon.com/images/I/81m0eJVO9vL._AC_UF894,1000_QL80_.jpg'),
('The Girl Who Drank the Moon', 'Kelly Barnhill', 'https://m.media-amazon.com/images/I/91bDYQ4S5WL._AC_UF894,1000_QL80_.jpg'),
('Dragons in a Bag', 'Zetta Elliott', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvN310x7_U1b9twPx5SrU95sxENWyIQ4nlEY2HUlwQ1g&s=10');

