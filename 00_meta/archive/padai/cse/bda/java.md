## 1. Data Structures in Java

### 1.1 Linked List

> A **Linked List** is a dynamic data structure where elements (nodes) are connected via pointers. No fixed size — grows as elements are added.

**Types of Linked Lists:**

- Singly Linked List (one direction pointer)
- Doubly Linked List (forward and backward pointers)
- Circular Linked List (last node points to first)

**Node Structure:**

```java
class Node {
    protected int data;
    protected Node link;

    public Node() { link = null; data = 0; }
    public Node(int d, Node n) { data = d; link = n; }

    public void setLink(Node n) { link = n; }
    public void setData(int d) { data = d; }
    public Node getLink() { return link; }
    public int getData() { return data; }
}
```

**Linked List Operations:**

```java
class linkedList {
    protected Node start;
    protected Node end;
    public int size;

    // Insert at beginning — O(1)
    public void insertAtStart(int val) {
        Node nptr = new Node(val, null);
        size++;
        if (start == null) { start = nptr; end = start; }
        else { nptr.setLink(start); start = nptr; }
    }

    // Insert at end — O(1)
    public void insertAtEnd(int val) {
        Node nptr = new Node(val, null);
        size++;
        if (start == null) { start = nptr; end = start; }
        else { end.setLink(nptr); end = nptr; }
    }

    // Insert at position — O(n)
    public void insertAtPos(int val, int pos) { ... }

    // Delete at position — O(n)
    public void deleteAtPos(int pos) { ... }
}
```

**Common Uses of Linked Lists:**

- Implementing Stacks and Queues
- Implementing Binary Trees
- Dynamic memory allocation

---

### 1.2 Stack

> A **Stack** is a LIFO (Last In, First Out) data structure. The last element inserted is the first to be removed.

**Operations:**

- `push()` — insert element on top
- `pop()` — remove element from top
- `peek()` — read top without removing
- `isEmpty()` — check if stack is empty
- `isFull()` — check if stack is full

```java
public class MyStack {
    private int maxSize;
    private long[] stackArray;
    private int top;

    public MyStack(int s) {
        maxSize = s;
        stackArray = new long[maxSize];
        top = -1;
    }

    public void push(long j) { stackArray[++top] = j; }
    public long pop()        { return stackArray[top--]; }
    public long peek()       { return stackArray[top]; }
    public boolean isEmpty() { return (top == -1); }
    public boolean isFull()  { return (top == maxSize - 1); }
}
```

**Stack Visualization:**

```
push(10) → [10]
push(20) → [10, 20]
push(30) → [10, 20, 30]
pop()    → returns 30 → [10, 20]
peek()   → returns 20 → [10, 20]
```

---

### 1.3 Queue

> A **Queue** is a FIFO (First In, First Out) data structure. The first element inserted is the first to be removed.

**Operations:**

- `add()` — add element to rear
- `remove()` — remove from front (throws exception if empty)
- `poll()` — remove from front (returns null if empty)
- `element()` — read front without removing (throws exception)
- `peek()` — read front without removing (returns null if empty)

```java
Queue queue = new LinkedList();
queue.add("Java");
queue.add("Hadoop");

queue.remove();    // removes "Java"
queue.element();   // reads front → "Hadoop"
queue.poll();      // removes and returns "Hadoop"
queue.peek();      // reads front, null if empty
```

**Queue Visualization:**

```
add("A") → [A]
add("B") → [A, B]
add("C") → [A, B, C]
remove() → returns "A" → [B, C]
peek()   → returns "B" → [B, C]
```

---

### 1.4 Set

> A **Set** is a collection of **unique** elements — no duplicates allowed. Java uses `HashSet` for unordered sets.

```java
HashSet hashset = new HashSet();
hashset.add(3);
hashset.add("srinivas");
hashset.add("srinivas");  // duplicate — ignored
System.out.println("Set is " + hashset);
// Output: Set is [3, srinivas, ...]
```

**Set Properties:**

- No duplicates
- No guaranteed order (HashSet)
- `contains()`, `add()`, `remove()` operations
- Used for membership testing

---

### 1.5 Map

> A **Map** stores **key-value pairs**. Each unique key maps to exactly one value. Retrieval is done via the key.

```java
Map m1 = new HashMap();
m1.put("Zara", "8");
m1.put("Mahnaz", "31");
m1.put("Ayan", "12");

System.out.println(m1);
// Output: {Mahnaz=31, Ayan=12, Zara=8}
```

**Common Map Exceptions:**

- `NoSuchElementException` — key not found
- `ClassCastException` — incompatible key type
- `NullPointerException` — null key not allowed
- `UnsupportedOperationException` — map is unmodifiable

**Map Implementations:**

|Class|Order|Null keys|Thread-safe|
|---|---|---|---|
|`HashMap`|None|Yes (one)|No|
|`TreeMap`|Sorted|No|No|
|`LinkedHashMap`|Insertion|Yes|No|
|`Hashtable`|None|No|Yes|

---

## 2. Generics in Java

> **Generics** allow writing a single method or class that works with multiple types while providing **compile-time type safety**.

### Generic Methods

