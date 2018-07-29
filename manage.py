#!/usr/bin/env python3
"""Módulo de administração django."""

import os
import sys

from django.core import management

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teoria.settings')
management.execute_from_command_line(sys.argv)
