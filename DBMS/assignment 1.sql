-- 1.SQL script to create and populate a patient database
INSERT INTO `paitent_db`.`patient` (`P_ID`, `P_NAME`, `P_DOB`, `P_AILMENT`, `P_BILL`, `P_CONTACT`, `P_ADDRESS`) VALUES ('P001', 'H.Das', '1965-07-13', 'HEART', '23000', 'KOLKATA', 'PATNA');
INSERT INTO `paitent_db`.`patient` (`P_ID`, `P_NAME`, `P_DOB`, `P_AILMENT`, `P_BILL`, `P_CONTACT`, `P_ADDRESS`) VALUES ('P002', 'P.Sen', '1981-07-31', 'LUNG', '18000', 'KOLKATA', 'KOLKATA');
INSERT INTO `paitent_db`.`patient` (`P_ID`, `P_NAME`, `P_DOB`, `P_AILMENT`, `P_BILL`, `P_CONTACT`, `P_ADDRESS`) VALUES ('P003', 'M.Ray', '1963-12-12', 'HEART', '19950', 'PATNA', 'ODISHA');
INSERT INTO `paitent_db`.`patient` (`P_ID`, `P_NAME`, `P_DOB`, `P_AILMENT`, `P_BILL`, `P_CONTACT`, `P_ADDRESS`) VALUES ('P004', 'Md.Ali', '1989-11-01', 'ENT', '21000', 'JHARKHAND', 'JHARKHAND');
INSERT INTO `paitent_db`.`patient` (`P_ID`, `P_NAME`, `P_DOB`, `P_AILMENT`, `P_BILL`, `P_CONTACT`, `P_ADDRESS`) VALUES ('P005', 'D.Clerk', '2000-09-23', 'HEART', '15000', 'KOLKATA', 'KOLKATA');
INSERT INTO `paitent_db`.`patient` (`P_ID`, `P_NAME`, `P_DOB`, `P_AILMENT`, `P_BILL`, `P_CONTACT`, `P_ADDRESS`) VALUES ('P006', 'K.reddy', '1998-02-17', 'LUNG', '24500', 'SILIGURI', 'ASSAM');
INSERT INTO `paitent_db`.`patient` (`P_ID`, `P_NAME`, `P_DOB`, `P_AILMENT`, `P_BILL`, `P_CONTACT`, `P_ADDRESS`) VALUES ('P007', 'T.Ghosh', '1995-05-19', 'HEART', '19900', 'KOLKATA', 'KOLKATA');
INSERT INTO `paitent_db`.`patient` (`P_ID`, `P_NAME`, `P_DOB`, `P_AILMENT`, `P_BILL`, `P_CONTACT`, `P_ADDRESS`) VALUES ('P008', 'M.Sekh', '1976-04-23', 'ENT', '12000', 'PATNA', 'BIHAR');
INSERT INTO `paitent_db`.`patient` (`P_ID`, `P_NAME`, `P_DOB`, `P_AILMENT`, `P_BILL`, `P_CONTACT`, `P_ADDRESS`) VALUES ('P009', 'L.Paul', '1987-11-22', 'LUNG', '23000', 'SILIGURI', 'ASSAM');
INSERT INTO `paitent_db`.`patient` (`P_ID`, `P_NAME`, `P_DOB`, `P_AILMENT`, `P_BILL`, `P_CONTACT`, `P_ADDRESS`) VALUES ('P010', 'G.Giri', '1992-08-30', 'HEART', '27000', 'DURGAPUR', 'DURGAPUR');
INSERT INTO `paitent_db`.`patient` (`P_ID`, `P_NAME`, `P_DOB`, `P_AILMENT`, `P_BILL`, `P_CONTACT`, `P_ADDRESS`) VALUES ('P011', 'N.Koley', '2002-05-25', 'ENT', '18000', 'ASANSOL', 'ASANSOL');

-- 2. Display all the patients who are above 60 years of age.
SELECT * FROM `paitent_db`.`patient` 
WHERE `P_DOB` <= DATE_SUB(CURDATE(), INTERVAL 60 YEAR);
-- 3. Find all the patients who have heart ailment and are from Kolkata. 
SELECT `P_NAME` FROM `paitent_db`.`patient` WHERE `P_AILMENT` = "HEART" AND `P_ADDR` = "KOLKATA";
-- 4. Find all the patients who have a bill greater than 20000 and are not from Kolkata.
SELECT `P_ID`,`P_NAME`,`P_BILL` FROM `paitent_db`.`patient` WHERE `P_BILL` > 20000 AND `P_ADDR` <> "KOLKATA";
-- 5. Find all the patients who were born between 1980 and 1990.
SELECT `P_NAME` FROM `paitent_db`.`patient` WHERE `P_DOB` BETWEEN '1980/01/01' AND '1990/12/31';
--OR
SELECT `P_NAME` FROM `paitent_db`.`patient` WHERE `P_DOB` > '1979/12/31' AND `P_DOB` <'1991/01/01';
--6. Find all the patients who have a contact person in Kolkata. 
SELECT `P_NAME` FROM `paitent_db`.`patient` WHERE `P_CONTACT` = 'KOLKATA';

