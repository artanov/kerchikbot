 CREATE TABLE users
(
	user_id int4 NULL,
	user_name varchar(40) NULL,

    CONSTRAINT users_pk
    PRIMARY KEY (user_id)
);

 CREATE TABLE films
(
    film_id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	film_name varchar(50) NULL,
	user_id int4,

    CONSTRAINT films_pk
    PRIMARY KEY (film_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id) 
    on delete cascade
    on update cascade
);


 CREATE TABLE todo_list
(
	task_id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	task_name varchar NULL,
	user_id int4,
    
    CONSTRAINT todo_list_pk
    PRIMARY KEY (task_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id) 
    on delete cascade
    on update cascade
);

 CREATE TABLE filmsfavorites
(
	favorites_id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	favorites_name varchar(100) NULL,
	user_id int4,

    CONSTRAINT favorites_id_pk
    PRIMARY KEY (favorites_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id) 
    on delete cascade
    on update cascade
);

CREATE ROLE admindb WITH PASSWORD 'password'
	SUPERUSER
	CREATEDB
	CREATEROLE
	INHERIT
	LOGIN
	NOREPLICATION
	NOBYPASSRLS
	CONNECTION LIMIT -1;