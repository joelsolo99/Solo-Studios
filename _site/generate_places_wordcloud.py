import csv
import math
from collections import Counter

csv_file = "assets/locations/location-wordcloud.csv"
output_md = "_pages/places-wordcloud.md"

front_matter = """---
layout: page
title: "Where We've Played"
permalink: /places/
---
"""


html_intro = """
<link rel="stylesheet" href="/assets/css/wordcloud.css">

<div class="wordcloud-wrapper">
<p>Here are some of our favourite places to perform:</p><section class="wordcloud">
"""
html_end = "</section>\n</div>\n"


html_end = "</section>\n"

with open(csv_file, newline='') as f:
    reader = csv.DictReader(f)
    places = [row['place'].strip() for row in reader if row['place'].strip()]

counts = Counter(places)
max_count = max(counts.values())

def scaled_font_size(count):
    scale = math.sqrt(count) / math.sqrt(max_count)
    size_rem = 0.8 + scale * 4  # 0.8rem to 4.8rem
    return f"{size_rem:.2f}rem"

bg_classes = ['bg1', 'bg2', 'bg3', 'bg4', 'bg5']

spans = []
for i, (place, count) in enumerate(sorted(counts.items(), key=lambda x: x[1], reverse=True)):
    font_size = scaled_font_size(count)
    bg_class = bg_classes[i % len(bg_classes)]
    spans.append(f'  <span class="town {bg_class}" style="font-size: {font_size}; --i: {i}">{place}</span>')

with open(output_md, "w") as f:
    f.write(front_matter)
    f.write(html_intro)
    f.write("\n".join(spans))
    f.write("\n" + html_end)

print(f"\u2705 Word cloud markdown saved to {output_md}")
