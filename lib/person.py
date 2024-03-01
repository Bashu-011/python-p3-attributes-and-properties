#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Bob", job="Legal"):
        self.set_name(name)
        self.set_job(job)

    def set_name(self, name):

        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name.title()


    def set_job(self, job):
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = job

    @property
    def name(self):
        return self._name

    @property
    def job(self):
        return self._job
    
      


