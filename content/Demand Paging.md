## segmentation

- memory is divided into **variable-sized logical segments**
    
- each segment represents a logical unit:
    
    - code
        
    - stack
        
    - heap
        
    - global data
        

### address format

- logical address = `(segment_number, offset)`
    

### segment table

- per-process table
    
- each entry:
    
    - **base** → starting physical address
        
    - **limit** → length of segment
        

### translation

1. use `segment_number` to index segment table
    
2. check `offset < limit`
    
3. physical address = `base + offset`
    

### properties

- supports **modularity**
    
- easy **sharing** (multiple processes map same segment)
    
- fine-grained **protection** (per segment)
    

### problems

- **external fragmentation**
    
- allocation becomes complex over time
    

---

## demand paging

- paging variant where pages are loaded **only when needed**
    
- avoids loading entire process into memory
    

### key idea

- bring page into memory **on first access**
    

### page table

- includes:
    
    - **valid/invalid bit**
        
        - valid → page is in memory
            
        - invalid → page not in memory
            

### page fault

when process accesses a page not in memory:

1. trap to OS (page fault)
    
2. OS checks if access is valid
    
3. locate page on disk (swap)
    
4. find free frame (or replace one)
    
5. load page into memory
    
6. update page table
    
7. restart instruction
    

### properties

- reduces **memory usage**
    
- allows **larger programs** than RAM
    
- improves **multiprogramming**
    

### costs

- page fault is expensive (disk I/O)
    
- excessive faults → **thrashing**
    

---

## segmentation vs demand paging

|feature|segmentation|demand paging|
|---|---|---|
|unit|variable size|fixed size (pages)|
|view|logical|physical|
|fragmentation|external|internal|
|allocation|complex|simple|
|protection|per segment|per page|

---

## quick mental model

- segmentation = _how programmer sees memory_
    
- paging = _how OS manages memory efficiently_
    
- demand paging = _lazy loading of pages_