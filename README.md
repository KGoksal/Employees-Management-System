# Employees-Management-System

This Python module (`employees.py`) defines classes to manage different types of employees within a company. It includes basic employee details and behaviors, as well as specific implementations for commission-paid and hourly-paid employees.

## Classes

### 1. Employee

Represents a basic employee with attributes for name and department. This class includes methods to retrieve and update these attributes.

**Methods:**
- `get_name()`: Retrieves the employee's name.
- `set_name(name)`: Sets the employee's name.
- `get_department()`: Retrieves the employee's department.
- `set_department(department)`: Sets the employee's department.
- `pay()`: Returns the base pay for the employee.

### 2. CommissionPaid

Inherits from `Employee` and represents an employee who receives a base rate plus commission based on sales.

**Additional Attributes:**
- `base_rate`: Base rate of pay.
- `sales`: Sales amount for commission calculation.

**Methods:**
- `get_base_rate()`
- `set_base_rate(base_rate)`
- `get_sales()`
- `set_sales(sales)`
- `pay()`: Calculates and returns the weekly pay, including commission, based on predefined commission rates.

### 3. HourlyPaid

Inherits from `Employee` and represents an employee who is paid based on an hourly rate and hours worked, including overtime.

**Additional Attributes:**
- `hourly_rate`: Hourly rate of pay.
- `hours`: Hours worked by the employee.

**Methods:**
- `get_hourly_rate()`
- `set_hourly_rate(hourly_rate)`
- `get_hours()`
- `set_hours(hours)`
- `pay()`: Calculates and returns the weekly pay, considering regular hours and overtime hours (if applicable).

## Usage

To use these classes, you can create instances of `Employee`, `CommissionPaid`, or `HourlyPaid` by initializing them with relevant details. Here's a simple example:

```python
# Example usage
from employees import Employee, CommissionPaid, HourlyPaid

# Create an instance of an employee
emp1 = Employee("John Doe", "Sales")

# Create an instance of a commission-paid employee
emp2 = CommissionPaid("Jane Smith", "Marketing", 1000.0, 15000)

# Create an instance of an hourly-paid employee
emp3 = HourlyPaid("Michael Brown", "Operations", 25.0, 45)

# Display information about the employees
print(emp1)
print(emp2)
print(emp3)
```

In this example:
- `emp1` is a basic employee with default pay.
- `emp2` is a commission-paid employee with a base rate and sales amount.
- `emp3` is an hourly-paid employee with an hourly rate and hours worked.

Each class provides its own `__str__()` method for a formatted string representation, displaying relevant details including weekly pay where applicable.
