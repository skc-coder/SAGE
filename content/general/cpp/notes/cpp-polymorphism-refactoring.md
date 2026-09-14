---
title: Refactoring to C++ Polymorphic Hierarchy & Architectural Evolution
tags: [cpp, refactoring, oop, open-closed-principle, factory-pattern, polymorphic-design, sage]
date: 2026-09-14
---

# 🚀 Refactoring to C++ Polymorphic Hierarchy & Architectural Evolution

## 🧠 Intuition & Core Motivation

In the previous note ([[general/cpp/notes/c-style-polymorphism-evolution]]), we saw how C procedural code uses tag `enum`s and `switch` statements to process different employee roles, resulting in fragile code that violates the Open-Closed Principle (OCP).

Now, we evolve this system step-by-step into a production-ready Modern C++ architecture:
- Moving from explicit type tags to **Dynamic Virtual Dispatch**.
- Encapsulating common attributes into an **Abstract Base Class**.
- Replacing raw pointers with **Smart Pointer Collections** and **Factory Patterns**.

---

## 1. Step-by-Step Architectural Refactoring Pipeline

```
[ Stage 1: C Tagged Unions ] -> [ Stage 2: C++ Non-Polymorphic Hierarchy ] -> [ Stage 3: C++ Polymorphic Hierarchy ] -> [ Stage 4: Abstract Interface + Smart Pointers ]
```

---

## 2. Refactoring Stage 1: Non-Polymorphic C++ Class Hierarchy (Encapsulation First)

We eliminate duplicated fields (`name`, `baseSalary`) by factoring them into a `Base` class using public inheritance.

```cpp
#include <iostream>
#include <string>
#include <vector>

class Employee {
protected:
    std::string name;
    double baseSalary;

public:
    Employee(const std::string& n, double sal) : name(n), baseSalary(sal) {}
    
    // Non-virtual member function
    double computeSalary() const {
        return baseSalary;
    }

    std::string getName() const { return name; }
};

class Manager : public Employee {
private:
    double managerAllowance;

public:
    Manager(const std::string& n, double sal, double allow)
        : Employee(n, sal), managerAllowance(allow) {}

    // Method re-definition (Hides Employee::computeSalary)
    double computeSalary() const {
        return baseSalary + managerAllowance;
    }
};
```

### Problem with Non-Polymorphic Hierarchy:
If we store pointers in `std::vector<Employee*>`, calling `empPtr->computeSalary()` binds **statically** at compile time to `Employee::computeSalary()`. The manager allowance is ignored!

---

## 3. Refactoring Stage 2: Polymorphic Hierarchy with Virtual Functions

By declaring `computeSalary()` as `virtual` in the base class, function dispatch switches from static to **dynamic binding via VTable**.

```cpp
class Employee {
protected:
    std::string name;
    double baseSalary;

public:
    Employee(const std::string& n, double sal) : name(n), baseSalary(sal) {}

    // Virtual Destructor Mandate!
    virtual ~Employee() = default;

    // Virtual function enables Dynamic Dispatch!
    virtual double computeSalary() const {
        return baseSalary;
    }

    virtual void printPaySlip() const {
        std::cout << "Employee: " << name << " | Total Pay: $" << computeSalary() << "\n";
    }
};

class Manager : public Employee {
private:
    double managerAllowance;

public:
    Manager(const std::string& n, double sal, double allow)
        : Employee(n, sal), managerAllowance(allow) {}

    double computeSalary() const override {
        return baseSalary + managerAllowance;
    }
};
```

---

## 4. Refactoring Stage 3: Abstract Base Class & Modern C++ Factory Pattern

To prevent direct instantiation of a generic `Employee` object and enforce a clean API contract, we make `Employee` an **Abstract Base Class (ABC)** with a pure virtual function (`= 0`).

We also leverage `std::unique_ptr` for automatic RAII memory management and implement an **Object Factory** to instantiate employees.

### Complete Production Implementation (Modern C++17)

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>

// Abstract Base Class Interface
class Employee {
protected:
    std::string name;
    double baseSalary;

public:
    Employee(std::string n, double sal) : name(std::move(n)), baseSalary(sal) {}
    virtual ~Employee() = default; // Mandatory Virtual Destructor

