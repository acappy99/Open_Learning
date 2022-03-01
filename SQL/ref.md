# Beginner work

## IN
The hard way:
```
SELECT * FROM [table] WHERE [column_name] = 'value1' [column_name] = 'value2' [column_name] = 'value3';
```
The easy way:
```
SELECT * FROM [table] WHERE [column_name] IN ('value1','value2','value3);
```

## BETWEEN
Select data from a range:
```
SELECT * FROM [table_name] WHERE [column_name] BETWEEN [DATA_FUNCTION] 'value1' AND 'value2'
# not sure if data function is necessary
```

## LIKE and ILIKE
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

## ILIKE
not case sensitive; would return 'apple' or 'Apple'
```
SELECT * FROM [table_name] WHERE [column_name] ILIKE 'a%'
```

## GROUP BY
counting number of rows with same country
```
SELECT country_, COUNT(*) FROM person GROUP BY country_
```

## HAVING





