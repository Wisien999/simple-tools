# simple-tools

It's a set of simple tools that i made for myself.

# massive-unzip.py
You can extract all *.zip files in any directory.
```
Syntax: python massive-unzip.py <source directory> <destination directory>
        python massive-unzip.py <source directory> - extract to the same directory
        python massive-unzip.py - extract form current directory to the same directory
        ```

# new-project/new-project.py
Create new coding project (for VS Code). Works only with c++ for now.

# pdf-shrinker.py
Shrinks the given PDF file by removing pages that are 'contained' by the next page.
*INFO:* requires PyPDF4
```
Syntax: python pdf-shrinker.py [path to .pdf file]...
```
