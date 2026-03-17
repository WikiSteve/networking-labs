# SAN and DAS - Concepts and Applications

- Filename: `SAN and DAS - Concepts and Applications.pptx`
- Subject: `systems`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/SAN%20and%20DAS%20-%20Concepts%20and%20Applications.pptx)

## Summary

This reusable lecture deck covers enterprise storage concepts with the main goal of helping learners understand Direct-Attached Storage (DAS) versus Storage Area Networks (SANs) and the storage mechanics underneath both. It starts with storage fundamentals such as character devices versus block devices, file storage versus block storage versus object storage, and the meaning of sectors, blocks, clusters, and cylinders. It then uses those foundations to explain why block and cluster size affect I/O efficiency, slack space, and performance differently on HDDs and SSDs. From there it defines DAS as simple local storage attached directly to one machine and SAN as a high-speed shared storage network for multiple servers, then compares them on connectivity, scalability, performance, and cost.

## Key Details

- Opens with a storage primer that distinguishes character devices from block devices.
- Compares file storage, block storage, and object storage with their typical use cases.
- Explains storage anatomy terms such as sector, block, cluster, and cylinder.
- Reinforces how block size and cluster size affect efficiency, slack space, fragmentation, metadata overhead, and workload performance.
- Includes media-specific discussion of HDDs versus SSDs.
- Defines DAS as storage attached directly to a server or workstation.
- Defines SAN as a high-speed shared storage fabric for multiple servers.
- Compares DAS and SAN on connectivity, scalability, performance, and cost.
- Covers thin provisioning in detail, including over-provisioning risk and monitoring requirements.
- Explains snapshots using copy-on-write behavior and ties them to retention and capacity planning.
- Teaches deduplication, block-level replication, synchronous versus asynchronous replication, and tiered storage.
- Compares SATA, SCSI, and SAS, then covers NAND types, endurance tradeoffs, and write-through versus write-back cache policy.

## Tags

- `san`
- `das`
- `block-storage`
- `thin-provisioning`
- `snapshots`
- `replication`
- `tiered-storage`
- `raid`
