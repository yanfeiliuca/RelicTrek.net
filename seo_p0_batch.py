#!/usr/bin/env python3
"""
RelicTrek P0 SEO Batch Fix
==========================
Implements all P0 SEO improvements across all 296 pages:
1. Schema structured data (HowTo, FAQ, BreadcrumbList, Article)
2. Optimized page titles with long-tail keywords
3. Optimized meta descriptions
4. Canonical tags
5. Hreflang tags (EN ↔ ZH)

Usage:
    python seo_p0_batch.py          # Preview changes (dry run)
    python seo_p0_batch.py --apply  # Apply changes to all files
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime

# ─── Configuration ──────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent

GAMES = {
    'terraria': {'en': 'Terraria', 'zh': '泰拉瑞亚'},
    'subnautica2': {'en': 'Subnautica 2', 'zh': '深海迷航2'},
    'monster-hunter-wilds': {'en': 'Monster Hunter Wilds', 'zh': '怪物猎人：荒野'},
    'zelda-totk': {'en': 'Zelda: Tears of the Kingdom', 'zh': '塞尔达传说：王国之泪'},
    'minecraft': {'en': 'Minecraft', 'zh': '我的世界'},
    'no-mans-sky': {'en': 'No Man\'s Sky', 'zh': '无人深空'},
    'baldurs-gate-3': {'en': 'Baldur\'s Gate 3', 'zh': '博德之门3'},
    'valheim': {'en': 'Valheim', 'zh': '英灵神殿'},
    'path-of-exile-2': {'en': 'Path of Exile 2', 'zh': '流放之路2'},
    'elden-ring': {'en': 'Elden Ring', 'zh': '艾尔登法环'},
    'stardew-valley': {'en': 'Stardew Valley', 'zh': '星露谷物语'},
    'hades-2': {'en': 'Hades 2', 'zh': '哈迪斯2'},
    'satisfactory': {'en': 'Satisfactory', 'zh': '幸福工厂'},
}

# SEO-optimized title templates per game (long-tail keyword rich)
TITLE_TEMPLATES = {
    'terraria': {
        'en': '{item} Crafting Guide: Complete Materials & Locations | Terraria | RelicTrek',
        'zh': '泰拉瑞亚{item}合成攻略：全材料位置一览 | RelicTrek',
    },
    'subnautica2': {
        'en': '{item} Crafting Guide: How to Build & Upgrade | Subnautica 2 | RelicTrek',
        'zh': '深海迷航2{item}建造攻略：制作方法与升级 | RelicTrek',
    },
    'monster-hunter-wilds': {
        'en': '{item} Guide: Stats, Crafting & Best Build | MH Wilds | RelicTrek',
        'zh': '怪物猎人荒野{item}攻略：属性合成与最佳配装 | RelicTrek',
    },
    'zelda-totk': {
        'en': '{item} Guide: How to Get, Stats & Best Fuse | Zelda TOTK | RelicTrek',
        'zh': '塞尔达王国之泪{item}攻略：获取方法属性与最佳余料 | RelicTrek',
    },
    'minecraft': {
        'en': '{item} Crafting Guide: Recipe, Materials & Setup | Minecraft | RelicTrek',
        'zh': '我的世界{item}合成攻略：配方材料与摆放 | RelicTrek',
    },
    'no-mans-sky': {
        'en': '{item} Guide: How to Craft & Farm Efficiently | NMS | RelicTrek',
        'zh': '无人深空{item}攻略：合成方法与高效农场 | RelicTrek',
    },
    'baldurs-gate-3': {
        'en': '{item} Guide: Location, Stats & Best Build | BG3 | RelicTrek',
        'zh': '博德之门3{item}攻略：位置属性与最佳Build | RelicTrek',
    },
    'valheim': {
        'en': '{item} Crafting Guide: Materials & Best Upgrade | Valheim | RelicTrek',
        'zh': '英灵神殿{item}合成攻略：材料与最佳升级 | RelicTrek',
    },
    'path-of-exile-2': {
        'en': '{item} Guide: How to Get, Build & Price | POE2 | RelicTrek',
        'zh': '流放之路2{item}攻略：获取方法与Build价格 | RelicTrek',
    },
    'elden-ring': {
        'en': '{item} Crafting Guide: Effects, Duration & Best Use | Elden Ring | RelicTrek',
        'zh': '艾尔登法环{item}合成攻略：效果持续与最佳用法 | RelicTrek',
    },
    'stardew-valley': {
        'en': '{item} Crafting Guide: Recipe & Best Use | Stardew Valley | RelicTrek',
        'zh': '星露谷物语{item}合成攻略：配方与最佳用法 | RelicTrek',
    },
    'hades-2': {
        'en': '{item} Guide: How to Unlock & Best Strategy | Hades 2 | RelicTrek',
        'zh': '哈迪斯2{item}攻略：解锁方法与最佳策略 | RelicTrek',
    },
    'satisfactory': {
        'en': '{item} Guide: Alternate Recipe & Efficiency | Satisfactory | RelicTrek',
        'zh': '幸福工厂{item}攻略：替代配方与效率优化 | RelicTrek',
    },
}

# Meta description templates
DESC_TEMPLATES = {
    'terraria': {
        'en': 'Complete {item} crafting guide for Terraria. Full materials list with locations, drop rates, step-by-step recipe, farming route & gotcha tips. Updated for 1.4.4.',
        'zh': '泰拉瑞亚{item}完整合成攻略。全材料清单与位置、掉率、分步配方、最佳刷取路线与避坑指南。',
    },
    'zelda-totk': {
        'en': 'How to get {item} in Zelda Tears of the Kingdom. Complete stats, best fuse combinations, durability tips and location guide.',
        'zh': '塞尔达王国之泪{item}获取攻略。完整属性、最佳余料组合、耐久度技巧与位置指南。',
    },
    'elden-ring': {
        'en': 'Complete {item} crafting guide for Elden Ring. Effects, duration, materials needed, farming locations & best combat uses.',
        'zh': '艾尔登法环{item}完整合成攻略。效果、持续时间、所需材料、农场位置与最佳战斗用法。',
    },
    'minecraft': {
        'en': 'Complete {item} crafting guide for Minecraft. Materials, recipe, setup tips & best uses. Works in 1.20+ Java & Bedrock.',
        'zh': '我的世界{item}完整合成攻略。材料、配方、设置技巧与最佳用法。适用于1.20+ Java和基岩版。',
    },
    'stardew-valley': {
        'en': 'Complete {item} crafting guide for Stardew Valley. Recipe, materials, profit analysis & best uses on your farm.',
        'zh': '星露谷物语{item}完整合成攻略。配方、材料、利润分析与农场最佳用法。',
    },
    'default': {
        'en': 'Complete {item} crafting guide for {game}. Materials, locations, step-by-step recipe, gotcha tips & optimal route.',
        'zh': '{game}{item}完整合成攻略。材料、位置、分步配方、避坑指南与最优路线。',
    },
}

TODAY = datetime.now().strftime('%Y-%m-%d')


# ─── HTML Parsing Helpers ───────────────────────────────────────────

def extract_from_html(html):
    """Extract key information from an HTML page"""
    data = {
        'title': '',
        'description': '',
        'h1': '',
        'h2_sections': [],
        'body_text': '',
        'difficulty': '',
        'item_icon_class': '',
    }
    
    # Extract title
    title_match = re.search(r'<title>([^<]*)</title>', html, re.IGNORECASE)
    if title_match:
        data['title'] = title_match.group(1).strip()
    
    # Extract meta description
    desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html, re.IGNORECASE)
    if desc_match:
        data['description'] = desc_match.group(1).strip()
    else:
        desc_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', html, re.IGNORECASE)
        if desc_match:
            data['description'] = desc_match.group(1).strip()
    
    # Extract H1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
    if h1_match:
        data['h1'] = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
    
    # Extract H2 sections (module names)
    h2_matches = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.IGNORECASE | re.DOTALL)
    data['h2_sections'] = [re.sub(r'<[^>]+>', '', h).strip() for h in h2_matches]
    
    # Extract difficulty
    diff_match = re.search(r'<div class="difficulty">(.*?)</div>', html, re.IGNORECASE | re.DOTALL)
    if diff_match:
        data['difficulty'] = re.sub(r'<[^>]+>', '', diff_match.group(1)).strip()
    
    # Extract item icon class
    icon_match = re.search(r'class="(item-icon-\w+)"', html)
    if icon_match:
        data['item_icon_class'] = icon_match.group(1)
    
    # Extract first paragraph text for description fallback
    p_match = re.search(r'<div class="section"[^>]*>.*?<p>(.*?)</p>', html, re.IGNORECASE | re.DOTALL)
    if p_match:
        data['body_text'] = re.sub(r'<[^>]+>', '', p_match.group(1)).strip()[:200]
    
    return data


def extract_faq_items(html):
    """Extract FAQ items from gotcha-tips section"""
    faqs = []
    
    # Look for gotcha-box or tips sections
    gotcha_match = re.search(r'Gotcha|gotcha|⚠|Warning|warning', html)
    if gotcha_match:
        # Try to extract tips as FAQ
        tip_matches = re.findall(r'<li[^>]*>(.*?)</li>', html, re.DOTALL)
        for tip in tip_matches[:5]:
            clean_tip = re.sub(r'<[^>]+>', '', tip).strip()
            if len(clean_tip) > 20 and len(clean_tip) < 200:
                faqs.append({
                    'question': f'What should I watch out for when crafting this item?',
                    'answer': clean_tip
                })
                break  # Just one for now
    
    return faqs


def extract_crafting_steps(html):
    """Extract crafting steps from recipe section"""
    steps = []
    
    # Look for numbered steps or route items
    step_matches = re.findall(r'<li[^>]*>.*?<strong>(.*?)</strong>(.*?)</li>', html, re.DOTALL)
    for i, (title, desc) in enumerate(step_matches[:8], 1):
        clean_title = re.sub(r'<[^>]+>', '', title).strip()
        clean_desc = re.sub(r'<[^>]+>', '', desc).strip()
        if clean_title:
            steps.append({
                'position': i,
                'name': clean_title,
                'text': f"{clean_title}: {clean_desc}" if clean_desc else clean_title
            })
    
    # If no steps found, create generic ones from sections
    if not steps and 'h2_sections' in dir():
        for i, section in enumerate([s for s in [] if s], 1):
            steps.append({
                'position': i,
                'name': section,
                'text': f'Complete the {section} phase'
            })
    
    return steps


# ─── Schema Generators ──────────────────────────────────────────────

def generate_schemas(data, game_dir, item_slug, is_zh=False):
    """Generate all Schema.org structured data for a page"""
    
    game_name = GAMES.get(game_dir, {}).get('en', game_dir)
    game_zh = GAMES.get(game_dir, {}).get('zh', game_dir)
    item_name = data['h1'] or item_slug.replace('-', ' ').title()
    lang = 'zh-CN' if is_zh else 'en'
    
    # Determine URL
    if is_zh:
        url = f"https://relictrek.net/{game_dir}/zh/{item_slug}.html"
        en_url = f"https://relictrek.net/{game_dir}/{item_slug}.html"
    else:
        url = f"https://relictrek.net/{game_dir}/{item_slug}.html"
        en_url = url
    
    schemas = []
    
    # 1. BreadcrumbList Schema
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home" if not is_zh else "首页",
                "item": "https://relictrek.net/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": game_name,
                "item": f"https://relictrek.net/{game_dir}/"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": item_name,
                "item": url
            }
        ]
    }
    schemas.append(breadcrumb)
    
    # 2. HowTo Schema (if crafting steps found)
    steps = extract_crafting_steps(data.get('_raw_html', ''))
    if steps:
        howto = {
            "@context": "https://schema.org",
            "@type": "HowTo",
            "name": data['title'] or f"How to craft {item_name} in {game_name}",
            "description": data['description'] or f"Complete guide to crafting {item_name}",
            "totalTime": "PT4H",
            "estimatedCost": {
                "@type": "MonetaryAmount",
                "currency": "USD",
                "value": "0"
            },
            "supply": [
                {
                    "@type": "HowToSupply",
                    "name": data.get('material', 'Various materials')
                }
            ],
            "step": [
                {
                    "@type": "HowToStep",
                    "position": step['position'],
                    "name": step['name'],
                    "text": step['text'],
                    "url": f"{url}#step-{step['position']}"
                } for step in steps
            ]
        }
        schemas.append(howto)
    
    # 3. FAQPage Schema
    faqs = extract_faq_items(data.get('_raw_html', ''))
    if faqs:
        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": faq['question'],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": faq['answer']
                    }
                } for faq in faqs
            ]
        }
        schemas.append(faq_schema)
    
    # 4. Article Schema
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": data['title'] or item_name,
        "description": data['description'] or '',
        "author": {
            "@type": "Organization",
            "name": "RelicTrek"
        },
        "publisher": {
            "@type": "Organization",
            "name": "RelicTrek",
            "logo": {
                "@type": "ImageObject",
                "url": "https://relictrek.net/logo.png"
            }
        },
        "datePublished": TODAY,
        "dateModified": TODAY,
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": url
        }
    }
    schemas.append(article)
    
    return schemas


# ─── SEO Tag Generators ─────────────────────────────────────────────

def generate_optimized_title(data, game_dir, item_slug, is_zh=False):
    """Generate SEO-optimized title with long-tail keywords"""
    
    game_name = GAMES.get(game_dir, {}).get('en', game_dir)
    item_name = data['h1'] or item_slug.replace('-', ' ').title()
    
    templates = TITLE_TEMPLATES.get(game_dir, TITLE_TEMPLATES['terraria'])  # fallback
    template = templates.get('zh' if is_zh else 'en', templates['en'])
    
    return template.format(item=item_name, game=game_name)


def generate_optimized_description(data, game_dir, item_slug, is_zh=False):
    """Generate SEO-optimized meta description"""
    
    game_name = GAMES.get(game_dir, {}).get('en', game_dir)
    item_name = data['h1'] or item_slug.replace('-', ' ').title()
    
    templates = DESC_TEMPLATES.get(game_dir, DESC_TEMPLATES['default'])
    template = templates.get('zh' if is_zh else 'en', templates['en'])
    
    desc = template.format(item=item_name, game=game_name)
    
    # Truncate to 155-160 chars for optimal display
    if len(desc) > 158:
        desc = desc[:155] + '...'
    
    return desc


def generate_hreflang(game_dir, item_slug):
    """Generate hreflang tags for EN/ZH pair"""
    
    en_url = f"https://relictrek.net/{game_dir}/{item_slug}.html"
    zh_url = f"https://relictrek.net/{game_dir}/zh/{item_slug}.html"
    
    return f'''<link rel="alternate" hreflang="en" href="{en_url}" />
<link rel="alternate" hreflang="zh-CN" href="{zh_url}" />
<link rel="alternate" hreflang="x-default" href="{en_url}" />'''


def generate_canonical(game_dir, item_slug, is_zh=False):
    """Generate canonical tag"""
    
    if is_zh:
        url = f"https://relictrek.net/{game_dir}/zh/{item_slug}.html"
    else:
        url = f"https://relictrek.net/{game_dir}/{item_slug}.html"
    
    return f'<link rel="canonical" href="{url}" />'


# ─── Main Processing ────────────────────────────────────────────────

def process_file(filepath, game_dir, item_slug, is_zh=False, dry_run=True):
    """Process a single HTML file with all P0 SEO improvements"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    changes = []
    
    # Extract data from HTML
    data = extract_from_html(html)
    data['_raw_html'] = html
    
    # ─── 1. Generate and inject Schema ──────────────────────────
    schemas = generate_schemas(data, game_dir, item_slug, is_zh)
    
    # Find position after <head> tag to inject schemas
    head_end = html.find('</head>')
    if head_end == -1:
        head_end = html.find('<body')
    
    if head_end > 0 and schemas:
        schema_scripts = []
        for schema in schemas:
            schema_scripts.append(f'<script type="application/ld+json">\n{json.dumps(schema, indent=2, ensure_ascii=False)}\n</script>')
        
        schema_block = '\n'.join(schema_scripts)
        html = html[:head_end] + '\n' + schema_block + '\n' + html[head_end:]
        changes.append(f"Added {len(schemas)} Schema(s)")
    
    # ─── 2. Update Title ────────────────────────────────────────
    new_title = generate_optimized_title(data, game_dir, item_slug, is_zh)
    
    title_match = re.search(r'(<title>)[^<]*(</title>)', html, re.IGNORECASE)
    if title_match:
        old_title = title_match.group(0)
        new_title_tag = f'<title>{new_title}</title>'
        if old_title != new_title_tag:
            html = html.replace(old_title, new_title_tag)
            changes.append(f"Title: '{data['title'][:40]}...' → '{new_title[:50]}...'")
    
    # ─── 3. Update Meta Description ─────────────────────────────
    new_desc = generate_optimized_description(data, game_dir, item_slug, is_zh)
    
    desc_pattern = r'(<meta[^>]*name=["\']description["\'][^>]*content=["\'])[^"\']*(["\'])'
    desc_replacement = r'\g<1>' + new_desc + r'\2'
    
    if re.search(desc_pattern, html, re.IGNORECASE):
        html = re.sub(desc_pattern, desc_replacement, html, flags=re.IGNORECASE)
        changes.append(f"Meta desc updated ({len(new_desc)} chars)")
    else:
        # No existing meta description, add one
        head_match = re.search(r'<head[^>]*>', html, re.IGNORECASE)
        if head_match:
            insert_pos = head_match.end()
            meta_tag = f'\n<meta name="description" content="{new_desc}">'
            html = html[:insert_pos] + meta_tag + html[insert_pos:]
            changes.append(f"Meta desc added ({len(new_desc)} chars)")
    
    # ─── 4. Add Canonical Tag ───────────────────────────────────
    canonical = generate_canonical(game_dir, item_slug, is_zh)
    
    if '<link rel="canonical"' not in html:
        # Insert before </head>
        head_end = html.find('</head>')
        if head_end > 0:
            html = html[:head_end] + canonical + '\n' + html[head_end:]
            changes.append("Canonical added")
    
    # ─── 5. Add Hreflang Tags ──────────────────────────────────
    hreflang = generate_hreflang(game_dir, item_slug)
    
    if '<link rel="alternate" hreflang=' not in html:
        # Insert before </head>
        head_end = html.find('</head>')
        if head_end > 0:
            html = html[:head_end] + hreflang + '\n' + html[head_end:]
            changes.append("Hreflang added (EN + ZH + x-default)")
    
    # Apply or preview
    if not dry_run and html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
    
    return changes, html != original


