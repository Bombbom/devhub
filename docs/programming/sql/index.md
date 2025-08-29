# SQL Basic SELECT Statement

This guide covers the fundamental concepts of SQL SELECT statements, from basic queries to advanced filtering and ordering techniques.

## Basic SELECT Statement

To read data from a table, you use the `SELECT` statement. The most basic form retrieves all columns from a table:

```sql
SELECT * FROM customers;
```

The `SELECT` statement is the foundation of data retrieval in SQL and allows you to specify exactly what data you want to extract from your database.

## Case Sensitivity

The SQL language is case insensitive, meaning that you can write statements in upper or lower case. All of the following are equivalent:

```sql
-- Lowercase
select * from customers;

-- Uppercase  
SELECT * FROM CUSTOMERS;

-- Mixed case
Select * From customers;
```

!!! note "Best Practice"
    While SQL is case insensitive, it's common practice to write SQL keywords in uppercase (SELECT, FROM, WHERE) and table/column names in lowercase for better readability.

## Spacing and Formatting

SQL is flexible with whitespace. These statements are functionally identical:

```sql
-- Compact format
SELECT id,name FROM customers;

-- Formatted for readability
SELECT 
    id,
    name 
FROM customers;

-- Extra spacing
SELECT     id    ,    name     FROM     customers    ;
```

## Clause Ordering

SQL statements must follow a specific order of clauses:

1. `SELECT` - specify columns
2. `FROM` - specify table(s)
3. `WHERE` - filter rows
4. `GROUP BY` - group rows
5. `HAVING` - filter groups
6. `ORDER BY` - sort results
7. `LIMIT` - limit number of results

!!! info "Historical Note"
    The original proposed name for SQL was SEQUEL (Structured English Query Language), which explains why SQL reads like structured English.

## Semicolon (;)

The semicolon marks the end of a SQL statement:

```sql
SELECT * FROM customers;
```

While optional in many database systems for single statements, it's required when executing multiple statements and is considered best practice to always include it.

## Selecting Specific Columns

Instead of using `SELECT *`, you can specify individual columns:

```sql
SELECT id, givenname, familyname FROM customers;
```

### Benefits of Specific Column Selection

- **Performance**: Reduces data transfer and memory usage
- **Clarity**: Makes your intent explicit
- **Maintenance**: Easier to understand and modify
- **Security**: Reduces exposure of sensitive data

## Column Order

The order of columns in your `SELECT` statement determines their order in the result set:

```sql
-- This order
SELECT familyname, givenname, id FROM customers;

-- Will display: familyname | givenname | id
```

## Layout and Formatting

For better readability, especially with many columns, use formatting:

```sql
SELECT 
    id,
    givenname,
    familyname,
    email,
    phone,
    address
FROM customers;
```

## Using SELECT *

!!! warning "Best Practice Warning"
    It is considered bad practice to use `SELECT *` in production code, even if you want all columns. Always specify columns explicitly.

**Problems with SELECT ***:

- **Performance**: May retrieve unnecessary data
- **Breaking changes**: New columns can break applications
- **Security**: May expose sensitive data
- **Clarity**: Unclear what data is being used

**Instead of:**
```sql
SELECT * FROM customers;
```

**Use:**
```sql
SELECT 
    id,
    givenname,
    familyname,
    email,
    phone
FROM customers;
```

## Calculated Columns

You can perform calculations and create new columns in your results:

```sql
SELECT 
    id,
    givenname,
    familyname,
    height,
    height * 2.54 AS height_cm,
    weight / 2.205 AS weight_kg
FROM customers;
```

### Common Calculations

```sql
SELECT 
    product_name,
    price,
    quantity,
    price * quantity AS total_value,
    price * 1.1 AS price_with_tax
FROM order_items;
```

## Aliases

Aliases provide alternative names for columns or tables, making results more readable:

### Column Aliases

```sql
SELECT 
    givenname AS first_name,
    familyname AS last_name,
    height/2.54 AS height_inches
FROM customers;
```

