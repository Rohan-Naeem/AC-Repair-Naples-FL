# -*- coding: utf-8 -*-
"""
Script to integrate the 4 new services into:
1. index.html (Homepage cards, header nav panel, mobile drawer, footer services)
2. services.html (Service cards, header nav panel, mobile drawer, footer services)
3. All other root HTML files (header nav panel, mobile drawer, footer services)
4. All blog/*.html files (header nav panel, mobile drawer, footer services with ../ prefix)
5. sitemap.xml
6. _redirects
7. vercel.json
8. build_blog.py
"""

import os
import glob
import re
import json

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

INDEX_NEW_CARDS = """
          <article class="t6-card" data-sal="slide-up" data-sal-delay="480">
            <div class="t6-card-image" style="aspect-ratio:16 / 10;">
              <img src="assets/images/services/ac-not-working.webp"
                alt="Emergency AC not working troubleshooting in Naples, FL." loading="lazy" />
              <span
                style="position:absolute;top:14px;left:14px;width:44px;height:44px;border-radius:10px;background:var(--t6-green);color:#fff;display:inline-flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.18);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path
                    d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z" />
                </svg>
              </span>
            </div>
            <div class="t6-card-body">
              <h3 style="margin:0 0 .55rem;font-size:1.25rem;">AC Not Working (Complete Shutdown)</h3>
              <p class="t6-muted"
                style="margin:0 0 1rem;font-size:.95rem;line-height:1.6;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;">
                When your AC won't start, trips the circuit breaker, or completely shuts down, our emergency technicians diagnose electrical relays, capacitors, contactors, and safety float switches to restore cooling fast.</p>
              <a href="ac-not-working.html" class="t6-link-grow">View Details <svg width="16" height="16"
                  viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"
                  stroke-linejoin="round">
                  <path d="M5 12h14M12 5l7 7-7 7" />
                </svg></a>
            </div>
          </article>

          <article class="t6-card" data-sal="slide-up" data-sal-delay="560">
            <div class="t6-card-image" style="aspect-ratio:16 / 10;">
              <img src="assets/images/services/central-ac-repair.webp"
                alt="Central air conditioning repair services in Naples, FL." loading="lazy" />
              <span
                style="position:absolute;top:14px;left:14px;width:44px;height:44px;border-radius:10px;background:var(--t6-green);color:#fff;display:inline-flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.18);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path
                    d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z" />
                </svg>
              </span>
            </div>
            <div class="t6-card-body">
              <h3 style="margin:0 0 .55rem;font-size:1.25rem;">Central AC Repair & Service</h3>
              <p class="t6-muted"
                style="margin:0 0 1rem;font-size:.95rem;line-height:1.6;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;">
                Comprehensive diagnostics and repair for split-system central air conditioners. We service air handlers, ECM blower motors, evaporator coils, expansion valves, and outdoor condensers.</p>
              <a href="central-ac-repair.html" class="t6-link-grow">View Details <svg width="16" height="16"
                  viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"
                  stroke-linejoin="round">
                  <path d="M5 12h14M12 5l7 7-7 7" />
                </svg></a>
            </div>
          </article>

          <article class="t6-card" data-sal="slide-up" data-sal-delay="640">
            <div class="t6-card-image" style="aspect-ratio:16 / 10;">
              <img src="assets/images/services/ac-not-blowing-cold-air.webp"
                alt="AC not blowing cold air troubleshooting in Naples, FL." loading="lazy" />
              <span
                style="position:absolute;top:14px;left:14px;width:44px;height:44px;border-radius:10px;background:var(--t6-green);color:#fff;display:inline-flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.18);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path
                    d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z" />
                </svg>
              </span>
            </div>
            <div class="t6-card-body">
              <h3 style="margin:0 0 .55rem;font-size:1.25rem;">AC Not Blowing Cold Air</h3>
              <p class="t6-muted"
                style="margin:0 0 1rem;font-size:.95rem;line-height:1.6;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;">
                If your air conditioner runs but blows warm or room-temperature air, we test temperature split Delta-T, inspect refrigerant charge for pinhole leaks, and thaw frozen evaporator coils.</p>
              <a href="ac-not-blowing-cold-air.html" class="t6-link-grow">View Details <svg width="16" height="16"
                  viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"
                  stroke-linejoin="round">
                  <path d="M5 12h14M12 5l7 7-7 7" />
                </svg></a>
            </div>
          </article>

          <article class="t6-card" data-sal="slide-up" data-sal-delay="720">
            <div class="t6-card-image" style="aspect-ratio:16 / 10;">
              <img src="assets/images/services/commercial-ac-unit-replacement.webp"
                alt="Commercial AC unit replacement and rooftop RTU installation in Naples, FL." loading="lazy" />
              <span
                style="position:absolute;top:14px;left:14px;width:44px;height:44px;border-radius:10px;background:var(--t6-green);color:#fff;display:inline-flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.18);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path
                    d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z" />
                </svg>
              </span>
            </div>
            <div class="t6-card-body">
              <h3 style="margin:0 0 .55rem;font-size:1.25rem;">Commercial AC Unit Replacement</h3>
              <p class="t6-muted"
                style="margin:0 0 1rem;font-size:.95rem;line-height:1.6;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;">
                Turn-key commercial HVAC replacement for Naples businesses, offices, and restaurants. We install heavy-duty rooftop packaged units (RTUs) and multi-zone split systems with crane rigging.</p>
              <a href="commercial-ac-unit-replacement.html" class="t6-link-grow">View Details <svg width="16" height="16"
                  viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"
                  stroke-linejoin="round">
                  <path d="M5 12h14M12 5l7 7-7 7" />
                </svg></a>
            </div>
          </article>"""

