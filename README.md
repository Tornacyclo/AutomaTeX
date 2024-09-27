# AutomaTeX

AutomaTeX is a Python script designed to automate the generation and customization of LaTeX documents. Given a list of names, cities, and languages from an input file, it creates personalized LaTeX files, modifies them with specific details, and compiles them using XeLaTeX, MakeIndex, and BibTeX.

## Features

- Automatically creates folders for each person and city.
- Copies template LaTeX files based on the specified language (English or French).
- Replaces placeholders with user-defined values (e.g., person and city).
- Compiles the `.tex` files into PDF format using `XeLaTeX`, `MakeIndex`, and `BibTeX`.

## File Structure

The script processes the input file and generates a folder structure based on the provided data. Example output:

```
.
├───Apolline_Copenhagen
├───Marmiton_Delémont
└───Salhi_Neuchâtel
```

Each folder will contain the generated LaTeX files for that specific person and city.

## Requirements

- Python 3.x
- `texify` installed on the system (XeLaTeX, MakeIndex, and BibTeX are required for compilation).

## Script Overview

### `AutomaTeX.py`

The script reads from an input file and performs the following operations:

1. **Sanitize Folder Names**: Ensures folder names are valid by replacing invalid characters.
2. **Create Folders**: A new folder is created for each test case, named after the person and city.
3. **Copy Files**: LaTeX templates (EN.tex or FR.tex) are copied to the new folder based on the selected language (English or French).
4. **Modify LaTeX Files**: Custom placeholders like city and person name are replaced in the LaTeX template.
5. **Compile LaTeX Files**: The LaTeX files are compiled into PDFs using `XeLaTeX`, `MakeIndex`, and `BibTeX`.

### Input

The input is read from a file in the following format:

```plaintext
T
N1 C1 L1
N2 C2 L2
...
Nx Cx Lx
```

Where:
- The first line is the number of test cases T.
- Each subsequent line consists of the person's name N, city C, and language L (either `EN` or `FR`).

### Example Input

```
3
Apolline Copenhagen EN
Salhi Neuchâtel FR
Marmiton Delémont FR
```

### Example Execution

To execute the script with an input file:

#### Windows:
```bash
Get-Content .\input.txt | python AutomaTeX.py
```

#### Linux/Mac:
```bash
python3 AutomaTeX.py < input.txt
```
