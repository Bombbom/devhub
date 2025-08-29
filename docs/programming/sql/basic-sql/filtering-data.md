# How to Filter Data in SQL Queries

Data filtering is one of the most fundamental and powerful features in SQL. The `WHERE` clause allows you to specify conditions that determine which rows are returned by your query. This comprehensive guide covers all aspects of filtering data in SQL queries.

## Table of Contents

- [Basic WHERE Clause](#basic-where-clause)
- [Comparison Operators](#comparison-operators)
- [Logical Operators](#logical-operators)
- [Pattern Matching with LIKE](#pattern-matching-with-like)
- [Range Filtering](#range-filtering)
- [List Filtering](#list-filtering)
- [NULL Value Handling](#null-value-handling)
- [Date and Time Filtering](#date-and-time-filtering)
- [Advanced Filtering Techniques](#advanced-filtering-techniques)
- [Performance Considerations](#performance-considerations)

## Basic WHERE Clause

The `WHERE` clause filters rows based on specified conditions. It comes after the `FROM` clause and before `GROUP BY`, `HAVING`, `ORDER BY`, and `LIMIT`.

### Basic Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### Simple Examples

```sql
-- Sample table structure for examples
-- employees: id, first_name, last_name, department, salary, hire_date, age, email

-- Filter by exact match
SELECT first_name, last_name, salary
FROM employees
WHERE department = 'Marketing';

-- Filter by numeric condition
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 50000;

-- Filter by date
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date >= '2020-01-01';
```

## Comparison Operators

SQL provides various comparison operators for filtering data:

| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Equal to | `salary = 50000` |
| `<>` or `!=` | Not equal to | `department <> 'HR'` |
| `>` | Greater than | `age > 30` |
| `<` | Less than | `salary < 40000` |
| `>=` | Greater than or equal | `age >= 25` |
| `<=` | Less than or equal | `salary <= 60000` |

### Comparison Examples

```sql
-- Equal to
SELECT * FROM employees WHERE department = 'Sales';

-- Not equal to (two ways)
SELECT * FROM employees WHERE department <> 'HR';
SELECT * FROM employees WHERE department != 'HR';

-- Greater than
SELECT first_name, last_name, age
FROM employees
WHERE age > 35;

-- Less than or equal to
SELECT first_name, last_name, salary
FROM employees
WHERE salary <= 45000;

-- Combining comparisons with different data types
SELECT first_name, last_name, salary, hire_date
FROM employees
WHERE salary >= 50000 AND hire_date >= '2021-01-01';
```

## Logical Operators

Combine multiple conditions using logical operators:

### AND Operator

All conditions must be true:

```sql
-- Both conditions must be true
SELECT first_name, last_name, department, salary
FROM employees
WHERE department = 'Engineering' AND salary > 70000;

-- Multiple AND conditions
SELECT first_name, last_name, age, department, salary
FROM employees
WHERE age >= 25 
  AND age <= 40 
  AND department = 'Marketing' 
  AND salary > 45000;
```

### OR Operator

At least one condition must be true:

```sql
-- Either condition can be true
SELECT first_name, last_name, department
FROM employees
WHERE department = 'Sales' OR department = 'Marketing';

-- Multiple OR conditions
SELECT first_name, last_name, department, salary
FROM employees
WHERE salary < 30000 
   OR salary > 80000 
   OR department = 'Executive';
```

### NOT Operator

Negates a condition:

```sql
-- NOT with equality
SELECT first_name, last_name, department
FROM employees
WHERE NOT department = 'HR';

-- NOT with other operators
SELECT first_name, last_name, salary
FROM employees
WHERE NOT salary > 60000;  -- Same as salary <= 60000

-- NOT with complex conditions
SELECT first_name, last_name, department, age
FROM employees
WHERE NOT (age < 25 OR department = 'Intern');
```

### Combining Logical Operators

Use parentheses to control precedence:

```sql
-- Without parentheses - AND has higher precedence
SELECT first_name, last_name, department, salary
FROM employees
WHERE department = 'Sales' OR department = 'Marketing' AND salary > 50000;
-- This means: Sales department OR (Marketing department AND salary > 50000)

-- With parentheses - clearer intention
SELECT first_name, last_name, department, salary
FROM employees
WHERE (department = 'Sales' OR department = 'Marketing') AND salary > 50000;
-- This means: (Sales OR Marketing) AND salary > 50000

-- Complex example
SELECT first_name, last_name, department, salary, age
FROM employees
WHERE (department = 'Engineering' AND salary > 70000)
   OR (department = 'Sales' AND age < 30)
   OR (department = 'Executive');
```

## Pattern Matching with LIKE

The `LIKE` operator enables pattern matching with wildcards:

- `%` - Matches zero or more characters
- `_` - Matches exactly one character

### LIKE Examples

```sql
-- Starts with 'John'
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE 'John%';

-- Ends with 'son'
SELECT first_name, last_name
FROM employees
WHERE last_name LIKE '%son';

-- Contains 'tech'
SELECT first_name, last_name, email
FROM employees
WHERE email LIKE '%tech%';

-- Second character is 'a'
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE '_a%';

-- Exactly 5 characters
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE '_____';

-- Complex patterns
SELECT first_name, last_name, email
FROM employees
WHERE email LIKE '%@company.com' 
  AND first_name LIKE 'J%';
```

### NOT LIKE

```sql
-- Does not start with 'A'
SELECT first_name, last_name
FROM employees
WHERE first_name NOT LIKE 'A%';

-- Does not contain 'temp'
SELECT first_name, last_name, email
FROM employees
WHERE email NOT LIKE '%temp%';
```

### Case Sensitivity

!!! note "Database Specific Behavior"
    LIKE behavior varies by database system:
    - MySQL: Case-insensitive by default (depends on collation)
    - PostgreSQL: Case-sensitive by default, use ILIKE for case-insensitive
    - SQL Server: Depends on collation settings

```sql
-- PostgreSQL case-insensitive pattern matching
SELECT first_name, last_name
FROM employees
WHERE first_name ILIKE 'john%';

-- Force case-insensitive in other databases
SELECT first_name, last_name
FROM employees
WHERE UPPER(first_name) LIKE UPPER('john%');
```

## Range Filtering

### BETWEEN Operator

Filters values within a specified range (inclusive):

```sql
-- Numeric range
SELECT first_name, last_name, salary
FROM employees
WHERE salary BETWEEN 40000 AND 60000;

-- Age range
SELECT first_name, last_name, age
FROM employees
WHERE age BETWEEN 25 AND 35;

-- Date range
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date BETWEEN '2020-01-01' AND '2022-12-31';

-- NOT BETWEEN
SELECT first_name, last_name, salary
FROM employees
WHERE salary NOT BETWEEN 30000 AND 70000;
```

### Equivalent Range Conditions

```sql
-- BETWEEN is equivalent to >= AND <=
-- These two queries are identical:

SELECT first_name, last_name, salary
FROM employees
WHERE salary BETWEEN 40000 AND 60000;

SELECT first_name, last_name, salary
FROM employees
WHERE salary >= 40000 AND salary <= 60000;
```

## List Filtering

### IN Operator

Matches any value in a specified list:

```sql
-- Department list
SELECT first_name, last_name, department
FROM employees
WHERE department IN ('Sales', 'Marketing', 'Engineering');

-- Numeric list
SELECT first_name, last_name, id
FROM employees
WHERE id IN (1, 5, 10, 15, 20);

-- Mixed data types (same column type)
SELECT first_name, last_name, department
FROM employees
WHERE department IN ('HR', 'Legal', 'Finance');

-- NOT IN
SELECT first_name, last_name, department
FROM employees
WHERE department NOT IN ('Intern', 'Contractor');
```

### IN vs OR

```sql
-- These queries are equivalent:
-- Using IN
SELECT first_name, last_name, department
FROM employees
WHERE department IN ('Sales', 'Marketing', 'Engineering');

-- Using OR
SELECT first_name, last_name, department
FROM employees
WHERE department = 'Sales' 
   OR department = 'Marketing' 
   OR department = 'Engineering';
```

### Subqueries with IN

```sql
-- Find employees in departments with more than 10 people
SELECT first_name, last_name, department
FROM employees
WHERE department IN (
    SELECT department 
    FROM employees 
    GROUP BY department 
    HAVING COUNT(*) > 10
);
```

## NULL Value Handling

NULL values require special handling in SQL:

### IS NULL and IS NOT NULL

```sql
-- Find employees with no phone number
SELECT first_name, last_name, phone
FROM employees
WHERE phone IS NULL;

-- Find employees with phone numbers
SELECT first_name, last_name, phone
FROM employees
WHERE phone IS NOT NULL;

-- Complex NULL handling
SELECT first_name, last_name, phone, email
FROM employees
WHERE phone IS NOT NULL AND email IS NOT NULL;
```

!!! warning "Common NULL Mistakes"
    Never use `= NULL` or `<> NULL`. These will always return false because NULL cannot be compared using standard operators.

```sql
-- WRONG - This will return no results
SELECT * FROM employees WHERE phone = NULL;

-- CORRECT - This will find NULL phone numbers
SELECT * FROM employees WHERE phone IS NULL;
```

### NULL in Calculations

```sql
-- NULL values in conditions
SELECT first_name, last_name, bonus, salary
FROM employees
WHERE bonus IS NULL OR bonus = 0;

-- Using COALESCE to handle NULLs
SELECT first_name, last_name, 
       COALESCE(bonus, 0) as bonus_amount
FROM employees
WHERE COALESCE(bonus, 0) > 5000;
```

## Date and Time Filtering

### Date Comparisons

```sql
-- Exact date match
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date = '2021-06-15';

-- Date range
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date >= '2020-01-01' AND hire_date < '2021-01-01';

-- Recent hires (last 30 days)
SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date >= CURRENT_DATE - INTERVAL '30 days';  -- PostgreSQL
-- WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);  -- MySQL
-- WHERE hire_date >= DATEADD(day, -30, GETDATE());  -- SQL Server
```

### Date Functions in Filtering

```sql
-- Filter by year
SELECT first_name, last_name, hire_date
FROM employees
WHERE EXTRACT(YEAR FROM hire_date) = 2021;  -- PostgreSQL
-- WHERE YEAR(hire_date) = 2021;  -- MySQL/SQL Server

-- Filter by month
SELECT first_name, last_name, hire_date
FROM employees
WHERE EXTRACT(MONTH FROM hire_date) = 6;  -- PostgreSQL
-- WHERE MONTH(hire_date) = 6;  -- MySQL/SQL Server

-- Filter by day of week
SELECT first_name, last_name, hire_date
FROM employees
WHERE EXTRACT(DOW FROM hire_date) = 1;  -- Monday in PostgreSQL
-- WHERE DAYOFWEEK(hire_date) = 2;  -- Monday in MySQL
```

### Time and Timestamp Filtering

```sql
-- Assuming login_timestamp column exists
-- Filter by specific time range
SELECT user_id, login_timestamp
FROM user_logins
WHERE login_timestamp BETWEEN '2023-12-01 09:00:00' AND '2023-12-01 17:00:00';

-- Filter by time of day (PostgreSQL)
SELECT user_id, login_timestamp
FROM user_logins
WHERE EXTRACT(HOUR FROM login_timestamp) BETWEEN 9 AND 17;

-- Recent activity (last hour)
SELECT user_id, login_timestamp
FROM user_logins
WHERE login_timestamp >= NOW() - INTERVAL '1 hour';  -- PostgreSQL
-- WHERE login_timestamp >= NOW() - INTERVAL 1 HOUR;  -- MySQL
```

## Advanced Filtering Techniques

### Filtering with Aggregate Functions (HAVING)

Use `HAVING` to filter groups after `GROUP BY`:

```sql
-- Find departments with average salary > 60000
SELECT department, AVG(salary) as avg_salary, COUNT(*) as employee_count
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;

-- Departments with more than 5 employees and high average age
SELECT department, AVG(age) as avg_age, COUNT(*) as employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5 AND AVG(age) > 30;
```

### Filtering with Window Functions

```sql
-- Find employees with above-average salary in their department
SELECT first_name, last_name, department, salary,
       AVG(salary) OVER (PARTITION BY department) as dept_avg_salary
FROM employees
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees e2 
    WHERE e2.department = employees.department
);

-- Using window functions with filtering
WITH ranked_employees AS (
    SELECT first_name, last_name, department, salary,
           ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as salary_rank
    FROM employees
)
SELECT first_name, last_name, department, salary
FROM ranked_employees
WHERE salary_rank <= 3;  -- Top 3 earners per department
```

### Regular Expressions

Some databases support regular expression filtering:

```sql
-- PostgreSQL regular expressions
SELECT first_name, last_name, email
FROM employees
WHERE email ~ '^[a-zA-Z0-9]+@company\.(com|org)$';

-- MySQL regular expressions
SELECT first_name, last_name, phone
FROM employees
WHERE phone REGEXP '^[0-9]{3}-[0-9]{3}-[0-9]{4}$';

-- SQL Server (limited regex support, use LIKE with patterns)
SELECT first_name, last_name, phone
FROM employees
WHERE phone LIKE '[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]';
```

### Case-Sensitive Filtering

```sql
-- Force case-sensitive comparison
SELECT first_name, last_name
FROM employees
WHERE BINARY first_name = 'john';  -- MySQL

-- Case-sensitive LIKE
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE BINARY 'John%';  -- MySQL

-- PostgreSQL (default case-sensitive)
SELECT first_name, last_name
FROM employees
WHERE first_name = 'John';
```

## Performance Considerations

### Index Usage

!!! tip "Performance Tips"
    Proper indexing is crucial for query performance, especially with WHERE clauses.

```sql
-- Create indexes on frequently filtered columns
CREATE INDEX idx_department ON employees(department);
CREATE INDEX idx_salary ON employees(salary);
CREATE INDEX idx_hire_date ON employees(hire_date);

-- Composite index for multiple column filtering
CREATE INDEX idx_dept_salary ON employees(department, salary);
```

### Efficient Filtering Practices

```sql
-- GOOD: Use indexed columns in WHERE clause
SELECT first_name, last_name, salary
FROM employees
WHERE department = 'Engineering';  -- Assuming department is indexed

-- AVOID: Functions on indexed columns prevent index usage
SELECT first_name, last_name, salary
FROM employees
WHERE UPPER(department) = 'ENGINEERING';  -- Index on department won't be used

-- BETTER: Store data consistently or use functional index
SELECT first_name, last_name, salary
FROM employees
WHERE department = 'Engineering';  -- Ensure consistent case in data

-- GOOD: Range queries on indexed columns
SELECT first_name, last_name, salary
FROM employees
WHERE salary BETWEEN 50000 AND 70000;

-- AVOID: Negation can prevent index usage
SELECT first_name, last_name, salary
FROM employees
WHERE NOT department = 'HR';

-- BETTER: Use positive conditions when possible
SELECT first_name, last_name, salary
FROM employees
WHERE department IN ('Engineering', 'Sales', 'Marketing');
```

### Filtering with EXISTS vs IN

```sql
-- Using EXISTS (often more efficient for large datasets)
SELECT e1.first_name, e1.last_name, e1.department
FROM employees e1
WHERE EXISTS (
    SELECT 1 
    FROM departments d 
    WHERE d.name = e1.department AND d.budget > 100000
);

-- Using IN (good for smaller result sets)
SELECT e1.first_name, e1.last_name, e1.department
FROM employees e1
WHERE e1.department IN (
    SELECT d.name 
    FROM departments d 
    WHERE d.budget > 100000
);
```

## Real-World Examples

### E-commerce Order Filtering

```sql
-- Sample orders table structure
-- orders: order_id, customer_id, order_date, total_amount, status, shipping_country

-- Find recent high-value orders
SELECT order_id, customer_id, order_date, total_amount
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
  AND total_amount > 500
  AND status = 'completed';

-- Find orders requiring attention
SELECT order_id, customer_id, order_date, status
FROM orders
WHERE (status = 'pending' AND order_date < CURRENT_DATE - INTERVAL '7 days')
   OR (status = 'processing' AND order_date < CURRENT_DATE - INTERVAL '3 days')
   OR status = 'failed';

-- International orders with specific criteria
SELECT order_id, customer_id, shipping_country, total_amount
FROM orders
WHERE shipping_country NOT IN ('USA', 'Canada')
  AND total_amount BETWEEN 100 AND 1000
  AND status = 'completed'
  AND order_date >= '2023-01-01';
```

### User Activity Analysis

```sql
-- Sample user_sessions table
-- user_sessions: session_id, user_id, login_time, logout_time, ip_address, device_type

-- Find suspicious login patterns
SELECT user_id, login_time, ip_address, device_type
FROM user_sessions
WHERE login_time >= CURRENT_DATE - INTERVAL '24 hours'
  AND user_id IN (
      SELECT user_id 
      FROM user_sessions 
      WHERE login_time >= CURRENT_DATE - INTERVAL '24 hours'
      GROUP BY user_id 
      HAVING COUNT(DISTINCT ip_address) > 5
  );

-- Active users on mobile devices
SELECT user_id, COUNT(*) as session_count, 
       MIN(login_time) as first_login,
       MAX(login_time) as last_login
FROM user_sessions
WHERE login_time >= CURRENT_DATE - INTERVAL '7 days'
  AND device_type LIKE '%mobile%'
  AND logout_time IS NOT NULL  -- Completed sessions only
GROUP BY user_id
HAVING COUNT(*) >= 3;
```

### Inventory Management

```sql
-- Sample products table
-- products: product_id, name, category, price, stock_quantity, reorder_level, last_updated

-- Low stock alerts
SELECT product_id, name, category, stock_quantity, reorder_level
FROM products
WHERE stock_quantity <= reorder_level
  AND stock_quantity > 0  -- Not completely out of stock
  AND category NOT IN ('discontinued', 'seasonal')
ORDER BY (reorder_level - stock_quantity) DESC;

-- Price analysis
SELECT category, 
       COUNT(*) as product_count,
       AVG(price) as avg_price,
       MIN(price) as min_price,
       MAX(price) as max_price
FROM products
WHERE stock_quantity > 0  -- In stock only
  AND last_updated >= CURRENT_DATE - INTERVAL '90 days'
  AND price BETWEEN 10 AND 1000  -- Reasonable price range
GROUP BY category
HAVING COUNT(*) >= 5  -- Categories with at least 5 products
ORDER BY avg_price DESC;
```

## Summary

Data filtering with the WHERE clause is essential for extracting meaningful information from databases. Key takeaways:

1. **Use appropriate operators** for different data types and conditions
2. **Combine conditions logically** with AND, OR, and NOT operators
3. **Handle NULL values** explicitly with IS NULL and IS NOT NULL
4. **Leverage pattern matching** with LIKE for flexible text searches
5. **Use range and list filtering** for efficient multi-value conditions
6. **Consider performance implications** when designing filters
7. **Test complex conditions** thoroughly with representative data

!!! note "Best Practices"
    - Always test filters with sample data first
    - Use parentheses to clarify complex logical conditions
    - Consider indexing frequently filtered columns
    - Be mindful of case sensitivity requirements
    - Handle NULL values appropriately in your logic
    - Document complex filtering logic with comments

Master these filtering techniques to write more efficient and precise SQL queries that return exactly the data you need.