


Select @@SERVERNAME

use ForTestingClass6


select * from Roster

select * from INFORMATION_SCHEMA.TABLES




drop database ForTestingClass6

-- 1️⃣ Set the database to SINGLE_USER mode to disconnect all connections
ALTER DATABASE ForTestingClass6 SET SINGLE_USER WITH ROLLBACK IMMEDIATE;

-- 2️⃣ Drop the database
DROP DATABASE ForTestingClass6;



drop database ForTestingClass2

-- 1️⃣ Set the database to SINGLE_USER mode to disconnect all connections
ALTER DATABASE ForTestingClass2 SET SINGLE_USER WITH ROLLBACK IMMEDIATE;

-- 2️⃣ Drop the database
DROP DATABASE ForTestingClass2;



drop database ForTestingClass3

-- 1️⃣ Set the database to SINGLE_USER mode to disconnect all connections
ALTER DATABASE ForTestingClass3 SET Multi_USER WITH ROLLBACK IMMEDIATE;

-- 2️⃣ Drop the database
DROP DATABASE ForTestingClass3;


drop database ForTestingClass4

-- 1️⃣ Set the database to SINGLE_USER mode to disconnect all connections
ALTER DATABASE ForTestingClass4 SET SINGLE_USER WITH ROLLBACK IMMEDIATE;

-- 2️⃣ Drop the database
DROP DATABASE ForTestingClass4;


drop database ForTestingClass6

-- 1️⃣ Set the database to SINGLE_USER mode to disconnect all connections
ALTER DATABASE ForTestingClass6 SET Multi_USER WITH ROLLBACK IMMEDIATE;

-- 2️⃣ Drop the database
DROP DATABASE ForTestingClass6;

use RosterDatabase



select * from Roster



