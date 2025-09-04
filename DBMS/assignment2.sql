CREATE SCHEMA `ass2` ;

--Supplier Table
CREATE TABLE `ass2`.`supplier_table` (
  `SID` VARCHAR(45) NOT NULL,
  `SNAME` VARCHAR(45) NOT NULL,
  `CITY` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`SID`));



--Item Table
CREATE TABLE `ass2`.`item_table` (
  `ITEM_ID` VARCHAR(45) NOT NULL,
  `INAME` VARCHAR(45) NOT NULL,
  `COLOR` VARCHAR(45) NOT NULL,
  `WEIGHT` INT NOT NULL,
  PRIMARY KEY (`ITEM_ID`));

--supply Table
CREATE TABLE `ass2`.`supply_table` (
  `SID` VARCHAR(45) NOT NULL,
  `ITEM_ID` VARCHAR(45) NOT NULL,
  `QUANTITY` INT NOT NULL,
  PRIMARY KEY (`SID`, `ITEM_ID`));


--Supplier Table Data
  
INSERT INTO `ass2`.`supplier_table` (`SID`, `SNAME`, `CITY`) VALUES ('S001', 'Manish', 'Kolkata');

INSERT INTO `ass2`.`supplier_table` (`SID`, `SNAME`, `CITY`) VALUES ('S002', 'Hari', 'Delhi');

INSERT INTO `ass2`.`supplier_table` (`SID`, `SNAME`, `CITY`) VALUES ('S003', 'Kundan', 'Kolkata');

INSERT INTO `ass2`.`supplier_table` (`SID`, `SNAME`, `CITY`) VALUES ('S004', 'Sagar', 'Patna');

INSERT INTO `ass2`.`supplier_table` (`SID`, `SNAME`, `CITY`) VALUES ('S005', 'Zahir', 'Delhi');

--Item Table Data

INSERT INTO `ass2`.`item_table` (`ITEM_ID`, `INAME`, `COLOR`, `WEIGHT`) VALUES ('ITEM1', 'Desk', 'Brown', 20);

INSERT INTO `ass2`.`item_table` (`ITEM_ID`, `INAME`, `COLOR`, `WEIGHT`) VALUES ('ITEM2', 'Chair', 'Red', 7);

INSERT INTO `ass2`.`item_table` (`ITEM_ID`, `INAME`, `COLOR`, `WEIGHT`) VALUES ('ITEM3', 'Board-1', 'Blue', 15);

INSERT INTO `ass2`.`item_table` (`ITEM_ID`, `INAME`, `COLOR`, `WEIGHT`) VALUES ('ITEM4', 'Board-2', 'White', 10);

INSERT INTO `ass2`.`item_table` (`ITEM_ID`, `INAME`, `COLOR`, `WEIGHT`) VALUES ('ITEM5', 'Marker', 'Black', 20);

--Supply Table Data

INSERT INTO `ass2`.`supply_table` (`SID`, `ITEM_ID`, `QUANTITY`) VALUES ('S002', 'ITEM2', 210);

INSERT INTO `ass2`.`supply_table` (`SID`, `ITEM_ID`, `QUANTITY`) VALUES ('S001', 'ITEM5', 200);

INSERT INTO `ass2`.`supply_table` (`SID`, `ITEM_ID`, `QUANTITY`) VALUES ('S005', 'ITEM1', 125);

INSERT INTO `ass2`.`supply_table` (`SID`, `ITEM_ID`, `QUANTITY`) VALUES ('S002', 'ITEM5', 500);

INSERT INTO `ass2`.`supply_table` (`SID`, `ITEM_ID`, `QUANTITY`) VALUES ('S005', 'ITEM2', 156);

INSERT INTO `ass2`.`supply_table` (`SID`, `ITEM_ID`, `QUANTITY`) VALUES ('S001', 'ITEM1', 370);


-- List the names of all suppliers
SELECT `SNAME` FROM `ass2`.`supplier_table`;

--Find all the items which are sold by at least one supplier.
SELECT DISTINCT it.INAME FROM `ass2`.`supply_table` st JOIN `ass2`.`item_table` it ON st.ITEM_ID = it.ITEM_ID;

--Find all the suppliers who live in Delhi.
SELECT SID, SNAME FROM `ass2`.`supplier_table` WHERE CITY = 'Delhi';

--Find all the suppliers who do not live in Kolkata.
SELECT SID, SNAME FROM `ass2`.`supplier_table` WHERE CITY <> 'Kolkata';

--Find all the suppliers who do not sell any item. 
SELECT s.SNAME FROM `ass2`.`supplier_table` s LEFT JOIN `ass2`.`supply_table` sp ON s.SID = sp.SID WHERE sp.SID IS NULL;