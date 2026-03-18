# OS & Networking Fundamentals

- Filename: `OS & Networking Fundamentals.pptx`
- Subject: `systems`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/OS%20%26%20Networking%20Fundamentals.pptx)

## Summary

This reusable introductory lecture deck combines operating system fundamentals with basic networking concepts in one broad survey lesson. The first half explains what an operating system does, focusing on resource management duties such as CPU scheduling, memory management, virtual memory, swapping, disk and filesystem management, and I/O handling through device drivers. It then explains the kernel's role as the privileged resource manager, introduces protection rings with Ring 0 and Ring 3, and uses system calls to show how applications safely request kernel services. The second half shifts to networking fundamentals, introducing OSI Layers 1 through 3, the role of LLC and MAC at Layer 2, IP routing and logical addressing at Layer 3, and the difference between hubs, bridges, and switches.

## Key Details

- Defines the operating system as the software layer that manages hardware and software resources, user interaction, and file operations.
- Covers CPU scheduling and names approaches such as round-robin, priority-based, and multilevel queue scheduling.
- Explains memory management with emphasis on virtual memory, paging, and swapping.
- Includes disk and filesystem management concepts such as partitions, file organization, free-space tracking, and read/write operations.
- Teaches the kernel as the privileged resource manager and ties it to protection rings and the difference between Ring 0 and Ring 3.
- Uses system calls as the bridge between user applications and kernel services.
- Explains stability issues including memory access violations, buffer overflows, deadlocks, driver bugs, hardware faults, resource exhaustion, and kernel panic.
- Introduces the OSI model with specific attention to Layers 1 through 3.
- Breaks Layer 2 into LLC and MAC sublayers.
- Compares hubs, bridges, and switches, including their OSI layers and forwarding behavior.
- Assigns homework on operating systems, the OSI model, and TCP/IP versus OSI comparison.
- Ends with a lab teaser on network discovery, Layer 2 addresses and OUIs, connecting to another group's web server, and identifying the default gateway's OUI.

## Tags

- `operating-systems`
- `kernel`
- `virtual-memory`
- `osi-model`
- `switching`
- `layer-2`
- `layer-3`
- `networking-fundamentals`
