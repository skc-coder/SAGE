---
title: "Evolution of Polymorphism: C-Style Tagged Unions & Function Switches"
tags: [c, cpp, refactoring, architectural-evolution, design-patterns, sage]
date: 2026-09-14
---

# 📜 Evolution of Polymorphism: C-Style Tagged Unions & Function Switches

## 🧠 Intuition & Core Motivation

Before C++ introduced inheritance and virtual function dispatch, how did procedural software written in C handle situations where different types of entity items required distinct processing algorithms?

The traditional C approach relied on **Explicit Type Tagging (Discriminators)** combined with **Manual Control Flow (Function Switches or `if-else` Cascades)**.

Think of procedural C polymorphism like a **manual sorting conveyor belt**:
- Every item coming down the belt carries a colored tag (an `enum` type code).
- The worker standing at the belt must look at the tag, read its type code, and manually flip a switch to route the item to processing routine `A`, `B`, or `C`.
- If a new product with a purple tag is introduced tomorrow, every single worker across the factory floor must be updated with new instructions for the purple tag!

---

## 1. Case Study: Staff Salary Processing Problem Requirements

Consider an enterprise payroll processing system managing different roles:
1. **Engineers**: Earn a base salary.
2. **Managers**: Earn a base salary + dynamic managerial allowance. They also supervise a group of Engineers.
3. **Directors**: Earn a base salary + managerial allowance + performance bonus + stock options.

The software must compute net monthly salaries, generate pay slips, and handle dynamic staff lists.

---

## 2. The Procedural C Implementation

In pure C, programmers structure heterogeneous entities using an `enum` discriminator tag and a `struct` containing either type-specific structs or raw unions.

### 2.1 C Type Definitions & Data Representation
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Explicit Discriminator Tag
typedef enum {
    TYPE_ENGINEER,
    TYPE_MANAGER,
    TYPE_DIRECTOR
} EmployeeType;

typedef struct {
    char name[50];
    double baseSalary;
} Engineer;

typedef struct {
    char name[50];
    double baseSalary;
    double managerAllowance;
} Manager;

typedef struct {
    char name[50];
    double baseSalary;
    double managerAllowance;
    double bonus;
} Director;

// Staff Container storing generic pointers and explicit type tags
typedef struct {
    EmployeeType type;
    void* data; // Pointer to Engineer, Manager, or Director struct
} Employee;
```

---

### 2.2 Manual Type Dispatching via Function Switch

To calculate salaries, procedural C code uses `switch` statements matching on `EmployeeType`:

```c
void ProcessSalary(Employee* emp) {
    switch (emp->type) {
        case TYPE_ENGINEER: {
            Engineer* eng = (Engineer*)emp->data;
            double total = eng->baseSalary;
            printf("Engineer %s Salary: $%.2f\n", eng->name, total);
            break;
        }
        case TYPE_MANAGER: {
            Manager* mgr = (Manager*)emp->data;
            double total = mgr->baseSalary + mgr->managerAllowance;
            printf("Manager %s Salary: $%.2f\n", mgr->name, total);
            break;
        }
        case TYPE_DIRECTOR: {
            Director* dir = (Director*)emp->data;
            double total = dir->baseSalary + dir->managerAllowance + dir->bonus;
            printf("Director %s Salary: $%.2f\n", dir->name, total);
            break;
        }
    }
}
```

---

## 3. Critical Flaws & Architectural Bottlenecks of C-Style Dispatch

While the C solution works for small, static programs, it breaks down disastrously under enterprise scale:

### 1. Violation of Open-Closed Principle (OCP)
The Open-Closed Principle states that code should be *open for extension, but closed for modification*.
Adding a new role (e.g., `SalesExecutive`) in the C solution forces changes in **every single place**:
- Add `TYPE_SALES` to `enum EmployeeType`.
- Create `typedef struct SalesExecutive`.
- Update every `switch(emp->type)` statement across the codebase (`ProcessSalary`, `DeallocateStaff`, `PrintTaxSlip`, etc.). Missing even one switch branch causes silent runtime bugs!

### 2. Zero Encapsulation & Data Duplication
Common attributes (`name`, `baseSalary`) are duplicated inside `Engineer`, `Manager`, and `Director`. Data fields are completely public, exposing memory to accidental corruption.

### 3. Untype-safe Casting Risks
`void* data` strips all static type checking. If `emp->type` is set to `TYPE_MANAGER` but `emp->data` accidentally points to an `Engineer` struct, casting `(Manager*)emp->data` reads corrupted memory without warning!

### 4. Memory Deallocation Fragility
Custom `Init...()` and `Free...()` routines must be manually maintained for each struct type, increasing the risk of memory leaks.

---

## 💡 Related Idioms & Patterns

- **Tagged Union / Discriminant Pattern**: Representing variant types using a tag enum + union (modernized in C++17 via `std::variant` and `std::visit`).

---

## 📋 Comprehensive Verification Checklist

- [x] Tagged union discriminator pattern in C demonstrated.
- [x] Procedural function switch dispatch architecture implemented.
- [x] 4 major architectural drawbacks (OCP violation, lack of encapsulation, `void*` type safety failure, dynamic memory cleanup fragility) detailed.
