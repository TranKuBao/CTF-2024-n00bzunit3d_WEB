from flask import Flask, request, redirect, render_template, render_template_string
import tarfile
from hashlib import sha256
import os

xxx='1234567890'
print(sha256(os.urandom(16)).digest().hex())