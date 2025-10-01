# distutils: language = c
# cython: boundscheck=False, wraparound=False, cdivision=True
from typing import List

def publish_event(list handlers, object event):
    cdef int i, n = len(handlers)
    for i in range(n):
        handlers[i](event)

def publish_batch(list handlers, list events):
    cdef int i, n = len(events)
    for i in range(n):
        publish_event(handlers, events[i])
