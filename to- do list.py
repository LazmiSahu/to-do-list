# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 22:46:06 2025

@author: hp
"""

tasks = []
def add_task():
    task = input("enter a new task : ")
    tasks.append(task)
    print("task Added Successful")
def view_task():
    if not tasks:
        print("No tasks available")
    else:
        print("your To-Do List is here: ")
        for i, task in enumerate(tasks,1):
            print(i,task)
def delete_task():
    view_task()  # Show tasks before deleting
    try:
        task_num = int(input("Enter task number to delete: ")) - 1  # Convert to zero-based index
        if 0 <= task_num < len(tasks):  # Check if input is valid
            removed_task = tasks.pop(task_num)  # Remove task from list
            print("Deleted:", removed_task)
        else:
            print("Invalid task number!")  
    except ValueError:
        print("Please enter a valid number!") 
while True:
    print("---TO-DO List---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4.Exit")
    choice = input("Enter Choice : ")

    if choice=="1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
        delete_task()
    elif choice=="4":
        print("bye")
        break
    else:
        print("Invalid choice! \n Please try again")
    