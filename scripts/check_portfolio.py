#!/usr/bin/env python3
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[
    ROOT/"index.html",
    ROOT/"assets"/"portfolio.css",
    ROOT/"assets"/"portfolio.js",
    ROOT/"data"/"repositories.json",
]
missing=[str(p.relative_to(ROOT)) for p in REQUIRED if not p.exists()]
if missing:
    print(json.dumps({"ok":False,"error":"missing_files","files":missing},ensure_ascii=False))
    raise SystemExit(1)

data=json.loads((ROOT/"data"/"repositories.json").read_text(encoding="utf-8"))
repos=data["repositories"]
index=(ROOT/"index.html").read_text(encoding="utf-8").lower()
for stale in (">59 repositories<",">60 repositories<"):
    if stale in index:
        print(json.dumps({"ok":False,"error":"hardcoded_repository_total","value":stale}))
        raise SystemExit(1)

cp=subprocess.run([sys.executable,"-m","unittest","discover","-s","tests","-v"],cwd=ROOT)
if cp.returncode:
    raise SystemExit(cp.returncode)

summary={
    "ok":True,
    "repositories":len(repos),
    "public":sum(r["visibility"]=="public" for r in repos),
    "private":sum(r["visibility"]=="private" for r in repos),
    "lifecycle":{},
}
for r in repos:
    summary["lifecycle"][r["lifecycle"]]=summary["lifecycle"].get(r["lifecycle"],0)+1
print(json.dumps(summary,ensure_ascii=False,sort_keys=True))
