# Uniflow

Uniflow is a robust ETL library designed for the NUDA team at Unimed SC.

## Content Table
- [Uniflow](#uniflow)
  - [Content Table](#content-table)
  - [Instalation](#instalation)
    - [Pre-requisites](#pre-requisites)
  - [Usage](#usage)
  - [Functionalities](#functionalities)
  - [Project Structure](#project-structure)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)

## Instalation

### Pre-requisites

Make sure to follow the next steps in order to get the project up and running. 

```bash
# Create a virtual enviroment session
poetry shell
```

```bash
# Install all dependencies
poetry install
```

## Usage

```bash
# Adding new dependencies
# `--group` dev specifies that the packages you're installing are gonna be in the development group
poetry add requests pendulum --group dev
```

```bash
# You can also create new groups to install the project dependencies
poetry add requests --group http
poetry add pendulum --group time_utils
```

## Functionalities

- [ ] Text Utils
  - [ ] Normalize
  - [ ] Split
  - [ ] Concatenate
  - [ ] Find & Count
  - [ ] Lower
  - [ ] Upper
  - [ ] Trim
  - [ ] Format
  - [ ] Convert Data Type
  - [ ] Duplicates
  - [ ] Null
  - [ ] Replace

- [ ] Script Generation
  - [ ] Select
  - [ ] Truncate
  - [ ] Delete
  - [ ] Drop
  - [ ] Create
  - [ ] Insert
  - [ ] Alter Table
  - [ ] Update

- [ ] Database Manipulation
  - [ ] Execute Script
  - [ ] Connection (Local and Airflow)

- [ ] File & Directory Management
  - [ ] Read Content (File)
  - [ ] Create (File)
  - [ ] Remove (File)
  - [ ] Move (File)
  - [ ] Rename (File)
  - [ ] List Files Inside (Directory)
  - [ ] Create (Directory)
  - [ ] Remove (Directory)
  - [ ] File Format Conversion

- [ ] Time Tracking Uitls
  - [ ] Start Track
  - [ ] Stop Track
  - [ ] Set Timeout

- [ ] Dataframe Utils
  - [ ] Merge Dataframe
  - [ ] Dataframe to SQL
  - [ ] Aggregations
  - [ ] Filter

- [ ] Logging
  - [ ] Log Step
  - [ ] Generate Reports

- [ ] Data Validation
  - [ ] Schema Validation (Right Collumns Type, Expected Values)
  - [ ] Data Profiling (Identify Duplicates, Missing Values, Outliers)

## Project Structure
/uniflow</br>
│</br>
├── /dist             # Package</br>
├── /tests            # Tests</br>
├── /uniflow          # Source code</br>
├── poetry.lock</br>
├── pyproject.toml    # Project dependencies</br>
└── README.md         # Documentation</br>

## Technologies Used

- python 3.x
- poetry
- taskipy
- pandas
- oracledb
- ydata-profiling  <!-- validate -->

## Testing

Description here

```python
# Not implemented yet
tasks test
```