SERVICES_HTML_NEW_CARDS = """
      <article class="t6-card" data-sal="slide-up" data-sal-delay="800">
        <div class="t6-card-image" style="aspect-ratio:16 / 10;">
          <img src="assets/images/services/ac-not-working.webp" alt="Certified HVAC technician diagnosing an AC unit not working in Naples, FL." loading="lazy" />
          <span style="position:absolute;top:14px;left:14px;width:44px;height:44px;border-radius:10px;background:var(--t6-green);color:var(--t6-ink);display:inline-flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.18);">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>
          </span>
        </div>
        <div class="t6-card-body">
          <h3 style="margin:0 0 .55rem;font-size:1.25rem;">AC Not Working</h3>
          <p class="t6-muted" style="margin:0 0 1rem;font-size:.95rem;line-height:1.6;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;">When your AC refuses to turn on, trips the circuit breaker, or completely shuts down, we provide fast emergency diagnostics, electrical repair, capacitor swaps, and float switch resets.</p>
          <a href="ac-not-working.html" class="t6-link-grow">View Details <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        </div>
      </article>
      <article class="t6-card" data-sal="slide-up" data-sal-delay="900">
        <div class="t6-card-image" style="aspect-ratio:16 / 10;">
          <img src="assets/images/services/central-ac-repair.webp" alt="NATE-certified technician repairing a residential split-system central AC air handler in Naples, FL." loading="lazy" />
          <span style="position:absolute;top:14px;left:14px;width:44px;height:44px;border-radius:10px;background:var(--t6-green);color:var(--t6-ink);display:inline-flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.18);">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>
          </span>
        </div>
        <div class="t6-card-body">
          <h3 style="margin:0 0 .55rem;font-size:1.25rem;">Central AC Repair</h3>
          <p class="t6-muted" style="margin:0 0 1rem;font-size:.95rem;line-height:1.6;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;">Precision repair for residential split-system central air conditioners and heat pumps. We service air handlers, ECM blower motors, evaporator coils, expansion valves, and outdoor condensers.</p>
          <a href="central-ac-repair.html" class="t6-link-grow">View Details <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        </div>
      </article>
      <article class="t6-card" data-sal="slide-up" data-sal-delay="1000">
        <div class="t6-card-image" style="aspect-ratio:16 / 10;">
          <img src="assets/images/services/ac-not-blowing-cold-air.webp" alt="HVAC technician checking supply vent temperature in Naples Florida home." loading="lazy" />
          <span style="position:absolute;top:14px;left:14px;width:44px;height:44px;border-radius:10px;background:var(--t6-green);color:var(--t6-ink);display:inline-flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.18);">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>
          </span>
        </div>
        <div class="t6-card-body">
          <h3 style="margin:0 0 .55rem;font-size:1.25rem;">AC Not Blowing Cold Air</h3>
          <p class="t6-muted" style="margin:0 0 1rem;font-size:.95rem;line-height:1.6;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;">If your air conditioner blows warm or room-temperature air, we test supply Delta-T, inspect refrigerant charge for pinhole leaks, thaw frozen evaporator coils, and restore ice-cold 55°F air.</p>
          <a href="ac-not-blowing-cold-air.html" class="t6-link-grow">View Details <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        </div>
      </article>
      <article class="t6-card" data-sal="slide-up" data-sal-delay="1100">
        <div class="t6-card-image" style="aspect-ratio:16 / 10;">
          <img src="assets/images/services/commercial-ac-unit-replacement.webp" alt="Commercial HVAC rooftop packaged unit replacement with crane lift in Naples, FL." loading="lazy" />
          <span style="position:absolute;top:14px;left:14px;width:44px;height:44px;border-radius:10px;background:var(--t6-green);color:var(--t6-ink);display:inline-flex;align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.18);">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>
          </span>
        </div>
        <div class="t6-card-body">
          <h3 style="margin:0 0 .55rem;font-size:1.25rem;">Commercial AC Unit Replacement</h3>
          <p class="t6-muted" style="margin:0 0 1rem;font-size:.95rem;line-height:1.6;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;">Heavy-duty commercial AC replacements, packaged rooftop units (RTU), curb adapters, crane rigging, and multi-zone VRF systems engineered for Naples businesses with minimal downtime.</p>
          <a href="commercial-ac-unit-replacement.html" class="t6-link-grow">View Details <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></a>
        </div>
      </article>"""

