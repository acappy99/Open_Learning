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
If you don't specify a column name, postgres will default to the function name or question marks

### ALIAS
```
SELECT [column_name] AS [new_column_name] FROM [table_name];
```
## NULL
### COALESCE
```
SELECT COALESCE([column_name], '[value if null]') FROM [table_name];
```

### NULLIF
How to tackle division by zero; takes two arguments and returns the first argument if the first is not equal to the second
```
test=# SELECT 10/0;
ERROR:  division by zero
```
```
test=# SELECT 10/NULLIF(2,0);
 ?column?
----------
        5
```
```
test=# SELECT 10/NULLIF(0,0);
 ?column?
----------

```
```
test=# SELECT COALESCE(10/NULLIF(0,0),0);
 coalesce
----------
        0
```



## Timestamps and Dates
### NOW()
```
SELECT NOW();
```
```
test=# SELECT NOW()::DATE;
    now
------------
 2022-03-05
```
```
test=# SELECT NOW()::TIME;
      now
----------------
 12:13:37.26244
```

### Adding and Subtracting Dates
Returning timestamp examples
```
SELECT NOW() + INTERVAL '10 YEARS';
SELECT NOW() - INTERVAL '1 DAY';
SELECT NOW() - INTERVAL '2 MONTHS';
```
Return date instead of timestamp
```
SELECT (NOW() + INTERVAL '1 YEAR')::DATE;
```

### Extracting fields from timestamp
Month, Day, Day of Week, Century -- respectively
```
SELECT EXTRACT(MONTH FROM NOW());
SELECT EXTRACT(DAY FROM NOW());
SELECT EXTRACT(DOW FROM NOW());
SELECT EXTRACT(CENTURY FROM NOW());
```

### Age function
```
SELECT [name], [date_of_birth], AGE(NOW(), [date_of_birth]) AS [new_col_name] FROM [table_name];
```


## Primary keys
Uniquely identify a record in tables, i.e. a passport number

### Drop primary key
i.e. dropping primary key
```
ALTER TABLE [table_name] DROP CONSTRAINT [table_name]_key;
```
### Add primary key
Every row must be unique in the primary key column
```
ALTER TABLE [table_name] ADD PRIMARY KEY([column_name])
```


## Unique constraint
### Add unique constraint
You name the constraint
```
ALTER TABLE [table_name] ADD CONSTRAINT [constraint_name] UNIQUE ([column_name]);
```
Let postgreSQL name the constraint
```
ALTER TABLE [table_name] ADD UNIQUE ([column_name]);
```

### Drop constraint
```
ALTER TABLE [table_name] DROP CONSTRAINT [constraint_name];
```


## Check constraint
Can use AND/OR in the CHECK function
```
ALTER TABLE [table_name] ADD CONSTRAINT [constraint_name] CHECK ([column_name] = 'value')
```


## Update/Delete records
