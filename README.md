# DISARM Add-In for Word Server Application

## Overview
This repository contains the code for the server-side of the DISARM Add-In for Word hosted on the **main** branch.



### Prerequisites
- Python installed on your system
- `pip` package manager available
- `openpyxl` installed (`pip install openpyxl`)

### Steps to update the framework:
To update the framework, run the two Python scripts located in the `python-scripts` branch. These scripts  process the data from the `DISARM_FRAMEWORKS_MASTER.xlsx` file and generate the necessary JSON files on the server-side od the add-in.

1. **Prepare the Input Data**  
   - Clone the repository
   - Make sure you have the latest `DISARM_FRAMEWORKS_MASTER.xlsx` file
   - Place this file in the `python-scripts` branch 

2. **Execute the Python Scripts**  

   - Run the scripts `update-tags-from-framework.py` and `update-techniques-from-framework.py` in the `python-scripts` branch locally
   - This will generate new versions of `tags.json` and `techniques.json` files

3. **Update the Repository**  
   - Replace the `tags.json` and `techniques.json` files with the newly generated versions on the **main** branch
   - Commit and push the updated JSON files to the **main** branch, this will trigger an automatic deploy of the new files to the server
   - Do not merge the branches!



### Contact
For any questions or support, feel free to reach out via email to esma.karahodza@digiqal.de.