def update_file_nav(filepath, depth=0):
    p = "../" if depth == 1 else ""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content

    # 1. Update Desktop nav panel if not already containing ac-not-working.html
    if f"{p}ac-not-working.html" not in content and f"{p}mini-split-repair.html" in content:
        # We can append the new services after refrigerant-freon-recharge in the panel
        target_ref = f"{p}refrigerant-freon-recharge.html"
        # Find the closing </a> of the refrigerant service item in t6-nav-panel
        pattern = rf'(<a\s+href="{re.escape(target_ref)}"[^>]*class="t6-nav-panel-item"[^>]*>.*?</a>)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            new_chunk = match.group(1) + "\n" + NEW_SERVICES_DESKTOP.format(p=p)
            content = content[:match.start()] + new_chunk + content[match.end():]
            print(f"[{filepath}] Updated desktop nav panel")

    # 2. Update Mobile drawer if not already containing ac-not-working.html
    if f"{p}ac-not-working.html" not in content and "Browse Services" in content:
        target_drawer = f'<li><a href="{p}refrigerant-freon-recharge.html" class="t6-link-grow t6-link-grow--on-ink">Refrigerant & Freon Recharge</a></li>'
        if target_drawer in content:
            content = content.replace(target_drawer, target_drawer + NEW_SERVICES_DRAWER.format(p=p))
            print(f"[{filepath}] Updated mobile drawer")
        else:
            # Fallback regex for drawer link
            m = re.search(rf'<li><a\s+href="{re.escape(p)}refrigerant-freon-recharge\.html"[^>]*>.*?</a></li>', content)
            if m:
                content = content[:m.end()] + NEW_SERVICES_DRAWER.format(p=p) + content[m.end():]
                print(f"[{filepath}] Updated mobile drawer (regex)")

    # 3. Update Footer services column if not already containing ac-not-working.html
    if f"{p}ac-not-working.html" not in content and f"{p}refrigerant-freon-recharge.html" in content:
        target_footer = f'<li><a href="{p}refrigerant-freon-recharge.html" style="color:rgba(255,255,255,.85);text-decoration:none;">Refrigerant & Freon Recharge</a></li>'
        if target_footer in content:
            content = content.replace(target_footer, target_footer + "\n" + NEW_SERVICES_FOOTER.format(p=p))
            print(f"[{filepath}] Updated footer services")
        else:
            # regex for footer
            m = re.search(rf'<li><a\s+href="{re.escape(p)}refrigerant-freon-recharge\.html"[^>]*>.*?</a></li>', content)
            if m:
                content = content[:m.end()] + "\n" + NEW_SERVICES_FOOTER.format(p=p) + content[m.end():]
                print(f"[{filepath}] Updated footer services (regex)")

    if content != orig_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

