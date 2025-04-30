#!/usr/bin/env python3

import sys
import os
import re
from shutil import copyfile
import json
from datetime import datetime
from glob import glob

root_dir = os.path.realpath(os.path.join(__file__, "..", ".."))

with open(os.path.join(root_dir, ".cookiecutter.json")) as fh:
    data = json.load(fh)

talk_slug = data["talk_slug"]
talk_date = datetime.strptime(data["date"], "%Y-%m-%d")
talk_filename = glob(f"{talk_slug}.*")[0]

def parse_version(file):
    m = re.match("^(.*)_v(\d+)\.pdf$", os.path.basename(file))
    assert m is not None
    return int(m.group(2))

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
version_dir = os.path.join(root, "versions")

if not os.path.isdir(version_dir):
    os.makedirs(version_dir)

versions = []
for file in os.listdir(version_dir):
    try:
        versions.append(parse_version(file))
    except AssertionError:
        print(file, "not matched, ignoring")

current_version = 0

if len(versions) > 0:
    current_version = max(versions)

next_version = current_version + 1

print(current_version, "->", next_version)

base, ext = os.path.splitext(talk_filename)

src = os.path.join(root, "build.nosync", "%s.pdf" % (base))
dest = os.path.join(version_dir, "%s_v%d.pdf" % (talk_slug, next_version))

assert os.path.exists(src), "Source pdf file does not exist"
assert not os.path.exists(dest), "Destination version file already exists"

print(src, "->", dest)

copyfile(src, dest)
