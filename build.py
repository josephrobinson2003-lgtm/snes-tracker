#!/usr/bin/env python3
"""Rebuild index.html + sw.js from games.json. Run: python3 build.py"""
import json, hashlib, pathlib
d = pathlib.Path(__file__).parent
games = json.loads((d/"games.json").read_text())
data = json.dumps([{"title": g["title"].strip(), "owned": bool(g["owned"])} for g in games if g["title"].strip()], ensure_ascii=False, separators=(",", ":"))
tpl = (d/"template.html").read_text()
ver = hashlib.sha1((data + tpl + (d/"sw.template.js").read_text()).encode()).hexdigest()[:10]
v1 = (d/"owned-v1-baseline.json").read_text().strip()  # v1.0 defaults, used once to migrate old saved lists
(d/"index.html").write_text(tpl.replace("__DATA__", data).replace("__V1__", v1).replace("__VER__", ver))
(d/"sw.js").write_text((d/"sw.template.js").read_text().replace("__VER__", ver))
(d/"manifest.json").write_text(json.dumps({"name":"SNES Collection Tracker","short_name":"SNES Tracker","start_url":"./","scope":"./","display":"standalone","background_color":"#14151f","theme_color":"#14151f","icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png"},{"src":"icon.svg","sizes":"any","type":"image/svg+xml"}]}, indent=1))
print("built version", ver, "games", len(games), "owned", sum(g["owned"] for g in games))