# 1. Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# Add cards to index.html if not already present
if "ac-not-working.html" not in idx_content:
    # Find the end of the services grid in index.html
    # In index.html, the last service article before </div> is ac-maintenance-tune-up.html
    target_idx = 'href="ac-maintenance-tune-up.html" class="t6-link-grow">View Details'
    if target_idx in idx_content:
        pos = idx_content.find(target_idx)
        # Find closing </article> after pos
        end_art = idx_content.find("</article>", pos)
        if end_art != -1:
            end_art += len("</article>")
            idx_content = idx_content[:end_art] + INDEX_NEW_CARDS + idx_content[end_art:]
            print("[index.html] Inserted 4 new homepage service cards!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)

update_file_nav("index.html", depth=0)

# 2. Update services.html
with open("services.html", "r", encoding="utf-8") as f:
    svc_content = f.read()

if "ac-not-working.html" not in svc_content:
    # In services.html, the last card is refrigerant-freon-recharge.html
    target_svc = 'href="refrigerant-freon-recharge.html" class="t6-link-grow">View Details'
    if target_svc in svc_content:
        pos = svc_content.find(target_svc)
        end_art = svc_content.find("</article>", pos)
        if end_art != -1:
            end_art += len("</article>")
            svc_content = svc_content[:end_art] + SERVICES_HTML_NEW_CARDS + svc_content[end_art:]
            print("[services.html] Inserted 4 new service cards in grid!")

with open("services.html", "w", encoding="utf-8") as f:
    f.write(svc_content)

update_file_nav("services.html", depth=0)

# 3. Update all other root HTML files
root_htmls = glob.glob("*.html")
for r in root_htmls:
    if r in ["index.html", "services.html", "404.html"]:
        continue
    updated = update_file_nav(r, depth=0)
    if updated:
        print(f"Updated {r}")

# 4. Update blog/*.html files
blog_htmls = glob.glob("blog/*.html")
for b in blog_htmls:
    updated = update_file_nav(b, depth=1)
    if updated:
        print(f"Updated {b}")

# 5. Update sitemap.xml
with open("sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()

new_sitemap_entries = """    <url>
        <loc>https://acrepairnaplesfl.com/ac-not-working</loc>
        <lastmod>2026-10-15</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://acrepairnaplesfl.com/central-ac-repair</loc>
        <lastmod>2026-10-15</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://acrepairnaplesfl.com/ac-not-blowing-cold-air</loc>
        <lastmod>2026-10-15</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://acrepairnaplesfl.com/commercial-ac-unit-replacement</loc>
        <lastmod>2026-10-15</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.9</priority>
    </url>
"""

if "https://acrepairnaplesfl.com/ac-not-working" not in sitemap:
    target_loc = "<loc>https://acrepairnaplesfl.com/refrigerant-freon-recharge</loc>"
    if target_loc in sitemap:
        pos = sitemap.find(target_loc)
        end_url = sitemap.find("</url>", pos)
        if end_url != -1:
            end_url += len("</url>")
            sitemap = sitemap[:end_url] + "\n" + new_sitemap_entries + sitemap[end_url:]
            with open("sitemap.xml", "w", encoding="utf-8") as f:
                f.write(sitemap)
            print("[sitemap.xml] Added 4 new service URLs")

# 6. Update _redirects
with open("_redirects", "r", encoding="utf-8") as f:
    redirects = f.read()

new_redirect_entries = """/ac-not-working.html /ac-not-working 301!
/central-ac-repair.html /central-ac-repair 301!
/ac-not-blowing-cold-air.html /ac-not-blowing-cold-air 301!
/commercial-ac-unit-replacement.html /commercial-ac-unit-replacement 301!
"""

if "/ac-not-working.html" not in redirects:
    target_redir = "/refrigerant-freon-recharge.html /refrigerant-freon-recharge 301!"
    if target_redir in redirects:
        redirects = redirects.replace(target_redir, target_redir + "\n" + new_redirect_entries.strip())
    else:
        redirects = redirects.strip() + "\n" + new_redirect_entries
    with open("_redirects", "w", encoding="utf-8") as f:
        f.write(redirects + "\n")
    print("[_redirects] Added 4 new 301 redirects")

# 7. Update vercel.json
with open("vercel.json", "r", encoding="utf-8") as f:
    vdata = json.load(f)

v_redirects = vdata.get("redirects", [])
existing_sources = {r.get("source") for r in v_redirects}

new_v_redirects = [
    {"source": "/ac-not-working.html", "destination": "/ac-not-working", "permanent": True},
    {"source": "/central-ac-repair.html", "destination": "/central-ac-repair", "permanent": True},
    {"source": "/ac-not-blowing-cold-air.html", "destination": "/ac-not-blowing-cold-air", "permanent": True},
    {"source": "/commercial-ac-unit-replacement.html", "destination": "/commercial-ac-unit-replacement", "permanent": True}
]

added_v = 0
for nr in new_v_redirects:
    if nr["source"] not in existing_sources:
        v_redirects.append(nr)
        added_v += 1

if added_v > 0:
    vdata["redirects"] = v_redirects
    with open("vercel.json", "w", encoding="utf-8") as f:
        json.dump(vdata, f, indent=2)
    print(f"[vercel.json] Added {added_v} new redirects")

print("All site integrations completed successfully!")
