# pylint:disable=C0111,C0103
import sqlite3
def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = '''
    SELECT OrderID, Customers.ContactName, Employees.FirstName
FROM Orders
JOIN Customers
ON Orders.CustomerID = Customers.CustomerID
JOIN Employees
ON Orders.EmployeeID = Employees.EmployeeID
ORDER BY OrderID
    '''
    db.execute(query)
    results = db.fetchall()
    return results

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query = '''
    SELECT Customers.ContactName ,ROUND(SUM(UnitPrice*Quantity),2) as total
    FROM OrderDetails
    JOIN Orders
    ON OrderDetails.OrderID = Orders.OrderID
    JOIN Customers
    ON Orders.CustomerID = Customers.CustomerID
    GROUP BY Customers.ContactName
    ORDER BY total;
    '''
    db.execute(query)
    results = db.fetchall()
    print(results)
    return results

def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''
    query = '''
    SELECT Employees.FirstName,Employees.LastName,SUM(UnitPrice*Quantity) as total
    FROM OrderDetails
    JOIN Orders
    ON OrderDetails.OrderID = Orders.OrderID
    JOIN Employees
    ON Orders.EmployeeID = Employees.EmployeeID
    GROUP BY Employees.EmployeeID
    ORDER BY total DESC;
    '''
    db.execute(query)
    results = db.fetchone()
    # print(results)
    return results
def orders_per_customer(db):
    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    pass  # YOUR CODE HERE


conn = sqlite3.connect('data/ecommerce.sqlite')
db = conn.cursor()

spent_per_customer(db)
