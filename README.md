# Stacks-and-Trees
A Python CLI tool I built to practice Stacks and Trees. It demonstrates how text editors use stacks for undo/redo actions and how file systems use trees to organize files.

# Data Structures CLI Utility

A simple Python command-line tool I wrote to see how Data Structures work in real applications, rather than just on a whiteboard. I focused on Stacks and Trees for this project.

## What It Does

1. **Text Editor History (Stacks):** 
   I built an Undo/Redo manager using a dual-stack setup (two Python lists). It mimics how a text editor tracks user typing history.
   
2. **File System & Search (Trees):** 
   I modeled a folder directory using an N-ary tree where folders can hold files or other folders. I also wrote a recursive Depth-First Search (DFS) function to quickly find files by name.

## How to Run It

You don't need any special libraries. Just download the file and run it in your terminal:

```bash
python ds_utility.py