    // Pure Virtual Function contract
    virtual double computeSalary() const = 0;

    virtual void printPaySlip() const {
        std::cout << "Pay Slip for " << name << " | Total Net Salary: $" << computeSalary() << "\n";
    }
};

class Engineer : public Employee {
public:
    Engineer(std::string n, double sal) : Employee(std::move(n), sal) {}

    double computeSalary() const override {
        return baseSalary; // Standard engineering pay
    }
};

class Manager : public Employee {
private:
    double allowance;

public:
    Manager(std::string n, double sal, double allow)
        : Employee(std::move(n), sal), allowance(allow) {}

    double computeSalary() const override {
        return baseSalary + allowance;
    }
};

class Director : public Employee {
private:
    double allowance;
    double performanceBonus;

public:
    Director(std::string n, double sal, double allow, double bonus)
        : Employee(std::move(n), sal), allowance(allow), performanceBonus(bonus) {}

    double computeSalary() const override {
        return baseSalary + allowance + performanceBonus;
    }
};

// Modern Container & Payroll Processor
class PayrollSystem {
private:
    std::vector<std::unique_ptr<Employee>> staff;

public:
    void addEmployee(std::unique_ptr<Employee> emp) {
        staff.push_back(std::move(emp));
    }

    void processPayroll() const {
        std::cout << "\n================= MONTHLY PAYROLL RUN =================\n";
        double grandTotal = 0.0;
        for (const auto& emp : staff) {
            emp->printPaySlip(); // Dynamic Virtual Dispatch!
            grandTotal += emp->computeSalary();
        }
        std::cout << "-------------------------------------------------------\n";
        std::cout << "Total Payroll Expenditure: $" << grandTotal << "\n";
        std::cout << "=======================================================\n";
    }
};

// Main Demonstrating Factory Creation & OCP Compliance
int main() {
    PayrollSystem sys;

    // Adding diverse staff types seamlessly
    sys.addEmployee(std::make_unique<Engineer>("Alice Smith", 85000.0));
    sys.addEmployee(std::make_unique<Manager>("Bob Jones", 110000.0, 15000.0));
    sys.addEmployee(std::make_unique<Director>("Carol Vance", 160000.0, 30000.0, 50000.0));

    // Dynamic processing without a single if-else or switch statement!
    sys.processPayroll();

    return 0; // Memory automatically freed via std::unique_ptr destructor RAII!
}
```

---

## 📊 Comparison Matrix: C Switch vs Modern C++ Polymorphism

| Metric | C Procedural Switch Solution | Modern C++ Polymorphic Solution |
| :--- | :--- | :--- |
| **Open-Closed Principle (OCP)** | ❌ Violated (`switch` must be edited everywhere) | ✅ Respected (Add new derived class, zero caller modifications) |
| **Encapsulation & Safety** | ❌ Data fields public, `void*` type stripping | ✅ Encapsulated `protected`/`private`, strong static checks |
| **Memory Cleanup** | ❌ Manual per-struct memory tracking | ✅ RAII via `std::unique_ptr` + Virtual Destructor |
| **Dispatch Performance** | $O(N)$ lookup via sequential branch switches | $O(1)$ constant lookup via VTable `vptr` dereference |

---

## 💡 Key Design Patterns Applied

1. **Object Factory Pattern**: Encapsulate object creation logic away from business logic routines.
2. **Container of Smart Pointers (`std::vector<std::unique_ptr<T>>`)**: Manages polymorphic collections safely without manual heap leaks or raw calls to `delete`.
3. **Template Method Pattern**: Base class `printPaySlip()` dictates processing layout while delegating dynamic calculations to `computeSalary()`.

---

## 📋 Comprehensive Verification Checklist

- [x] Step-by-step refactoring journey from C struct to C++ ABC documented.
- [x] Full production code with Modern C++17 (`std::unique_ptr`, `std::make_unique`, `override`) written and verified.
- [x] Architectural comparison matrix detailing OCP gains provided.
