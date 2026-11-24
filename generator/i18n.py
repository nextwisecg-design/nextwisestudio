"""Traducere la nivel de HTML: fiecare nod de text (și aria-label/alt/content) e căutat într-un dicționar RO→EN.
Nimic nu se traduce parțial; ce lipsește din dicționar e raportat, ca să nu rămână română în pagina engleză."""
import re

TAG = re.compile(r"(<[^>]+>)")
ATTR = re.compile(r'\b(aria-label|alt|content|title)="([^"]*)"')
KEEP = re.compile(r"^[\s\d\W_]*$")  # doar cifre, semne, spații


def nodes(html):
    """Întoarce lista (index, text) a nodurilor de text din afara <script>/<style>."""
    parts, out, skip = TAG.split(html), [], None
    for i, part in enumerate(parts):
        if i % 2:  # tag
            low = part.lower()
            if skip and low.startswith("</" + skip):
                skip = None
            elif not skip and (low.startswith("<script") or low.startswith("<style")):
                skip = "script" if low.startswith("<script") else "style"
        elif not skip and part.strip():
            out.append((i, part))
    return parts, out


def strings(html, same=()):
    parts, ns = nodes(html)
    seen = []
    for _, t in ns:
        k = " ".join(t.split())
        if k not in seen and not KEEP.match(k) and k not in same:
            seen.append(k)
    for part in parts[1::2]:
        for _, v in ATTR.findall(part):
            if v and not KEEP.match(v) and v not in seen and v not in same and not v.startswith(("width=", "text/")):
                seen.append(v)
    return seen


def translate(html, D, same=()):
    parts, ns = nodes(html)
    missing = []
    for i, t in ns:
        k = " ".join(t.split())
        if KEEP.match(k) or k in same:
            continue
        if k in D:
            lead, trail = t[:len(t) - len(t.lstrip())], t[len(t.rstrip()):]
            parts[i] = lead + D[k] + trail
        else:
            missing.append(k)

    def attr(m):
        v = m.group(2)
        if v in D:
            return f'{m.group(1)}="{D[v]}"'
        if v and not KEEP.match(v) and v not in same and not v.startswith(("width=", "text/")):
            missing.append("@" + v)
        return m.group(0)
    for i in range(1, len(parts), 2):
        if parts[i].startswith("<") and not parts[i].startswith("<!"):
            parts[i] = ATTR.sub(attr, parts[i])
    return "".join(parts), missing
