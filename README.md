# ThoughtRiver take-home assignment

As part of this assignment there's a data injestion part, as well as a visualisation.

This is the folder structure:
--------------------------------

    ┌── README.md
    │
    ├── notebooks
    │  └── Playground              <- As the name says, just to keep track and have the spaguetti in one place.
    │
    ├── document-headers           <- Task files as sent from TR
    │
    ├── src                        <- code for the CLI.
    │  ├── extract.py              <- Entry point for the script, what gets called when using the CLI.
    │  └── utils.py                <- utility functions file used across the project
    │
    ├── header_extractor           <- Code env for the project.
    │
    └── requirements.txt           <- The requirements file for reproducing the environment environment.


## CLI
In order to use the cli issue the following command, use the following example script and replace:

- YOUR_FOLDER_NAME with the location where the repo has been downloaded.
- INPUT_FILE_PATH path to the file parsed
- OUTPUT_FILE_PATH path to store the results after parsing

```python3 YOUR_FOLDER_NAME/src/extract.py --input_file INPUT_FILE_PATH --output_file OUTPUT_FILE_PATH```