---
layout: post
title: "Time Machine, Core Storage and Disk Utility"
date: 2016-01-02
---

Time Machine is a wonderful tool. I remember how impressed I was when I first discovered this tool, built-in on my Mac. Finally I could rest assured that with a high probability my data will never get lost by a hard disk crash or an accidental erasure. Many times it has saved my works when I was playing a bit too far with my machine ..

Still today, I am using a pair of cheap hard disk in order to backup my work regulary. Especially I make sure to have a recent backup before doing a system upgrade. Then, once the new operating system is tested and working well, I erase the backup disk and start over with a fresh disk.

For this task, I am using a cheap USB hard disk (50 €) that is partitionned in 3 partitions. One of them is a HFS+ partition (required because Time Machine is using hard links to save space).
For security, every partition is encrypted by Filevault in a CoreStorage volume. This setup works very well, but it is not supported by the Disk Utility GUI.

The error message says :

Disk Utility - Unsupported Configuration detected

A CoreStorage logical volume group with more than one logical volume has been detected. The Disk Utility GUI does not support full CoreStorage editing. To use Disk Utility use diskutil to revert to single logical volume per logical volume group.

<img src="/images/Disk Utility - Unsupported Configuration detected.png" width="100%" 
 alt="Disk Utility - Unsupported Configuration detected"/>

The solution to this problem is to use the `diskutil` command line tool in order to erase the backup partition.

First, list the partitions :

```console
$ diskutil list

...

/dev/disk2 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *500.1 GB   disk2
   1:                        EFI EFI                     209.7 MB   disk2s1
   2:       Microsoft Basic Data SHARED2                 100.0 GB   disk2s2
   3:          Apple_CoreStorage BACKUP                  399.8 GB   disk2s3
   4:                 Apple_Boot Boot OS X               134.2 MB   disk2s4

/dev/disk3 (external, virtual):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                  Apple_HFS ARCHIVE2               +100.0 GB   disk3
                                 Logical Volume on disk2s3
                                 29E1E2A1-07D5-4751-8C65-BB26C95C3FA4
                                 Unlocked Encrypted

/dev/disk4 (external, virtual):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                  Apple_HFS BACKUP2                +299.4 GB   disk4
                                 Logical Volume on disk2s3
                                 3C90C3C4-72D1-49F4-AAC6-78BC93B702CD
                                 Unlocked Encrypted
```								 

Then reformat the backup partition in order to remove all data. It is very fast, don't worry.

```console
$ diskutil reformat BACKUP2 
Started erase on disk4 BACKUP2
Unmounting disk
Erasing
Initialized /dev/rdisk4 as a 279 GB case-insensitive HFS Plus volume with a 24576k journal
Mounting disk
Finished erase on disk4 BACKUP2
```	

Finally, I can use my new cleaned partition as a new disk for Time Machine !
