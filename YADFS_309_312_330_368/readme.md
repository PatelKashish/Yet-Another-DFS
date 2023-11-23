# YADFS (Yet Another Distributed File System)

## Overview

YADFS is a Python script that introduces a simplified Distributed File System (DFS) with comprehensive functionalities including file management, replication, and synchronization between Name Nodes and Data Nodes. This system empowers users with operations such as putting, removing, listing, and displaying files, along with advanced features like DFS formatting and directory structure management. Leveraging multiprocessing and synchronization mechanisms, YADFS ensures efficient and reliable DFS management.

## Setup

Setting up YADFS is a straightforward process:

1. Install the dependencies.
    ```bash
    pip3 install -r requirements.txt
    ```

2. Run the following command to configure and clean up the DFS:
   ```bash
   python setup.py --CONFIG config\dfs_setup.json --CLEANUP True
   ```

3. Start the DFS with the configured setup:
   ```bash
   python YADFS.py --CONFIG config\dfs_setup.json
   ```

## Commands Syntax

Understanding YADFS commands involves mapping intuitive syntax to their corresponding functionalities:

- `load` -> `put`
- `del` -> `rm`
- `create` -> `mkdir`
- `destroy` -> `rmdir`
- `list` -> `ls`
- `show` -> `cat`
- `retrieve` -> `download`
- `move` -> `mv`
- `copy` -> `cp`
- `clean` -> `format_namenode_datanode`

## Commands Explanation

Explore the versatility of YADFS through the following command explanations:

1. **Move a File:**
   ```bash
   (yadfs_309_312_330_368) > move /root/trail.txt trial.txt
   ```

2. **Delete a File:**
   ```bash
   (yadfs_309_312_330_368) > del trial.txt
   ```

3. **Destroy a Directory:**
   ```bash
   (yadfs_309_312_330_368) > destroy root
   ```

4. **List Files:**
   ```bash
   (yadfs_309_312_330_368) > list
   ```

5. **Clean DFS:**
   ```bash
   (yadfs_309_312_330_368) > clean
   ```

6. **Create Directory:**
   ```bash
   (yadfs_309_312_330_368) > create root
   ```

7. **List Contents of Directory:**
   ```bash
   (yadfs_309_312_330_368) > list
   ```

8. **Load a Text File:**
   ```bash
   (yadfs_309_312_330_368) > load content.txt /root/sample.txt
   ```

9. **List Contents of Directory Recursively:**
   ```bash
   (yadfs_309_312_330_368) > list root -r
   ```

10. **Show Contents of a File:**
    ```bash
    (yadfs_309_312_330_368) > show /root/sample.txt
    ```
