# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *
# @leet imports end

# @leet start


class Solution:
    def countCollisions(self, directions: str) -> int:

        stack = []
        collisions = 0

        for curr in directions:
            # Resolve collisions while possible
            while stack:
                last = stack[-1]

                # R + L → 2 collisions, becomes S
                if last == 'R' and curr == 'L':
                    collisions += 2
                    stack.pop()
                    curr = 'S'

                # R + S → 1 collision, becomes S
                elif last == 'R' and curr == 'S':
                    collisions += 1
                    stack.pop()
                    curr = 'S'

                # S + L → 1 collision, becomes S
                elif last == 'S' and curr == 'L':
                    collisions += 1
                    curr = 'S'

                else:
                    break

            stack.append(curr)

        return collisions
        # @leet end
