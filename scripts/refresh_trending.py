#!/usr/bin/env python3
"""Scrape Scirate's top-scited arXiv papers per time window and write a
trending.json snapshot for the Scholar Trends site.

Run locally or by the daily GitHub Action (.github/workflows/refresh-trending.yml).
Composite score per keyword (0-100) blends, 50/50, the normalized paper count and
the normalized total Scirate scites — i.e. a topic ranks high only when it has both
many recent papers AND strong community upvotes.
"""
import urllib.request, re, html, collections, json, datetime

WINDOWS = [("today", 1, 2), ("week", 7, 2), ("month", 30, 2), ("year", 365, 2)]
STOP = set((
    "the of for and to in on with via using from at is are we our new a an as by that this can be it its "
    "their towards toward between over under into more most general scite scites comment comments abstract "
    "quantum-ph results result approach method methods model models study"
).split())


def scrape(rng):
    req = urllib.request.Request(
        "https://scirate.com/?range=%d" % rng,
        headers={"User-Agent": "Mozilla/5.0 (scholar-trends refresh)"},
    )
    h = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "ignore")
    # (id, scites) come paired inside the scites-count block — authoritative.
    pairs = re.findall(r'/arxiv/(\d{4}\.\d{4,5})/scites"[^>]*>\s*<button[^>]*>(\d+)', h)
    # title map: first non-"N comments" text per id (title precedes the comments link).
    tmap = {}
    for aid, txt in re.findall(r'href="/arxiv/(\d{4}\.\d{4,5})"[^>]*>\s*([^<]{4,}?)\s*</a>', h):
        t = html.unescape(txt.strip())
        if aid in tmap or re.match(r"^\d+\s+comments?$", t, re.I) or t.lower() in ("scite!", "abstract"):
            continue
        tmap[aid] = t
    papers = [{"id": a, "scites": int(s), "title": tmap.get(a, "")} for a, s in pairs if tmap.get(a)]
    papers.sort(key=lambda p: -p["scites"])
    return papers


def keywords(papers, minp, top=8):
    # Phrase (bigram) extraction: single words split multi-word topics
    # ("error"+"correction") and let trivial words ("quantum") dominate.
    bg = collections.defaultdict(lambda: [0, 0])
    for p in papers:
        toks = [w for w in re.findall(r"[a-z][a-z\-]{2,}", p["title"].lower()) if w not in STOP]
        seen = set()
        for i in range(len(toks) - 1):
            phrase = toks[i] + " " + toks[i + 1]
            if phrase in seen:  # count each phrase once per paper
                continue
            seen.add(phrase)
            bg[phrase][0] += 1
            bg[phrase][1] += p["scites"]
    rows = [{"word": w, "papers": n, "scites": s} for w, (n, s) in bg.items() if n >= minp]
    if not rows:
        return []
    mn = max(r["papers"] for r in rows) or 1
    ms = max(r["scites"] for r in rows) or 1
    for r in rows:
        r["score"] = round(50 * r["papers"] / mn + 50 * r["scites"] / ms)
    rows.sort(key=lambda r: r["score"], reverse=True)
    return rows[:top]


def main():
    out = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%MZ"), "source": "scirate.com", "windows": {}}
    for name, rng, minp in WINDOWS:
        try:
            P = scrape(rng)
            out["windows"][name] = {
                "papers": [{"id": p["id"], "title": p["title"], "scites": p["scites"]} for p in P[:10]],
                "keywords": keywords(P, minp),
            }
        except Exception as exc:  # keep other windows even if one fails
            out["windows"][name] = {"papers": [], "keywords": [], "error": str(exc)[:100]}
    with open("trending.json", "w") as f:
        json.dump(out, f, indent=1)
    print("wrote trending.json", {k: len(v.get("papers", [])) for k, v in out["windows"].items()})


if __name__ == "__main__":
    main()
