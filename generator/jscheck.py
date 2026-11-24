"""python3 jscheck.py v3  → scoate scriptul paginii în /tmp și îl verifică de sintaxă cu node"""
import sys, subprocess
n = sys.argv[1]
h = open(f"{n}.html", encoding="utf-8").read()
open(f"/tmp/{n}.js", "w", encoding="utf-8").write(h[h.rindex("<script>") + 8:h.rindex("</script>")])
r = subprocess.run(["node", "--check", f"/tmp/{n}.js"], capture_output=True, text=True)
print(n, "syntax OK" if r.returncode == 0 else r.stderr[:600]); sys.exit(r.returncode)
