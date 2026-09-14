that stores each [bit](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/Bit "Bit") of data in a [memory cell](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/Memory_cell_\(computing\) "Memory cell (computing)"), usually consisting of a tiny capacitor and a transistor, both typically based on metal–oxide–semiconductor (MOS) technology
	- DRAM requires an external [memory refresh](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/Memory_refresh "Memory refresh") circuit which periodically rewrites the data in the capacitors, restoring them to their original charge
	- SRAM, which is faster and more expensive than DRAM, is typically used where speed is of greater concern than cost and size, such as the [cache memories](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/CPU_cache "CPU cache") in [processors](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/Central_processing_unit "Central processing unit")

SDRAM
># Synchronous dynamic random-access memory
		DRAM integrated circuits (ICs) produced from the early 1970s to the early 1990s used an _asynchronous_ interface, in which input control signals have a direct effect on internal functions delayed only by the trip across its semiconductor pathways. SDRAM has a _synchronous_ interface, whereby changes on control inputs are recognised after a rising edge of its clock input. In SDRAM families standardized by [JEDEC](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/JEDEC "JEDEC"), the clock signal controls the stepping of an internal finite-state machine that responds to incoming commands. These commands can be pipelined to improve performance, with previously started operations completing while new commands are received. The memory is divided into several equally sized but independent sections called _[banks](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/Memory_bank "Memory bank")_, allowing the device to operate on a memory access command in each bank simultaneously and speed up access in an [interleaved](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/Interleaved_memory "Interleaved memory") fashion. This allows SDRAMs to achieve greater concurrency and higher data transfer rates than asynchronous DRAMs could.
		

	
DDR
		**Double Data Rate Synchronous Dynamic Random-Access Memory** (**DDR SDRAM**) is a type of [synchronous dynamic random-access memory](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/Synchronous_dynamic_random-access_memory "Synchronous dynamic random-access memory") (SDRAM) widely used in computers and other electronic devices. It improves on earlier SDRAM technology by transferring data on both the rising and falling edges of the clock signal, effectively doubling the data rate without increasing the clock frequency. This technique, known as [double data rate](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/Double_data_rate "Double data rate") (DDR), allows for higher memory bandwidth while maintaining lower power consumption and reduced signal interference.
	
LPDDR
	Low Power DDR RAM for portable devices.
SRAM
	- Based on latching circuitry eg flip flops
	- SRAM will hold its data permanently in the **presence of power**, while data in DRAM decays in seconds and thus must be periodically [refreshed](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/Memory_refresh "Memory refresh").
	- SRAM is faster than DRAM but it is more expensive in terms of silicon area and cost.
	- Typically, SRAM is used for the [cache](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/CPU_cache "CPU cache") and internal [registers](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/CPU_register "CPU register") of a [CPU](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/CPU "CPU") while DRAM is used for a computer's [main memory](http://127.0.0.1:8080/content/wikipedia_en_computer_maxi_2025-08/Main_memory "Main memory").


**Examples**:
	Cache
	Main memory
	CAM
VRAM/GPU