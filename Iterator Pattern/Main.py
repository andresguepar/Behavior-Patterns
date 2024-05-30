import Employee,Organization


def main():

    # Crear empleados
    ceo = Employee.Employee("Alice", "CEO")
    cto = Employee.Employee("Bob", "CTO")
    cfo = Employee.Employee("Charlie", "CFO")
    dev1 = Employee.Employee("Dave", "Developer")
    dev2 = Employee.Employee("Eve", "Developer")
    fin1 = Employee.Employee("Frank", "Financial Analyst")

    # Construir la jerarquía
    ceo.add_subordinates(cto)
    ceo.add_subordinates(cfo)
    cto.add_subordinates(dev1)
    cto.add_subordinates(dev2)
    cfo.add_subordinates(fin1)

    # Crear la organización
    org = Organization.Organization(ceo)

    # Iterar sobre la organización
    for employee in org:
        print(employee)

# Ejecutar la función main
if __name__ == "__main__":
    main()
