-- drop test user if exists
DROP USER IF EXISTS 'pysports_user'@'localhost';

-- create pysports_user
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
-- grant all privileges to pysports_user on pysports database
GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost';

-- drop tablels and constraints if present
DROP TABLE IF EXISTS team;
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team_players;

-- create the team table
CREATE TABLE team (
    team_id     INT             NOT NULL    AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
);

-- create the player table and set the foreign key
CREATE TABLE player (
    player_id       INT             NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75)     NOT NULL,
    last_name       VARCHAR(75)     NOT NULL,
    team_id         INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);

-- insert records in team records
INSERT INTO team(team_name, mascot) VALUES('Team Gandalf', 'White Wizards');
INSERT INTO team(team_name, mascot) VALUES('Team Sauron', 'Orcs');

-- insert team 1 player records
INSERT INTO player(first_name, last_name, team_id) VALUES('Thorin', 'Oakenshield', 1);
INSERT INTO player(first_name, last_name, team_id) VALUES('Bilbo', 'Baggins', 1);
INSERT INTO player(first_name, last_name, team_id) VALUES('Frodo', 'Baggins', 1);

-- insert team 2 player records
INSERT INTO player(first_name, last_name, team_id) VALUES('Saruman', 'The White', 2);
INSERT INTO player(first_name, last_name, team_id) VALUES('Angmar', 'Witch-king', 2);
INSERT INTO player(first_name, last_name, team_id) VALUES('Azog', 'The Defiler', 2);

-- select a record from the team table
SELECT team_id FROM team WHERE team_name = 'Team Sauron';
