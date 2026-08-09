import sys
from pathlib import Path

command = sys.argv[1]

if command == "init":
    versions = Path(".VersiOns")
    objects = versions / "objects"
    commits = versions / "commits"
    branches = versions / "branches"
    branches_point = versions / "branches" / "main"
    head = versions / "HEAD"

    
    
    if(versions.exists()):
        print("Repositório ja criado")
    else:
        versions.mkdir()
        objects.mkdir()
        commits.mkdir()
        branches.mkdir()
        branches_point.write_text("")
        head.write_text("main")
        print("Versions repository initialized!")
        
    