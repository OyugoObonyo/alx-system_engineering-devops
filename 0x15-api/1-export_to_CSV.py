#!/usr/bin/python3
"""Obtains info from json placeholder api and returns it in CSV format"""
import csv
import requests
import sys


def getInformation(employeeid):
    """Returns information based on ID"""
    url = "https://jsonplaceholder.typicode.com/"
    endpoint = url + 'users/{}'.format(employeeid)
    employee = requests.get(endpoint).json()
    taskendpoint = url + 'TODOs?userId={}'.format(employee.get('id'))
    tasks = requests.get(taskendpoint).json()
    data = {"employee": employee, "tasks": tasks}
    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        _username = data['employee']['username']
        _id = data['employee']['id']
        for task in data['tasks']:
            w.writerow([_id, _username, task['completed'], task['title']])


if __name__ == '__main__':
    getInformation(sys.argv[1])
