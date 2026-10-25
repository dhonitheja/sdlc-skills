#!/usr/bin/env python3
"""Compare Python imports with declared dependencies.

Usage: check_deps.py [project_dir] [--requirements FILE]

Output:
  UNDECLARED  imported but not in the requirements file. A real defect: a clean
              install will fail. Exit code 1.
  CANDIDATE   declared but never imported. Only a candidate for review: dynamic
              imports, plugins, CLI tools, build tools and extras are invisible
              to static analysis. Never delete on this evidence alone.

Static analysis only. It does not run the code or install anything.
"""
import ast, os, re, sys

# import name -> distribution name, where they differ
ALIASES = {"yaml": "pyyaml", "PIL": "pillow", "cv2": "opencv-python", "sklearn": "scikit-learn",
           "bs4": "beautifulsoup4", "dateutil": "python-dateutil", "dotenv": "python-dotenv",
           "jwt": "pyjwt", "OpenSSL": "pyopenssl", "attr": "attrs", "serial": "pyserial",
           "google": "protobuf", "psycopg2": "psycopg2-binary", "Crypto": "pycryptodome"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "env", "build", "dist", ".tox"}

def norm(n):
    return re.sub(r"[-_.]+", "-", n).lower()

def parse_requirements(path):
    names = set()
    for line in open(path, encoding="utf-8"):
        line = line.split("#", 1)[0].strip()
        if not line or line.startswith(("-", "git+", "http")):
            continue
        m = re.match(r"([A-Za-z0-9_.\-]+)", line)
        if m:
            names.add(norm(m.group(1)))
    return names

def local_modules(root):
    """Top-level names that resolve inside the project (files, packages, service dirs)."""
    local = set()
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for f in fns:
            if f.endswith(".py"):
                local.add(f[:-3])
        for d in dns:
            local.add(d)
    return local

def imports(root):
    found = {}
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for f in fns:
            if not f.endswith(".py"):
                continue
            p = os.path.join(dp, f)
            try:
                tree = ast.parse(open(p, encoding="utf-8").read())
            except (SyntaxError, UnicodeDecodeError) as e:
                print(f"WARNING cannot parse {p}: {e}", file=sys.stderr)
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    mods = [a.name.split(".")[0] for a in node.names]
                elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                    mods = [node.module.split(".")[0]]
                else:
                    continue
                for m in mods:
                    found.setdefault(m, set()).add(os.path.relpath(p, root))
    return found

def main():
    args = sys.argv[1:]
    req = None
    if "--requirements" in args:
        i = args.index("--requirements"); req = args[i + 1]; del args[i:i + 2]
    root = args[0] if args else "."
    req = req or os.path.join(root, "requirements.txt")
    if not os.path.isfile(req):
        print(f"No requirements file at {req}. Pass --requirements FILE.")
        return 2
    declared = parse_requirements(req)
    local = local_modules(root)
    stdlib = set(sys.stdlib_module_names)
    used = imports(root)
    undeclared, used_dists = {}, set()
    for mod, files in sorted(used.items()):
        if mod in stdlib or mod in local or mod == "__future__":
            continue
        dist = norm(ALIASES.get(mod, mod))
        used_dists.add(dist)
        if dist not in declared:
            undeclared[mod] = sorted(files)
    unused = sorted(d for d in declared if d not in used_dists)
    for mod, files in undeclared.items():
        print(f"UNDECLARED  {mod}  (imported in {', '.join(files)}; not in {os.path.basename(req)})")
    for d in unused:
        print(f"CANDIDATE   {d}  (declared, no static import found; review before removing)")
    if not undeclared and not unused:
        print("OK  imports and declarations agree (static check only)")
    return 1 if undeclared else 0

if __name__ == "__main__":
    sys.exit(main())
