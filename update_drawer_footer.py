# -*- coding: utf-8 -*-
"""
Precise script to ensure all 3 navigation locations (desktop nav panel, mobile drawer, footer services)
are completely and accurately updated in EVERY HTML file (root files and blog files).
"""

import os
import glob
import re

NEW_SERVICES_DESKTOP = """              <a href="{p}ac-not-working.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">AC Not Working</span>
                  <span class="t6-nav-panel-desc">Emergency troubleshooting for complete system shutdown, breakers, and capacitors.</span>
                </span>
              </a>
              <a href="{p}central-ac-repair.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">Central AC Repair</span>
                  <span class="t6-nav-panel-desc">Complete split-system repair, ECM blower motors, coils, and condensers.</span>
                </span>
              </a>
              <a href="{p}ac-not-blowing-cold-air.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">AC Not Blowing Cold Air</span>
                  <span class="t6-nav-panel-desc">Rapid fix for warm vent air, low delta-T splits, frozen coils, and refrigerant.</span>
                </span>
              </a>
              <a href="{p}commercial-ac-unit-replacement.html" class="t6-nav-panel-item">
                <span class="t6-nav-panel-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg></span>
                <span class="t6-nav-panel-text">
                  <span class="t6-nav-panel-title">Commercial AC Replacement</span>
                  <span class="t6-nav-panel-desc">Rooftop RTU and commercial packaged replacement with crane rigging.</span>
                </span>
              </a>"""

NEW_SERVICES_DRAWER = """<li><a href="{p}ac-not-working.html" class="t6-link-grow t6-link-grow--on-ink">AC Not Working</a></li><li><a href="{p}central-ac-repair.html" class="t6-link-grow t6-link-grow--on-ink">Central AC Repair</a></li><li><a href="{p}ac-not-blowing-cold-air.html" class="t6-link-grow t6-link-grow--on-ink">AC Not Blowing Cold Air</a></li><li><a href="{p}commercial-ac-unit-replacement.html" class="t6-link-grow t6-link-grow--on-ink">Commercial AC Replacement</a></li>"""

NEW_SERVICES_FOOTER = """<li><a href="{p}ac-not-working.html" style="color:rgba(255,255,255,.85);text-decoration:none;">AC Not Working</a></li><li><a href="{p}central-ac-repair.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Central AC Repair</a></li><li><a href="{p}ac-not-blowing-cold-air.html" style="color:rgba(255,255,255,.85);text-decoration:none;">AC Not Blowing Cold Air</a></li><li><a href="{p}commercial-ac-unit-replacement.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Commercial AC Replacement</a></li>"""

def update_file(filepath, depth=0):
    p = "../" if depth == 1 else ""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content
    changes = []

    # 1. Desktop Nav Panel
    panel_match = re.search(r'(<div\s+class="t6-nav-panel-grid">)(.*?)(</div>\s*<a\s+href="[^"]*services\.html")', content, re.DOTALL)
    if panel_match:
        panel_inner = panel_match.group(2)
        if f"{p}ac-not-working.html" not in panel_inner:
            # find refrigerant link in panel_inner
            ref_pattern = rf'(<a\s+href="{re.escape(p)}refrigerant-freon-recharge\.html"[^>]*>.*?</a>)'
            ref_match = re.search(ref_pattern, panel_inner, re.DOTALL)
            if ref_match:
                new_inner = panel_inner[:ref_match.end()] + "\n" + NEW_SERVICES_DESKTOP.format(p=p) + panel_inner[ref_match.end():]
                content = content[:panel_match.start(2)] + new_inner + content[panel_match.end(2):]
                changes.append("desktop-nav")

    # 2. Mobile Drawer
    drawer_match = re.search(r'(<summary[^>]*>\s*Browse Services\s*</summary>\s*<ul[^>]*>)(.*?)(</ul>\s*</details>)', content, re.DOTALL)
    if drawer_match:
        drawer_inner = drawer_match.group(2)
        if f"{p}ac-not-working.html" not in drawer_inner:
            # add after refrigerant link
            ref_pattern = rf'(<li><a\s+href="{re.escape(p)}refrigerant-freon-recharge\.html"[^>]*>.*?</a></li>)'
            ref_match = re.search(ref_pattern, drawer_inner, re.DOTALL)
            if ref_match:
                new_inner = drawer_inner[:ref_match.end()] + NEW_SERVICES_DRAWER.format(p=p) + drawer_inner[ref_match.end():]
                content = content[:drawer_match.start(2)] + new_inner + content[drawer_match.end(2):]
                changes.append("mobile-drawer")

    # 3. Footer Services
    footer_match = re.search(r'(<!--\s*RL-AUTO:footer-services\s*START\s*-->)(.*?)(<!--\s*RL-AUTO:footer-services\s*END\s*-->)', content, re.DOTALL)
    if footer_match:
        footer_inner = footer_match.group(2)
        if f"{p}ac-not-working.html" not in footer_inner:
            ref_pattern = rf'(<li><a\s+href="{re.escape(p)}refrigerant-freon-recharge\.html"[^>]*>.*?</a></li>)'
            ref_match = re.search(ref_pattern, footer_inner, re.DOTALL)
            if ref_match:
                new_inner = footer_inner[:ref_match.end()] + "\n" + NEW_SERVICES_FOOTER.format(p=p) + footer_inner[ref_match.end():]
                content = content[:footer_match.start(2)] + new_inner + content[footer_match.end(2):]
                changes.append("footer-services")
    else:
        # Check without RL-AUTO comment, e.g. blog.html
        footer_sec = re.search(r'(<p[^>]*>Services</p>.*?<ul[^>]*>)(.*?)(<li><a\s+href="[^"]*services\.html"[^>]*>View All)', content, re.DOTALL)
        if footer_sec:
            footer_inner = footer_sec.group(2)
            if f"{p}ac-not-working.html" not in footer_inner:
                ref_pattern = rf'(<li><a\s+href="{re.escape(p)}refrigerant-freon-recharge\.html"[^>]*>.*?</a></li>)'
                ref_match = re.search(ref_pattern, footer_inner, re.DOTALL)
                if ref_match:
                    new_inner = footer_inner[:ref_match.end()] + "\n" + NEW_SERVICES_FOOTER.format(p=p) + footer_inner[ref_match.end():]
                    content = content[:footer_sec.start(2)] + new_inner + content[footer_sec.end(2):]
                    changes.append("footer-services-plain")

    if changes:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[{filepath}] Updated: {', '.join(changes)}")
        return True
    return False

all_files = glob.glob("*.html")
for f in all_files:
    if f != "404.html":
        update_file(f, depth=0)

blog_files = glob.glob("blog/*.html")
for bf in blog_files:
    update_file(bf, depth=1)

print("Nav & footer update pass complete.")
