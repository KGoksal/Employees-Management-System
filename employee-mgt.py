from employees import Employee, CommissionPaid, HourlyPaid

def total_pay(employee_list):
    # Calculates the total weekly pay for a list of employees.
    total = 0.0
    for emp in employee_list:
        total += emp.pay()
    return total

def print_employee_list(employee_list):
    # Prints a formatted list of employee information.
    print("Employee Type\tEmployee Name\tDepartment\tWeekly Pay")
    print("---------------\t-------------\t----------\t----------")
    for emp in employee_list:
        print(f"{emp}")

def main():
    # Main function to demonstrate usage of Employee subclasses and calculate total pay.
    # Create CommissionPaid objects
    commission_emp1 = CommissionPaid("Fname1 Lname1", "Marketing", 500, 30000)
    commission_emp2 = CommissionPaid("Fname2 Lname2", "Sales", 1000, 8000)
    
    # Create HourlyPaid objects
    hourly_emp1 = HourlyPaid("Fname3 Lname3", "Accounting", 20.5, 55.0)
    hourly_emp2 = HourlyPaid("Fname4 Lname4", "Finance", 30, 35.0)
    
    # Create a list of Employee objects
    employees = [commission_emp1, commission_emp2, hourly_emp1, hourly_emp2]
    
    # Calculate total weekly pay
    total = total_pay(employees)
    
    # Print employee information
    print_employee_list(employees)
    
    # Print total weekly pay
    print(f"\nTotal Weekly Pay: ${total:,.2f}")

if __name__ == "__main__":
    main()

# Overall:
#This file serves as the main program to demonstrate the functionality of the Employee subclasses defined in employees.py.
# It creates instances of CommissionPaid and HourlyPaid employees, calculates their weekly pay using defined methods, and displays their information.
# Key functions include total_pay() to compute overall payroll and print_employee_list() to format and display employee details.
