# Student Management System

## Overview

The Student Management System is a web application designed to streamline and manage information related to students, courses, and their results. It provides a set of RESTful APIs for performing various operations such as adding students, managing courses, and recording results.

## Table of Contents

- [Features](#features)
- [Endpoints](#endpoints)
- [Usage](#usage)
- [Authentication](#authentication)
- [API Reference](#api-reference)
- [Unit Testing](#unit-testing)

## Features

### 1. Student Module
- Add a student
- Find a student by roll number
- View all students' details
- Update a student's details
- Delete a student

### 2. Course Module
- Add a course
- Find a course by course ID
- View all courses' details
- Update a course's details
- Delete a course

### 3. Result Module
- Add a result
- Find a result by roll number
- View all results
- Update a result
- Delete a result

## Endpoints

- `/courses`
- `/courses/{course_id}`
- `/registrations`
- `/registrations/{roll_no}`
- `/students`
- `/students/{roll_no}`
- `/register`
- `/login`
- `/logout`
- `/refresh`

## Usage

To use the Student Management System refer to the API Reference section for details on each endpoint.

## Authentication

Authentication is required for certain endpoints. Use the /register, /login, /logout, and /refresh endpoints for authentication and managing user sessions.

## API Reference

Detailed API documentation is available in the [API Reference](path/to/your/API_REFERENCE.md) file.

## Unit Testing

1. To run the tests
```
coverage run -m unittest
```

2. To get the coverage report
```
coverage report -m
```

3. To run the tests in quiet mode
```
coverage run -m unittest -b
```
