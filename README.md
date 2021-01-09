

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

First, copy the project files into a folder and, in the terminal go to this folder. Then, you have two options to get started, since the project requires Python 3.6 and a few libraries you may not have on your machine. Follow one of the following:

#### 1. Local code environment
Assumption you already have Python 3 on your machine, if not please install.
-   Install virtualenv (if needed) :
    `pip3 install virtualenv`
-   from the project root folder, create environment
    `virtualenv header_extractor`
-  activate the environment
    `source header_extractor/bin/activate`
-   install the necessary packages
    `pip install -r requirements.txt`
-   make environment available to jupyter notebook
    `python -m ipykernel install --user --name=header_extractor`

#### 2. Docker
Install docker on your machine, if not already installed.
- create the image
 `docker build -t thoughtriver .`
- run a container in interactive mode.
`docker run -it -v HOST_DOCUMENTS_PATH:/LOCAL_DOCUMENTS_PATH thoughtriver`
where `HOST_DOCUMENTS_PATH` is the folder where the documents to be processed are. Since the container needs access to this folder, the folder needs to be mounted to the container volume.  In practice `HOST_DOCUMENTS_PATH` and `LOCAL_DOCUMENTS_PATH` could have the same name.

If access to the notebooks is required, then start a container with port forward
`docker run -it  -p 8888:8888 thoughtriver`
once inside the container execute
`jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser --allow-root`
which confirm that jupyter server has started and show the token. the output will look similar to this:
`http://127.0.0.1:8888/?token=SOME_LONG_STRING`
you should be able to access it now in your browser

## Usage
To use the CLI, issue a command to the `src/main.py` file in the project.
- If using the code environment setup:
`python3 src/main.py --input_file INPUT_FILE_PATH` from the project folder or
`python3 PATH_TO_PROJECT/header_extractor/src/main.py --input_file INPUT_FILE_PATH` from outside the folder.

- If using the Docker setup:
inside the **Docker console**
`python3 src/main.py -if LOCAL_DOCUMENTS_PATH/FILE.json`

#### mandatory parameters:
- `-if/--input_file` path to the file to process.
#### optional parameters:
- `-p/--parser` select between a `regex` or `jaccard` parsing strategy, defaults to `regex`.
- `-ot/--output_type` select to output `index` or `text` of headers, defaults to `index`.

### Sample file
This option exists in case the directory with documents is not made available to either Docker or the local project environment. In this case the mandatory `input_file` attribute is not required, and instead the `document-headers/files/letter.json` file is used. The other parameters remain unchanged.

#### A few example commands
`python3 src/sample.py -p jaccard`
`python3 src/sample.py -p jaccard -ot text`
`python3 src/sample.py -ot text`