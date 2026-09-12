📝 [[Problems - Speed]]

---
## Time, Speed & Distance

- Conversion factor: km/h = 5/18 m/s.
- You can solve problems involving s=dt using product constancy rule as well.
- average speed: using [Alligation](Alligation.md)
	## Case 1:
	 Same Distance
	- Speeds: S1, S2
	- Time ratio = inverse of speed ratio (S2:S1)
	- Avg speed = (S1×t1 + S2×t2)/(t1+t2)
	- Shortcut: 2×S1×S2/(S1+S2)
	
	## Case 2: Different Distances
	- Speed ratio → inverse → multiply by distance ratio → get time weights
	- Example: 66 km/h (100km), 110 km/h (200km)
	  - Speed ratio 3:5 → inverse 5:3 → × distance ratio 1:2 → weights 5:6
	  - Avg = (66×5 + 110×6)/11 = 90 km/h
- Train theory
	## Opposite Direction
	`(S_T + S_O) × t = L_T + L_O`
	## Same Direction
	`(S_T - S_O) × t = L_T + L_O`
	Where:  
	- `S_T`, `S_O` = speeds of train & object  
	- `L_T`, `L_O` = lengths of train & object  
	- `t` = time to cross
	
	## Problem: Train Crosses Man in Moving Train
	**Given:**  
	- Opposite direction: 8s  
	- Same direction: 25s  
	- Train 1 length: 200m  
	- Train 2 length: 160m
	
	**Key Insight:** Man is a point (no length). Train 2's length is irrelevant.
	
	**Setup:**
	- Opposite: `(S_1 + S_2) × 8 = 200`  
	- Same: `(S_1 - S_2) × 25 = 200`
	
	**Solve:**
	- From eq 1: `S_1 + S_2 = 25`
	- From eq 2: `S_1 - S_2 = 8`
	- Add: `2S_1 = 33` → `S_1 = 16.5 m/s = 59.4 km/h`
- Circular Motion
	- https://www.hitbullseye.com/Quant/Circular-Motion.php
	## First Meeting (Anywhere on Circle)
	Bodies start together, move same direction. They meet when fastest completes laps.
	
	**Method:** Find LCM of overlap times
	- `T_AB` = time for A to completely lap B
	- `T_AC` = time for A to completely lap C
	- `T_AD` = time for A to completely lap D
	- **First meeting time** = `LCM(T_AB, T_AC, T_AD)`
	> Fastest runner must lap all slower ones simultaneously.

	## First Meeting at Starting Point
	Bodies return to original position together.
	
	**Method:** Find LCM of individual lap times
	- `T_A` = time for A to complete 1 full round
	- `T_B` = time for B to complete 1 full round
	- `T_C` = time for C to complete 1 full round
	- **Meeting at start** = `LCM(T_A, T_B, T_C)`
- Clock
	- See problems
- back and fro motion
	- In this type of question don't treat speeds differently, take relative speed by adding individual speed(because they are moving towards each other) and for the first meet distance needed to travel 100km(for 1st meet) after that for every meet the distance needed to cover(to meet) will become 200 . So 100+200+200/80 . This gives the time after which they meet for the third time. With this time multiply the speed of Ram to get the distance covered by him
	- https://t.me/c/2261703493/11260
📝 [[Problems - Speed]]