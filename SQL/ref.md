# Reference

## Creating database
### Creating and destroying a database
```
CREATE DATABASE [name];
DROP DATABASE [name];
```

### Connecting to a database
```
psql -h localhost -p 5432 alexcappadona [database_name]
\c [database_name]
```


## Creating tables
```
CREATE TABLE [table name](
	[column_name1] [data_type] [constraints if any]
  [column_name2] [data_type] [constraints if any]
  ...
);
```


## Inserting & Querying Data

### Inserting data
```
INSERT INTO [table name](col1_, col2_,...,coln_)
VALUES(val of col1_, val of col2,...);
```

### Retrieving data
select all from table
```
SELECT * FROM [table_name];
```
select column name(s) from table
```
SELECT [column_name] FROM [table_name]
```

### Inserting from file
```
\i /User/path/file.sql;
```

### Sorting data
order by, default to ASC (optional DESC)
```
SELECT * FROM [table_name] ORDER BY [column] DESC
```

### Distinct keyword
removes duplicates
```
SELECT DISTINCT [column_name] FROM [table_name];
```


## Filtering Data

### WHERE clause & AND
```
SELECT * FROM [table_name] WHERE [column_name] = 'condition';
```
Selecting multiple
```
SELECT * FROM [table_name] WHERE [column_1] = 'condition' AND ([column_2] = 'condition2' OR [column_2] = 'condition2';
```

### Comparison operators
```
=
<
>
<=
>=
<>
```

### Limit, Offset, & FETCH
```

SELECT * FROM [table_name] LIMIT 10
---
OFFSET
---
FETCH FIRST 10 ROWS
```

### IN
The hard way:
```
SELECT * FROM [table] WHERE [column_name] = 'value1' [column_name] = 'value2' [column_name] = 'value3';
```
The easy way:
```
SELECT * FROM [table] WHERE [column_name] IN ('value1','value2','value3);
```

### BETWEEN
Select data from a range:
```
SELECT * FROM [table_name] WHERE [column_name] BETWEEN [DATA_FUNCTION] 'value1' AND 'value2'
# not sure if data function is necessary
```

### LIKE
Sorting for patterns, example emails ending in .com
would find any emails with .com
```
SELECT * FROM [table_name] WHERE email LIKE '%.com';
# any character (%) followed by the pattern you are looking for
```
would find any google email regardless of what comes before 'g' or after '.'
```
SELECT * FROM [table_name] WHERE email LIKE '%google.%';
# wildcard before and after
```
looking for certain number of characters; would return something like 'xxxxxxxx@mail.com' (character for each underscore)
```
SELECT * FROM [table_name] WHERE email LIKE '________@%';
```

### ILIKE
not case sensitive; would return 'apple' or 'Apple'
```
SELECT * FROM [table_name] WHERE [column_name] ILIKE 'a%'
```


## Grouping Data
### GROUP BY
counting number of rows with same country
```
SELECT country_, COUNT(*) FROM person GROUP BY country_
```

### HAVING
shows how many rows are in each country, only showing those with 10 or more, ordered by the number of countries in descending order
```
SELECT country_, COUNT(*) FROM person GROUP BY country_ HAVING COUNT(*) >= 10 ORDER BY COUNT(*) DESC;
```


## Basic Math Operations
### SUM, MAX, MIN, AVG
```
SELECT MAX([column_name]) FROM [table_name];
```
Find average for groups
```
SELECT [column_1], AVERAGE([column_2]) FROM [table_name] GROUP BY [column_1];
```

### Basic Arithmetic Operations
```
+ - * ^ / % !
```
Adding new row with calculation
```
SELECT id, make, model, price, price*.10, ROUND(price - (price*.10),2) FROM car;
```

### ROUND
```
SELECT ROUND([column_1],[# of decimals]) FROM [table_name];
```


## ALIAS
