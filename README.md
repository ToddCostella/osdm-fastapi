# Introduction to FastAPI

This project is an example application demonstrating the use of FastAPI for building web APIs. It includes a simple user service with a database for storing user data.

## Introduction

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. This project provides an introduction to FastAPI, showcasing its capabilities through a user service application.

## Features

- FastAPI framework for building APIs
- SQLModel for database models
- SQLite database for storage
- Example endpoints for user operations

## Project Structure


- `Introduction to FAST API - Slides.pdf`: Slides used for the introduction session on FastAPI.
- `main.py`: The main entry point for the FastAPI application.
- `models.py`: Contains the SQLModel definitions for database models.
- `pyproject.toml`: Configuration file for the project dependencies.
- `test.db`: SQLite database file for storing user data.
- `user_service.py`: Contains the implementation of the user service.

## Setup

To set up the project locally using Poetry, follow these steps:

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_name>
    ```

2. Install Poetry if you haven't already:
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Install the project dependencies:
    ```sh
    poetry install
    ```

4. Activate the virtual environment:
    ```sh
    poetry shell
    ```


**Note: Depending on your operating system, you may need to install SqlLite3** 


## Usage

To run the FastAPI application, execute the following command:

```sh
uvicorn main:app --reload
```

Open a browser and navigate to

http://127.0.0.1:8000/docs