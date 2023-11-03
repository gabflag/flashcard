drop database if exists dbcardcrud;
create database dbcardcrud;
use dbcardcrud;

create table user_table (
	iduser int not null auto_increment
    	, user_name varchar(255)
    	, key_pass varchar(255)
    	, primary key (iduser)
);

create table card (
	idcard int not null auto_increment
	, question varchar(500)
	, answer varchar(500)
    	, datecheck DATE
    	, createdate DATE
	, primary key (idcard)
);

INSERT INTO user_table (user_name, key_pass) VALUES ("admin", "admin");
INSERT INTO user_table (user_name, key_pass) VALUES ("root", "root");

INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 1° card', 'Answer to the 1° card', '2023/01/23', '2023/01/23');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 2° card', 'Answer to the 2° card', '2023/02/16', '2023/02/16');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 3° card', 'Answer to the 3° card', '2023/01/12', '2023/01/12');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 4° card', 'Answer to the 4° card', '2023/01/17', '2023/01/17');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 5° card', 'Answer to the 5° card', '2023/01/28', '2023/01/28');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 6° card', 'Answer to the 6° card', '2023/01/26', '2023/01/26');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 7° card', 'Answer to the 7° card', '2023/02/16', '2023/02/16');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 8° card', 'Answer to the 8° card', '2023/01/4', '2023/01/4');    
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 9° card', 'Answer to the 9° card', '2023/01/8', '2023/01/8');    
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 10° card', 'Answer to the 10° card', '2023/01/1', '2023/01/1');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 11° card', 'Answer to the 11° card', '2023/01/21', '2023/01/21');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 12° card', 'Answer to the 12° card', '2023/02/16', '2023/02/16');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 13° card', 'Answer to the 13° card', '2023/02/13', '2023/02/13');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 14° card', 'Answer to the 14° card', '2023/01/5', '2023/01/5');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 15° card', 'Answer to the 15° card', '2023/01/16', '2023/01/16');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 16° card', 'Answer to the 16° card', '2023/01/23', '2023/01/23');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 17° card', 'Answer to the 17° card', '2023/01/7', '2023/01/7');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 18° card', 'Answer to the 18° card', '2023/02/14', '2023/02/14');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 19° card', 'Answer to the 19° card', '2023/02/12', '2023/02/12');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 20° card', 'Answer to the 20° card', '2023/02/6', '2023/02/6');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 21° card', 'Answer to the 21° card', '2023/09/6', '2023/09/6');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 22° card', 'Answer to the 22° card', '2023/03/17', '2023/03/17');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 23° card', 'Answer to the 23° card', '2023/11/26', '2023/11/26');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 24° card', 'Answer to the 24° card', '2023/07/25', '2023/07/25');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 25° card', 'Answer to the 25° card', '2023/02/17', '2023/02/17');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 26° card', 'Answer to the 26° card', '2023/05/19', '2023/05/19');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 27° card', 'Answer to the 27° card', '2023/03/21', '2023/03/21');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 28° card', 'Answer to the 28° card', '2023/02/20', '2023/02/20');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 29° card', 'Answer to the 29° card', '2023/07/22', '2023/07/22');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 30° card', 'Answer to the 30° card', '2023/11/25', '2023/11/25');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 31° card', 'Answer to the 31° card', '2023/11/27', '2023/11/27');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 32° card', 'Answer to the 32° card', '2023/02/20', '2023/02/20');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 33° card', 'Answer to the 33° card', '2023/09/19', '2023/09/19');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 34° card', 'Answer to the 34° card', '2023/05/24', '2023/05/24');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 35° card', 'Answer to the 35° card', '2023/04/27', '2023/04/27');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 36° card', 'Answer to the 36° card', '2023/11/22', '2023/11/22');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 37° card', 'Answer to the 37° card', '2023/02/27', '2023/02/27');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 38° card', 'Answer to the 38° card', '2023/11/10', '2023/11/10');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 39° card', 'Answer to the 39° card', '2023/06/17', '2023/06/17');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 40° card', 'Answer to the 40° card', '2023/07/3', '2023/07/3');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 41° card', 'Answer to the 41° card', '2023/06/23', '2023/06/23');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 42° card', 'Answer to the 42° card', '2023/03/3', '2023/03/3');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 43° card', 'Answer to the 43° card', '2023/07/28', '2023/07/28');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 44° card', 'Answer to the 44° card', '2023/08/7', '2023/08/7');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 45° card', 'Answer to the 45° card', '2023/02/20', '2023/02/20');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 46° card', 'Answer to the 46° card', '2023/05/6', '2023/05/6');  
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 47° card', 'Answer to the 47° card', '2023/04/9', '2023/04/9');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 48° card', 'Answer to the 48° card', '2023/10/19', '2023/10/19');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 49° card', 'Answer to the 49° card', '2023/09/17', '2023/09/17');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 50° card', 'Answer to the 50° card', '2023/09/5', '2023/09/5');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 51° card', 'Answer to the 51° card', '2023/10/25', '2023/10/25');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 52° card', 'Answer to the 52° card', '2023/02/21', '2023/02/21');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 53° card', 'Answer to the 53° card', '2023/05/15', '2023/05/15');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 54° card', 'Answer to the 54° card', '2023/12/6', '2023/12/6');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 55° card', 'Answer to the 55° card', '2023/07/19', '2023/07/19');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 56° card', 'Answer to the 56° card', '2023/09/17', '2023/09/17');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 57° card', 'Answer to the 57° card', '2023/06/4', '2023/06/4');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 58° card', 'Answer to the 58° card', '2023/06/21', '2023/06/21');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 59° card', 'Answer to the 59° card', '2023/08/6', '2023/08/6');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 60° card', 'Answer to the 60° card', '2023/06/1', '2023/06/1');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 61° card', 'Answer to the 61° card', '2023/12/21', '2023/12/21');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 62° card', 'Answer to the 62° card', '2023/06/8', '2023/06/8');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 63° card', 'Answer to the 63° card', '2023/08/22', '2023/08/22');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 64° card', 'Answer to the 64° card', '2023/06/27', '2023/06/27');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 65° card', 'Answer to the 65° card', '2023/05/2', '2023/05/2');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 66° card', 'Answer to the 66° card', '2023/12/22', '2023/12/22');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 67° card', 'Answer to the 67° card', '2023/03/26', '2023/03/26');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 68° card', 'Answer to the 68° card', '2023/10/14', '2023/10/14');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 69° card', 'Answer to the 69° card', '2023/02/28', '2023/02/28');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 70° card', 'Answer to the 70° card', '2023/07/3', '2023/07/3');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 71° card', 'Answer to the 71° card', '2023/08/19', '2023/08/19');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 72° card', 'Answer to the 72° card', '2023/03/2', '2023/03/2');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 73° card', 'Answer to the 73° card', '2023/04/9', '2023/04/9');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 74° card', 'Answer to the 74° card', '2023/07/18', '2023/07/18');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 75° card', 'Answer to the 75° card', '2023/02/18', '2023/02/18');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 76° card', 'Answer to the 76° card', '2023/08/3', '2023/08/3');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 77° card', 'Answer to the 77° card', '2023/07/12', '2023/07/12');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 78° card', 'Answer to the 78° card', '2023/03/23', '2023/03/23');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 79° card', 'Answer to the 79° card', '2023/07/6', '2023/07/6');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 80° card', 'Answer to the 80° card', '2023/11/27', '2023/11/27');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 81° card', 'Answer to the 81° card', '2023/05/20', '2023/05/20');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 82° card', 'Answer to the 82° card', '2023/02/26', '2023/02/26');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 83° card', 'Answer to the 83° card', '2023/02/19', '2023/02/19');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 84° card', 'Answer to the 84° card', '2023/04/1', '2023/04/1');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 85° card', 'Answer to the 85° card', '2023/08/6', '2023/08/6');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 86° card', 'Answer to the 86° card', '2023/08/1', '2023/08/1');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 87° card', 'Answer to the 87° card', '2023/09/22', '2023/09/22');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 88° card', 'Answer to the 88° card', '2023/07/28', '2023/07/28');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 89° card', 'Answer to the 89° card', '2023/08/11', '2023/08/11');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 90° card', 'Answer to the 90° card', '2023/03/9', '2023/03/9');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 91° card', 'Answer to the 91° card', '2023/03/7', '2023/03/7');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 92° card', 'Answer to the 92° card', '2023/11/8', '2023/11/8');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 93° card', 'Answer to the 93° card', '2023/11/15', '2023/11/15');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 94° card', 'Answer to the 94° card', '2023/08/25', '2023/08/25');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 95° card', 'Answer to the 95° card', '2023/08/2', '2023/08/2');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 96° card', 'Answer to the 96° card', '2023/09/4', '2023/09/4');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 97° card', 'Answer to the 97° card', '2023/07/23', '2023/07/23');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 98° card', 'Answer to the 98° card', '2023/03/19', '2023/03/19');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 99° card', 'Answer to the 99° card', '2023/03/18', '2023/03/18');
INSERT INTO card (question, answer, datecheck, createdate)VALUES ('Question contained in the 100° card', 'Answer to the 100° card', '2023/10/19', '2023/10/19');

select * from card WHERE datecheck <= curdate();
select * from card WHERE datecheck > curdate();