### Table Aliases

```sql
SELECT 
    c.givenname,
    c.familyname
FROM customers AS c;
-- or simply
FROM customers c;
```

## Comments

SQL supports two types of comments for documenting your code.

### Single Line Comments

Use `--` for single line comments:

```sql
SELECT 
    id,
    givenname,        -- Customer's first name
    familyname,       -- Customer's last name
    height/2.54 AS inches  -- Convert cm to inches (1in = 2.54cm)
FROM customers;       -- Main customer table
```

### Block Comments

Use `/* */` for multi-line comments:

```sql
/*
This query retrieves customer information
with height converted from centimeters to inches
Author: Database Team
Date: 2024-01-15
*/
SELECT 
    id,
    givenname,
    familyname,
    height/2.54 AS inches
FROM customers;
```

## Filtering Rows

Use the `WHERE` clause to filter rows based on conditions:

```sql
SELECT 
    id,
    givenname,
    familyname
FROM customers
WHERE age >= 18;
```

### Common Filter Operations

```sql
-- Equality
SELECT * FROM customers WHERE country = 'USA';

-- Comparison operators
SELECT * FROM customers WHERE age > 21;
SELECT * FROM customers WHERE salary <= 50000;

-- Multiple conditions
SELECT * FROM customers WHERE age >= 18 AND country = 'USA';
SELECT * FROM customers WHERE status = 'active' OR status = 'pending';

-- Pattern matching
SELECT * FROM customers WHERE givenname LIKE 'John%';

-- Range checking
SELECT * FROM customers WHERE age BETWEEN 18 AND 65;

-- List membership
SELECT * FROM customers WHERE country IN ('USA', 'Canada', 'Mexico');
```

## Ordering the Results

Use `ORDER BY` to sort your results:

```sql
SELECT 
    id,
    givenname,
    familyname
FROM customers
ORDER BY familyname;
```

### Sorting Options

```sql
-- Ascending order (default)
SELECT * FROM customers ORDER BY age ASC;

-- Descending order
SELECT * FROM customers ORDER BY age DESC;

-- Multiple columns
SELECT * FROM customers 
ORDER BY familyname ASC, givenname ASC;

-- Mixed sorting
SELECT * FROM customers 
ORDER BY country ASC, age DESC;
```

## Distinct Rows

Use `DISTINCT` to eliminate duplicate rows from your results:

```sql
SELECT DISTINCT country FROM customers;
```

### DISTINCT with Multiple Columns

```sql
-- Returns unique combinations of country and state
SELECT DISTINCT country, state FROM customers;
```

### COUNT with DISTINCT

```sql
-- Count unique countries
SELECT COUNT(DISTINCT country) AS unique_countries FROM customers;
```

## Complete Example

Here's a comprehensive example combining multiple concepts:

```sql
/*
Query to get customer information with calculated fields
Filters for adult customers in specific countries
Orders by last name, then first name
*/
SELECT DISTINCT
    c.id,
    c.givenname AS first_name,
    c.familyname AS last_name,
    c.age,
    c.height/2.54 AS height_inches,    -- Convert to inches
    c.weight/2.205 AS weight_pounds,   -- Convert to pounds
    c.country
FROM customers AS c
WHERE 
    c.age >= 18                        -- Adults only
    AND c.country IN ('USA', 'Canada', 'UK')
    AND c.status = 'active'
ORDER BY 
    c.familyname ASC,
    c.givenname ASC;
```

!!! tip "Learning Path"
    Master these basic SELECT concepts before moving on to more advanced topics like JOINs, subqueries, and window functions. Practice with different combinations of clauses to build your confidence.

## Summary

The SELECT statement is your primary tool for data retrieval in SQL. Key points to remember:

- Always specify columns instead of using `SELECT *`
- Use meaningful aliases for clarity
- Comment your code for maintainability
- Follow consistent formatting and clause ordering
- Use filtering and sorting to get exactly the data you need
- Eliminate duplicates with DISTINCT when appropriate