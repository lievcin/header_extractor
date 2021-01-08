
# ThoughtRiver take-home assignment:

This project parses and extracts headers from NDA type agreements. It provides a CLI where the user can drop a file and
get the indices (or text) of the headers, as well as select one of two strategies to do so.


This is the folder structure:
--------------------------------

    ┌── README.md
    │
    ├── IDEAS.md                   <- General ideas file created when considering this task, vague to-do list to keep.
    │
    ├── notebooks
    │  ├── Jaccard                 <- experiments with Jaccard(ish) similarity.
    │  │
    │  └── Regex sandbox           <- experiments with regex.
    │
    ├── document-headers           <- Task files as sent from TR
    │
    ├── src                        <- code for the CLI.
    │  ├── config
    │  │   └── config.py           <- schema, jaccard threshold and regex patterns used in the project.
    │  ├── parsers                 <- folder containing different parser classes.
    │  │   ├── base
    │  │   ├── jaccard
    │  │   └── regex
    │  └── main.py                <- entry point for the script, what gets called when using the CLI.
    │
    └── requirements.txt           <- The requirements file for reproducing the code environment.


## Setup
The project requires Python3 and a few libraries and it is therefore recommended that a code environment is created for it.

-   Install virtualenv (if needed) :
    `pip3 install virtualenv`
-   from the project root folder, create environment
    `virtualenv header_extractor`
-  activate the environment
    ` source header_extractor/bin/activate`
-   install the necessary packages
    `pip install -r requirements.txt`

## Usage
In order to use the cli issue the following command, use the following example script from the root folder of the project (or prepending the necessary path):

`python3 src/main.py --input_file INPUT_FILE_PATH`
or
`python3 src/main.py --if INPUT_FILE_PATH`

where INPUT_FILE_PATH is the full path to the JSON file to parse.

#### optional parameters:
- `-p/--parser` select between a `regex` or `jaccard` parsing strategy, defaults to `regex`.
- `-ot/--output_type` select to output `index` or `text` of headers, defaults to `index`.