def process_blog_file(filepath, date_str, is_zh=False, dry_run=True):
    """Process blog HTML files"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    changes = []
    
    data = extract_from_html(html)
    
    # Extract item info from title if available
    item_name = data['h1'] or data['title'] or 'Game Item'
    
    # Generate blog-specific schemas
    url = f"https://relictrek.net/blog/{date_str}.html" if not is_zh else f"https://relictrek.net/blog/zh/{date_str}.html"
    
    # Article Schema for blog
    article = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": data['title'] or item_name,
        "description": data['description'] or '',
        "author": {"@type": "Organization", "name": "RelicTrek"},
        "publisher": {
            "@type": "Organization",
            "name": "RelicTrek",
            "logo": {"@type": "ImageObject", "url": "https://relictrek.net/logo.png"}
        },
        "datePublished": date_str,
        "dateModified": date_str,
        "mainEntityOfPage": {"@type": "WebPage", "@id": url}
    }
    
    # Breadcrumb for blog
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://relictrek.net/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://relictrek.net/blog/"},
            {"@type": "ListItem", "position": 3, "name": item_name[:50], "item": url}
        ]
    }
    
    schemas = [breadcrumb, article]
    
    # Inject schemas
    head_end = html.find('</head>')
    if head_end > 0:
        schema_scripts = []
        for schema in schemas:
            schema_scripts.append(f'<script type="application/ld+json">\n{json.dumps(schema, indent=2, ensure_ascii=False)}\n</script>')
        schema_block = '\n'.join(schema_scripts)
        html = html[:head_end] + '\n' + schema_block + '\n' + html[head_end:]
        changes.append(f"Added BlogPosting + Breadcrumb schemas")
    
    # Add canonical
    canonical = f'<link rel="canonical" href="{url}" />'
    if '<link rel="canonical"' not in html:
        head_end = html.find('</head>')
        if head_end > 0:
            html = html[:head_end] + canonical + '\n' + html[head_end:]
            changes.append("Canonical added")
    
    if not dry_run and html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
    
    return changes, html != original


def main():
    """Main execution"""
    import sys
    
    dry_run = '--apply' not in sys.argv
    
    if dry_run:
        print("=" * 70)
        print("RelicTrek P0 SEO Batch Fix — PREVIEW MODE (dry run)")
        print("Add --apply flag to execute changes")
        print("=" * 70)
    else:
        print("=" * 70)
        print("RelicTrek P0 SEO Batch Fix — APPLYING CHANGES")
        print("=" * 70)
    
    total_files = 0
    changed_files = 0
    all_changes = []
    
    # Process game item pages (EN + ZH)
    for game_dir in GAMES.keys():
        game_path = BASE_DIR / game_dir
        if not game_path.exists():
            continue
        
        # EN pages
        for html_file in game_path.glob('*.html'):
            if html_file.name == 'index.html':
                continue
            
            item_slug = html_file.stem
            changes, modified = process_file(
                str(html_file), game_dir, item_slug,
                is_zh=False, dry_run=dry_run
            )
            total_files += 1
            if modified:
                changed_files += 1
                all_changes.append(f"  {game_dir}/{html_file.name}: {', '.join(changes)}")
        
        # ZH pages
        zh_path = game_path / 'zh'
        if zh_path.exists():
            for html_file in zh_path.glob('*.html'):
                if html_file.name == 'index.html':
                    continue
                
                item_slug = html_file.stem
                changes, modified = process_file(
                    str(html_file), game_dir, item_slug,
                    is_zh=True, dry_run=dry_run
                )
                total_files += 1
                if modified:
                    changed_files += 1
                    all_changes.append(f"  {game_dir}/zh/{html_file.name}: {', '.join(changes)}")
    
    # Process blog pages
    blog_dir = BASE_DIR / 'blog'
    if blog_dir.exists():
        for html_file in blog_dir.glob('*.html'):
            if html_file.name == 'index.html':
                continue
            date_str = html_file.stem
            changes, modified = process_blog_file(
                str(html_file), date_str, is_zh=False, dry_run=dry_run
            )
            total_files += 1
            if modified:
                changed_files += 1
                all_changes.append(f"  blog/{html_file.name}: {', '.join(changes)}")
        
        zh_blog_dir = blog_dir / 'zh'
        if zh_blog_dir.exists():
            for html_file in zh_blog_dir.glob('*.html'):
                if html_file.name == 'index.html':
                    continue
                date_str = html_file.stem
                changes, modified = process_blog_file(
                    str(html_file), date_str, is_zh=True, dry_run=dry_run
                )
                total_files += 1
                if modified:
                    changed_files += 1
                    all_changes.append(f"  blog/zh/{html_file.name}: {', '.join(changes)}")
    
    # Print summary
    print(f"\n{'=' * 70}")
    print(f"SUMMARY")
    print(f"{'=' * 70}")
    print(f"Total files scanned: {total_files}")
    print(f"Files to modify: {changed_files}")
    
    # Show sample changes
    print(f"\nSample changes (first 10):")
    for change in all_changes[:10]:
        print(change)
    
    if len(all_changes) > 10:
        print(f"  ... and {len(all_changes) - 10} more")
    
    if dry_run:
        print(f"\n{'=' * 70}")
        print("This was a PREVIEW. No files were modified.")
        print("Run with --apply to execute changes.")
        print(f"{'=' * 70}")
    else:
        print(f"\n{'=' * 70}")
        print(f"✅ {changed_files} files modified successfully!")
        print(f"{'=' * 70}")


if __name__ == '__main__':
    main()