```java
public class GenericMethodTest {
    // Type parameter <E> declared before return type
    public static <E> void printArray(E[] inputArray) {
        for (E element : inputArray) {
            System.out.printf("%s ", element);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Integer[] intArray    = {1, 2, 3, 4, 5};
        Double[]  doubleArray = {1.1, 2.2, 3.3};
        Character[] charArray = {'H', 'E', 'L', 'L', 'O'};

        printArray(intArray);    // works for Integer
        printArray(doubleArray); // works for Double
        printArray(charArray);   // works for Character
    }
}
```

### Bounded Type Parameters

Restrict the types allowed: `<T extends Comparable<T>>`

```java
public static <T extends Comparable<T>> T maximum(T x, T y, T z) {
    T max = x;
    if (y.compareTo(max) > 0) max = y;
    if (z.compareTo(max) > 0) max = z;
    return max;
}

// Works for: Integer, Double, String (anything Comparable)
maximum(3, 4, 5);           // returns 5
maximum(6.6, 8.8, 7.7);    // returns 8.8
maximum("pear", "apple", "orange");  // returns "pear"
```

### Generic Classes

```java
public class Box<T> {
    private T t;

    public void add(T t) { this.t = t; }
    public T get() { return t; }

    public static void main(String[] args) {
        Box<Integer> intBox = new Box<Integer>();
        Box<String> strBox  = new Box<String>();

        intBox.add(10);
        strBox.add("Hello World");

        System.out.println(intBox.get());  // 10
        System.out.println(strBox.get());  // Hello World
    }
}
```

**Rules for Generic Methods:**

- Type parameter section uses angle brackets `<E>`
- Placed before the return type
- Can declare multiple type parameters: `<K, V>`
- Type parameters represent only **reference types** (not primitives like `int`)

---

## 3. Wrapper Classes

> **Wrapper classes** wrap Java primitive types into objects, enabling them to be used where objects are required (collections, generics, etc.).

### Primitive → Wrapper Mapping

|Primitive|Wrapper Class|
|---|---|
|`boolean`|`Boolean`|
|`char`|`Character`|
|`byte`|`Byte`|
|`short`|`Short`|
|`int`|`Integer`|
|`long`|`Long`|
|`float`|`Float`|
|`double`|`Double`|

All numeric wrappers extend `java.lang.Number`.

### Autoboxing and Unboxing (Java 5+)

```java
// Autoboxing: primitive → object (automatic)
int a = 20;
Integer i = Integer.valueOf(a);  // explicit
Integer j = a;                   // autoboxing (compiler adds valueOf)

// Unboxing: object → primitive (automatic)
Integer x = new Integer(3);
int m = x.intValue();  // explicit
int n = x;             // unboxing (compiler adds intValue)
```

### Why Wrapper Classes?

- Use primitives in **Collections** (`List<Integer>` not `List<int>`)
- Use with **Generics** (type parameters must be reference types)
- Provide utility methods: `Integer.parseInt()`, `Double.valueOf()`, etc.
- Enable **null** values (primitives cannot be null)

---

## 4. Serialization in Java

> **Serialization** converts an object into a byte stream for storage or network transmission. **Deserialization** rebuilds the object from those bytes.

### Key Properties

- Process is **JVM-independent** — serialize on one platform, deserialize on another
- Classes must implement `java.io.Serializable`
- All fields must be serializable, or marked `transient`
- `transient` fields are **NOT serialized** (reset to default values on deserialization)

### Serializable Class Example

```java
public class Student implements java.io.Serializable {
    public String name;
    public String address;
    public transient int SSN;  // NOT serialized
    public int number;
}
```

### Serializing an Object

```java
import java.io.*;

public class SerializeDemo {
    public static void main(String[] args) {
        Student e = new Student();
        e.name = "srinivas";
        e.address = "ibm vijayawada";
        e.SSN = 11122333;   // transient — won't be saved
        e.number = 101;

        try {
            FileOutputStream fileOut = new FileOutputStream("/tmp/Student.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(e);   // serialize
            out.close();
            fileOut.close();
            System.out.println("Serialized data saved in /tmp/Student.ser");
        } catch (IOException i) {
            i.printStackTrace();
        }
    }
}
```

### Deserializing an Object

```java
import java.io.*;

public class DeserializeDemo {
    public static void main(String[] args) {
        Student e = null;
        try {
            FileInputStream fileIn = new FileInputStream("/tmp/Student.ser");
            ObjectInputStream in = new ObjectInputStream(fileIn);
            e = (Student) in.readObject();  // deserialize
            in.close();
            fileIn.close();
        } catch (IOException i) {
            i.printStackTrace();
        } catch (ClassNotFoundException c) {
            System.out.println("Student class not found");
        }

        System.out.println("Name: " + e.name);       // srinivas
        System.out.println("Address: " + e.address); // ibm vijayawada
        System.out.println("SSN: " + e.SSN);         // 0 (transient!)
        System.out.println("Number: " + e.number);   // 101
    }
}
```

### Important Notes

- `SSN` was `11122333` before serialization → becomes `0` after (transient)
- `readObject()` returns `Object` — must cast to correct type
- `ClassNotFoundException` thrown if JVM cannot find class bytecode during deserialization
- File extension convention: `.ser`

---

