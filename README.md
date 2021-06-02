# Project 2: Meme Generator
This repository contains the second and final project of the [Intermediate Python Nanodegree Program](https://www.udacity.com/course/intermediate-python-nanodegree--nd303), by Udacity.

The goal of this project is to build a "meme generator" in Python: a multimedia application to dynamically generate memes, including an image with an overlaid quote.

The purpose of this work is to show the acquired skills in:

* Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
* DRY (don’t repeat yourself) principles of class and method design.
* Working with modules and packages in Python.

## The Application
The application shown in this repository performs the following actions:

* Interacting with a variety of complex filetypes.
* Loading quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
* Loading, manipulating, and saving images.
* Accepting dynamic user input through a command-line tool and a web service.

## Quote Engine module
The **Quote Engine** module is responsible for ingesting many types of files that contain quotes. 
A quote contains a body and an author: ' "This is a quote body" - Author '.

This module is composed of many classes and demonstrate a solid understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.
It realizes classes for parsing inputs file of several formats (txt, pdf, docx, csv).

## Meme Engine module
The **Meme Engine** module is responsible for manipulating and drawing text onto images. 
It demonstrates concrete understanding of object-oriented thinking while using a more advanced third party library for image manipulation (Pillow).

This module is used for the following actions:

* Loading of a file from disk
* Transform image by resizing to a maximum width of 500px while maintaining the input aspect ratio
* Add a caption to an image (string input) with a body and author to a random location on the image.

## Setting up and running the Application
This repository comes with a "requirements.txt" file that includes all nessesary lirbraries and dependencies.

The first step is:
```
pip install -r requirements.txt
```
And than run the command:
```
python app.py
```
A local html page with the address `http://127.0.0.1:5000/` allows you to interact with the application.