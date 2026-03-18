# Chapter 3: Memory, Filesystems, and Storage Layout

![Computer memory](assets/computer-memory.jpg)
*Image source: [Computer memory](https://en.wikipedia.org/wiki/Computer_memory) on Wikipedia / Wikimedia Commons.*

This chapter moves from operating-system control into the structures the OS must manage every day: memory, files, directories, disks, partitions, and boot-related storage structures.

Several topics that students often keep separate actually belong together:

- where running code lives,
- how the OS maps program-visible addresses onto real memory,
- how files are named and organized,
- how disks are physically laid out,
- and how the system divides storage into partitions, volumes, and boot structures.

If you confuse those layers, troubleshooting becomes guesswork.

## What You Should Be Able To Explain

By the end of this chapter, you should be able to explain:

- why memory management is an OS problem rather than an application problem,
- the difference between logical and physical addresses,
- how filesystems organize files, directories, metadata, inodes, and paths,
- why filenames and extensions can mislead users,
- how sectors, clusters, fragmentation, partitions, and volumes differ,
- and how MBR/GPT and BIOS/UEFI fit into storage and boot discussions.

## Memory Management Exists Because Raw Hardware Is Not Enough

If every program had to know the exact physical memory location where it would run, software would be fragile, difficult to move between systems, and unsafe in a multitasking environment.

The operating system solves that by treating memory as a managed resource rather than a pile of manually assigned addresses.

At a high level:

- the CPU executes instructions,
- memory holds instructions and data for running processes,
- and the OS decides how memory is assigned, protected, and reused.

That is why memory management belongs to the operating system. Applications depend on it, but they should not each invent their own machine-wide memory policy.

This chapter’s memory material works best when paired with the earlier hardware discussion:

- the CPU needs instructions and data quickly,
- registers and cache are too small to hold an entire workload,
- DRAM is large enough for active programs but still limited,
- and the OS must keep all of that usable even when many processes are competing at once.

## Logical Memory, Physical Memory, and Address Binding

One of the first important distinctions is:

- **logical address**: the address a program thinks it is using,
- **physical address**: the actual address in hardware memory.

The translation between those views is supported by the **MMU**, the Memory Management Unit.

This abstraction matters for several reasons:

- a program should not assume a fixed physical address,
- multiple programs need to coexist,
- the same program should run on different systems,
- and predictable fixed placement creates unnecessary security and stability problems.

The OS and hardware collaborate so that a program can operate with a logical view of memory while the machine maintains the real physical mapping.

The key hardware component here is the **MMU**. A student does not need to design one, but they should understand its job: helping translate the addresses a program uses into real memory locations that the machine can actually access.

That is why **address binding** matters. The system is binding a program’s logical view of memory to actual physical memory at the right time and in the right place, rather than forcing the program to assume a single fixed location forever.

## What Happens After a Program Is Loaded

Loading a program is only the beginning. The OS continues managing memory throughout execution.

### Dynamic loading

Not every routine has to be loaded immediately. Some code can be brought in only when it is needed. That conserves memory.

This is one of the places where the operating system stops being abstract theory. If a rarely used feature or library routine does not need to occupy memory yet, the system can defer loading it and preserve RAM for more urgent work.

### Shared libraries

Many programs reuse common libraries rather than carrying separate full copies of identical functionality in memory. That reduces waste and simplifies maintenance, even though it introduces dependency management.

### Paging and page tables

Modern systems often manage memory in fixed-size chunks called **pages**. The system keeps structures such as **page tables** to help translate program-visible memory references into the right backing memory.

Students should connect this to the logical/physical distinction immediately:

- the program uses addresses in its own logical view,
- the OS and hardware use page structures to resolve where that data really lives,
- and the process can continue without knowing the real placement details directly.

### Disk-backed memory and swapping

When RAM pressure rises, the system may rely on disk-backed memory mechanisms. That can extend apparent working memory, but it is much slower than RAM. This is why heavy swapping usually hurts performance and is treated as a sign that the workload and available memory are out of balance.

The important lesson is that memory management is about both **performance** and **control**.

This is also a place where students should avoid magical thinking. Using disk-backed memory does not “turn disk into RAM.” It is a fallback technique that helps the system survive memory pressure, usually at a noticeable performance cost.

## Memory Abstraction Improves Reliability and Security

Students sometimes hear about pages, address translation, or the MMU and assume these are just performance topics. They are also control topics.

If one process could casually read or overwrite another process’s memory, a multitasking OS would be nearly unusable. Memory abstraction helps support:

- process isolation,
- fault containment,
- multi-user systems,
- and safer execution of unrelated applications.

That is why memory management is closely related to privilege, process control, and later security material.

It is also why faults matter. A **page fault**, for example, is not automatically a catastrophe. It is part of the OS’s managed handling of memory access and backing storage. The important beginner lesson is that the OS must stay in control of how memory problems are resolved.

## Filesystems Turn Storage into a Manageable Namespace

Storage without a filesystem is just addressable space. A filesystem imposes structure.

Instead of treating storage as undifferentiated bytes, the operating system organizes it into:

- **files**,
- **directories**,
- and **metadata** describing those objects.

The directory structure is hierarchical. In practice, that means there is a top-level root and lower directories beneath it, forming a tree of paths and names.

The OS uses that structure to support actions such as:

- creating files,
- opening files,
- reading and writing data,
- renaming or deleting entries,
- and finding executables through path lookup.

That logical structure also depends on metadata objects that describe files beyond their visible names. In Unix-like filesystems, this is where the **inode** idea becomes important: the name in a directory entry is not the whole file. The filesystem also tracks ownership, permissions, timestamps, and block locations through metadata structures associated with that file.

At an introductory level, students should keep this distinction straight:

- the **filename** is how people usually refer to the file,
- the **directory entry** links that name into the hierarchy,
- and the **inode/metadata layer** describes the file object and where its contents live.

That is why file inspection, permissions, links, deletion, and later Linux storage work make more sense once you stop treating a file as “just a name with bytes behind it.”

In Linux, one practical way to reinforce this is by inspecting inode numbers directly with commands such as `ls -ail`. The point of the exercise is not the command itself. The point is that a file has metadata identity beyond its visible name.

## Filenames, Extensions, and Why Names Can Lie

A filename is helpful, but it is not truth by itself.

One of the useful introductory security lessons in this material is that default file-display behavior can hide important facts. In particular:

- a filename may not show the full extension,
- the visible name may encourage false assumptions,
- and users may mistake a dangerous file for a harmless one.

That is why file inspection should be disciplined. Do not trust a file purely because the visible beginning of the name looks familiar or safe.

This was a strongly practical lesson in the Windows material. If extensions are hidden, students can make bad assumptions quickly. A file that *looks* like a document may not actually be one. That is why “show the real name” is a defensive habit, not just a UI preference.

This also helps explain why administrators care about metadata and file attributes instead of only human-readable names.

## Paths, Command Lookup, and File Attributes

When you type a command, the OS or shell has to find the executable. That is where **PATH** comes in. The system searches expected locations rather than making you type a full absolute path every time.

That explains why:

- some commands run immediately,
- some require a full path,
- and some fail because the relevant directory is not in the search path.

In Windows, commands like `path` and `attrib` make this visible. `path` relates to command lookup. `attrib` relates to file properties such as whether a file is hidden. Those are different ideas, and students need both.

The same area of the material also introduces **attributes**. An attribute is not the same thing as a permission. Attributes describe properties or behaviors; permissions define allowed actions.

This distinction becomes important when students move from “why is the file hidden?” to “who is actually allowed to read or execute it?”

## Secondary Storage Has a Physical Layout and a Logical Layout

Mechanical hard drives are especially useful for teaching because their physical design is easy to visualize.

Important physical components include:

- **platters**,
- **read/write heads**,
- **tracks**,
- and **sectors**.

On that physical layout, two performance ideas matter:

- **seek time**: the time needed to move the head to the correct track,
- **rotational latency**: the wait for the right sector to rotate into position.

That physical reality is why scattered data hurts performance on spinning disks. The hardware cost of moving around the platter is real.

This is one reason traditional hard drives are still so useful in teaching. Their behavior is easy to visualize. Students can see why file layout, fragmentation, and access patterns matter because the hardware literally has to move.

The **logical layout** is the OS-facing view layered on top of that hardware.

## Sectors, Clusters, and Slack Space

Students should distinguish:

- a **sector** as a low-level storage unit,
- and a **cluster** as a filesystem allocation unit built from one or more sectors.

The OS usually allocates file storage in clusters, not raw sectors one at a time.

That introduces tradeoffs:

- small clusters waste less space with small files,
- larger clusters can reduce metadata overhead for some workloads,
- but larger clusters may waste more space at the tail end of many small files.

That wasted remainder is often called **slack space**. If a file uses only part of its final allocated cluster, the rest of that cluster is unavailable to other files.

This is one of the simplest examples of why “file size” and “space consumed on disk” are not always identical.

## File Allocation and Fragmentation

A file is not guaranteed to live in one perfect continuous run on disk. Over time, creation, deletion, growth, and resizing break free space into awkward pieces.

That leads to **fragmentation**.

- **Contiguous allocation** is simple and fast to read, but harder to preserve as disks fill up.
- **Non-contiguous allocation** is flexible, but requires metadata to keep track of where all the pieces live.

On mechanical disks, fragmentation can slow performance because the drive must gather file pieces from multiple locations. On SSDs, the physical penalty is different, which is why old blanket statements about fragmentation need context.

The reason is straightforward: SSDs do not have read heads seeking across spinning platters. They also use flash-management behavior such as wear-leveling internally. That means the classic “defragment regularly for speed” lesson from spinning disks does not transfer cleanly to SSDs.

The course material also tied deletion and secure erase to this storage discussion. On a magnetic hard drive, deleting a file usually removes references before the underlying data has truly disappeared. That is why overwrite tools, degaussing, or physical destruction show up in storage lessons. SSDs complicate this further because flash translation layers, wear-leveling, and TRIM change what “overwrite the same spot” even means.

## Filesystems: FAT and NTFS

The Windows-oriented storage material contrasts common filesystems such as **FAT** and **NTFS**.

### FAT

FAT remains historically important and is still relevant for compatibility. It is simple and widely supported, especially in removable-media contexts, but it offers fewer advanced features than newer filesystems.

That is why FAT-family filesystems keep reappearing on USB media and compatibility-focused devices even though they are not the best answer for every system disk.

### NTFS

NTFS introduces richer metadata handling and journaling behavior. **Journaling** helps the system recover more cleanly after interruptions such as crashes or power loss by tracking intended or in-progress changes.

Journaling is a reliability feature, not a magical backup system. It helps preserve consistency after interruption. It does not give you an automatic clean historical copy of every damaged or deleted file.

The important lesson is not that one filesystem is magic. It is that filesystem design affects:

- metadata richness,
- recovery behavior,
- compatibility,
- and administrative expectations.

The broader storage material also brought in Linux examples such as **ext4**, because students need to see that Windows is not the only filesystem world that matters. The durable lesson is comparative: file systems differ in features, recovery behavior, compatibility, and administrative tradeoffs.

## Boot-Related Storage Structures

Booting requires more than “a disk with files on it.” The system also depends on early boot structures.

Important terms include:

- **MBR**: Master Boot Record,
- **boot sector / VBR**: Volume Boot Record or partition boot sector,
- **bootloader**,
- **GPT**: GUID Partition Table,
- and **UEFI**.

The old model is commonly taught as:

1. firmware starts,
2. early boot code is read from disk,
3. that code helps find the next stage,
4. and eventually the operating system is loaded.

Students should understand the difference between:

- **whole-disk structure** such as partition layout and boot records,
- and the **filesystem inside a partition or volume**.

A disk can fail at one layer while another layer still looks fine. That is why storage troubleshooting must be layered.

This is where storage and startup meet. If the partition table is damaged, the problem is different from a damaged filesystem. If the filesystem is fine but the wrong boot structure is in place, that is a different failure again. Treating all “disk problems” as one category produces bad recovery decisions.

## Partitions and Volumes

A **partition** is a defined region of a physical disk. A **volume** is the usable storage entity the OS mounts and presents for use, usually with a filesystem on it.

In simple setups, one partition often becomes one volume, which is why students treat the words as interchangeable. Administratively, the distinction still matters.

Partitioning is used to:

- separate OS and data,
- support multi-boot layouts,
- create recovery areas,
- and organize storage for operational reasons.

This is also where management tools matter. Windows `diskpart`, Windows Disk Management, Linux partitioning tools, and later Linux LVM work all sit at different layers of the same storage story. A student who understands partitions and volumes will have a much easier time understanding why later Linux storage lessons add volume groups and logical volumes on top.

Students should also recognize tools such as DiskPart conceptually as command-line disk management tools, even if every exact command sequence is not part of the surviving reading pack.

## MBR vs GPT, BIOS vs UEFI

The storage and boot discussion eventually reaches the shift from older to newer platform models.

- **MBR** is the older partitioning style associated with legacy boot methods.
- **GPT** is the newer partitioning style commonly associated with **UEFI** systems.

Likewise:

- **BIOS** is the older firmware model,
- **UEFI** is the newer one.

The key lesson is not nostalgia. It is operational awareness. Real environments may contain both old and new systems, and troubleshooting or installation steps depend on which combination you are dealing with.

## Worked Examples and Teaching Moments

### Example: filenames can lie

One of the practical examples preserved from the foundational material is that users often trust the visible beginning of a filename instead of the actual file type. Hidden extensions and casual file browsing can make a dangerous file look harmless. That is why the book keeps tying file concepts to disciplined inspection instead of to cosmetic naming.

### Example: `path` and `attrib` are not trivia

The command-line material uses Windows examples to make filesystem behavior concrete. The `path` command shows how the system finds executables, while `attrib` demonstrates that a file can carry properties beyond its visible name. That is a good reminder that a file’s name, attributes, metadata, and executable status are related but not identical.

### Example: `diskpart` belongs in the storage conversation

The storage lectures do not keep partitioning purely theoretical. They tie the discussion to Windows `diskpart` as a command-line disk-management tool, which helps students connect partition tables, volumes, and boot structures to actual administrative tools instead of memorized vocabulary.

## Practice Connections

- For a Linux-focused continuation of the storage story, use [Linux Storage](../../course-materials/lectures/systems/linux-storage.md).
- For the chapter-to-repo map, use [Repo Companion Material](repo-companion-material.md).

## Chapter Summary

- Memory management exists so the OS can support flexibility, isolation, and multitasking.
- Logical addresses are mapped to physical memory with help from hardware such as the MMU.
- Filesystems organize persistent storage into files, directories, metadata, and inode-like tracking structures.
- Filenames and visible extensions can mislead users; disciplined inspection matters.
- Disks have both physical layout and logical allocation structures.
- Partitions, volumes, boot records, MBR/GPT, and BIOS/UEFI are related but distinct layers of the storage and startup story.

## Review Questions

1. Why does the operating system use logical addresses instead of forcing programs to use fixed physical addresses?
2. What is the difference between a filesystem and a raw storage device?
3. Why is a file not “just a name,” and what role do metadata or inodes play in that distinction?
4. How do sectors and clusters differ?
5. Why is it important to distinguish partitions, volumes, and boot structures during troubleshooting?

## Further Reading

- [Computer memory](https://en.wikipedia.org/wiki/Computer_memory)
- [Memory management](https://en.wikipedia.org/wiki/Memory_management)
- [Memory management unit](https://en.wikipedia.org/wiki/Memory_management_unit)
- [File system](https://en.wikipedia.org/wiki/File_system)
- [Disk partitioning](https://en.wikipedia.org/wiki/Disk_partitioning)
- [GUID Partition Table](https://en.wikipedia.org/wiki/GUID_Partition_Table)
