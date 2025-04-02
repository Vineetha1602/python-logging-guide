# Python Logging Example

This project is based on the YouTube tutorial on Python logging: [Python Logging - Logging Basics](https://www.youtube.com/watch?v=jxmzY9soFXg). It demonstrates how to properly implement logging in Python applications.

<!------------------>

## Features

- Uses Python's built-in logging module

- Demonstrates different logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)

- Configures logging format and handlers

- Writes logs to both console and a file

## Requirements

Python 3.x

## Installation

No external dependencies are required. Simply clone this repository and run the script.

```bash
$ git clone <repository-url>
$ cd <repository-folder>
$ python intro_to_logging.ipynb
```

<!------------------>

## Usage

The script initializes a logger and writes logs of different levels to both the console and a log file (app.log).

Modify the log level or format as needed by editing the _logger or logging.basicConfig()_ settings in the script.

## Example Output

```bash
2024-04-02 12:00:00,123 - INFO - This is an info message
2024-04-02 12:00:00,124 - WARNING - This is a warning message
2024-04-02 12:00:00,125 - ERROR - This is an error message
2024-04-02 12:00:00,126 - CRITICAL - This is a critical message
```

<!------------------>
