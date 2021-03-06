CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    genre_id uuid NOT NULL REFERENCES content.genre (id)
    ON DELETE CASCADE,
    film_work_id uuid NOT NULL REFERENCES content.film_work (id)
    ON DELETE CASCADE,
    created timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL REFERENCES content.film_work (id)
    ON DELETE CASCADE,
    person_id uuid NOT NULL REFERENCES content.person (id)
    ON DELETE CASCADE,
    role TEXT NOT NULL,
    created timestamp with time zone
);

CREATE UNIQUE INDEX film_work_pkey ON content.film_work USING btree (id);
CREATE UNIQUE INDEX genre_film_work_pkey ON content.genre_film_work USING btree (id);
CREATE UNIQUE INDEX genre_pkey ON content.genre USING btree (id);
CREATE UNIQUE INDEX person_pkey ON content.person USING btree (id);
CREATE UNIQUE INDEX person_film_work_pkey ON content.person_film_work USING btree (id);