| Hadoop                                | JavaScript        |
| ------------------------------------- | ----------------- |
| **Map** - transform each element      | `Array.map()`     |
| **Reduce** - aggregate/combine values | `Array.reduce()`  |
| **Filter** - select matching elements | `Array.filter()`  |
| **forEach** - iterate over elements   | `Array.forEach()` |

Quick examples:

```javascript
const arr = [1, 2, 3, 4];

// Map: transform each element
arr.map(x => x * 2); // [2, 4, 6, 8]

// Reduce: aggregate
arr.reduce((sum, x) => sum + x, 0); // 10

// Filter: select
arr.filter(x => x > 2); // [3, 4]

// Chain them
arr.map(x => x * 2).filter(x => x > 4).reduce((sum, x) => sum + x, 0); // 24
```

