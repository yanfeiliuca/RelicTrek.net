#!/usr/bin/env python3
"""
RelicTrek Daily Blog Generator
Automated daily blog post creation from trending gaming content.
Runs at 3:00 AM daily via cron/scheduler.

Usage:
    python generate_daily_blog.py          # Generate today's blog
    python generate_daily_blog.py --list   # Show all items in database
    python generate_daily_blog.py --force  # Force generation even if today exists
"""

import random
import json
import os
import sys
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# ─── Configuration ──────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent  # relictrek/
BLOG_DIR = BASE_DIR / "blog"
BLOG_ZH_DIR = BLOG_DIR / "zh"
BLOG_DB_FILE = BLOG_DIR / ".blog_database.json"

# All game items (game_dir, game_name, [item_slugs])
GAME_ITEMS = {
    "terraria": {
        "name": "Terraria",
        "zh_name": "泰拉瑞亚",
        "items": [
            ("ankh-shield", "Ankh Shield", "安卡盾"),
            ("zenith", "Zenith", "天顶剑"),
            ("cell-phone", "Cell Phone", "手机"),
            ("terra-blade", "Terra Blade", "泰拉之刃"),
            ("terraspark-boots", "Terraspark Boots", "泰拉闪耀靴"),
            ("avenger-emblem", "Avenger Emblem", "复仇者徽章"),
            ("frostspark-boots", "Frostspark Boots", "霜花靴"),
            ("ankh-charm", "Ankh Charm", "安卡护符"),
            ("pda", "PDA", "PDA"),
            ("nights-edge", "Night's Edge", "暗夜刃"),
        ]
    },
    "subnautica2": {
        "name": "Subnautica 2",
        "zh_name": "深海迷航2",
        "items": [
            ("tadpole", "Tadpole", "蝌蚪号"),
            ("scout-chassis", "Scout Chassis", "侦察机体"),
            ("depth-module-mk1", "Depth Module MK1", "深度模块MK1"),
            ("engine-efficiency", "Engine Efficiency Module", "引擎效率模块"),
            ("photovoltaic-charger", "Photovoltaic Charger", "光伏充电器"),
            ("sonic-resonator", "Sonic Resonator", "声波谐振器"),
            ("habitat-builder", "Habitat Builder", "基地建造器"),
            ("high-capacity-air-tank", "High Capacity Air Tank", "大容量氧气瓶"),
            ("rebreather", "Rebreather", "循环呼吸器"),
            ("thermal-reactor", "Thermal Reactor", "热反应堆"),
        ]
    },
    "monster-hunter-wilds": {
        "name": "Monster Hunter Wilds",
        "zh_name": "怪物猎人：荒野",
        "items": [
            ("rathalos-armor", "Rathalos Armor Set", "火龙防具套装"),
            ("nergigante-hammer", "Nergigante Hammer", "灭尽龙锤子"),
            ("legiana-bow", "Legiana Bow", "风漂龙弓"),
            ("charm-mighty", "Mighty Charm", "强力护石"),
            ("deviljho-greatsword", "Deviljho Greatsword", "恐暴龙大剑"),
            ("kirin-armor", "Kirin Armor Set", "麒麟防具套装"),
            ("teostra-longsword", "Teostra Longsword", "炎王龙太刀"),
            ("vaal-hazak-set", "Vaal Hazak Armor", "尸套龙防具"),
            ("attack-decorations", "Attack Decorations", "攻击珠"),
            ("xeno-jiiqa-lance", "Xeno'Jiiqa Lance", "冥灯龙长枪"),
        ]
    },
    "zelda-totk": {
        "name": "Zelda: Tears of the Kingdom",
        "zh_name": "塞尔达传说：王国之泪",
        "items": [
            ("master-sword", "Master Sword", "大师之剑"),
            ("hylian-shield", "Hylian Shield", "海利亚盾"),
            ("lightscale-trident", "Lightscale Trident", "光鳞之枪"),
            ("scimitar-seven", "Scimitar of the Seven", "七宝匕首"),
            ("great-eagle-bow", "Great Eagle Bow", "大鹫弓"),
            ("boulder-breaker", "Boulder Breaker", "碎岩巨剑"),
            ("fierce-deity-set", "Fierce Deity Set", "鬼神套装"),
            ("barbarian-set", "Barbarian Armor Set", "蛮族套装"),
            ("champions-leathers", "Champion's Leathers", "勇者皮衣"),
            ("radiant-set", "Radiant Armor Set", "夜光套装"),
        ]
    },
    "minecraft": {
        "name": "Minecraft",
        "zh_name": "我的世界",
        "items": [
            ("beacon", "Beacon", "信标"),
            ("netherite-armor", "Netherite Armor", "下界合金盔甲"),
            ("conduit", "Conduit", "潮涌核心"),
            ("enchanting-table", "Enchanting Table", "附魔台"),
            ("ender-chest", "Ender Chest", "末影箱"),
            ("slow-falling-potion", "Slow Falling Potion", "缓降药水"),
            ("anvil", "Anvil", "铁砧"),
            ("powered-rail", "Powered Rail", "动力铁轨"),
            ("eye-of-ender", "Eye of Ender", "末影之眼"),
            ("firework-rocket", "Firework Rocket", "烟花火箭"),
        ]
    },
    "no-mans-sky": {
        "name": "No Man's Sky",
        "zh_name": "无人深空",
        "items": [
            ("ai-valves", "AI Valves", "AI阀门"),
            ("fusion-ignitor", "Fusion Ignitor", "聚变点火器"),
            ("stasis-device", "Stasis Device", "停滞装置"),
            ("indium-drive", "Indium Drive", "铟驱动"),
            ("warp-hypercore", "Warp Hypercore", "跃迁超核"),
            ("minotaur-geobay", "Minotaur Geobay", "弥诺陶洛斯停靠站"),
            ("void-egg", "Void Egg", "虚空蛋"),
            ("multi-tool-s-class", "S-Class Multi-Tool", "S级多用途工具"),
            ("sentinel-exosuit", "Sentinel Exosuit", "护卫外骨骼"),
            ("underwater-module", "Underwater Module", "水下防护模块"),
        ]
    },
    "baldurs-gate-3": {
        "name": "Baldur's Gate 3",
        "zh_name": "博德之门3",
        "items": [
            ("blood-of-lathander", "Blood of Lathander", "洛山达之血"),
            ("gontr-mael", "Gontr Mael", "冈特·梅尔"),
            ("nyrulna", "Nyrulna", "尼鲁纳"),
            ("shars-spear", "Shar's Spear of Evening", "莎尔的黄昏之矛"),
            ("duellist-gloves", "Duellist's Prismatic Gloves", "决斗者的棱彩手套"),
            ("helldusk-armor", "Helldusk Armor", "地狱黄昏护甲"),
            ("moonlantern", "Moonlantern", "月亮提灯"),
            ("silver-sword", "Silver Sword of the Astral Plane", "星界银剑"),
            ("devilfoil-mask", "Devilfoil Mask", "魔鬼箔面具"),
            ("shadowheart-spear", "Shadowheart's Spear of Night", "暗影之心的夜之矛"),
        ]
    },
    "valheim": {
        "name": "Valheim",
        "zh_name": "英灵神殿",
        "items": [
            ("blackmetal-sword", "Blackmetal Sword", "黑金属剑"),
            ("bronze-mace", "Bronze Mace", "青铜钉锤"),
            ("carapace-armor", "Carapace Armor", "甲壳护甲"),
            ("draugr-fang", "Draugr Fang", "尸鬼之牙"),
            ("frostner", "Frostner", "霜牙钉锤"),
            ("iron-sledge", "Iron Sledge", "铁战锤"),
            ("padded-armor", "Padded Armor", "厚絮护甲"),
            ("porcupine", "Porcupine", "刺球钉锤"),
            ("stagbreaker", "Stagbreaker", "破鹿锤"),
            ("wolf-armor", "Wolf Armor", "狼皮护甲"),
        ]
    },
    "path-of-exile-2": {
        "name": "Path of Exile 2",
        "zh_name": "流放之路2",
        "items": [
            ("tabula-rasa", "Tabula Rasa", "纯白之袍"),
            ("headhunter", "Headhunter", "猎首"),
            ("mageblood", "Mageblood", "法师之血"),
            ("mirror-kalandra", "Mirror of Kalandra", "卡兰德的魔镜"),
            ("exalted-crafting", "Exalted Crafting", "崇高石合成"),
            ("six-link-armor", "Six-Link Armor", "六连护甲"),
            ("uncorrupted-vessel", "Uncorrupted 6-Mod Vessel", "未腐化6词容器"),
            ("regal-orb", "Regal Orb Farming", "富豪石刷取"),
            ("skill-gem", "Skill Gem", "技能石"),
            ("divine-orb", "Divine Orb Farming", "神圣石刷取"),
        ]
    },
    "elden-ring": {
        "name": "Elden Ring",
        "zh_name": "艾尔登法环",
        "items": [
            ("bewitching-branch", "Bewitching Branch", "魅惑树枝"),
            ("bloodboil-aromatic", "Bloodboil Aromatic", "狂热香药"),
            ("drawstring-blood-grease", "Drawstring Blood Grease", "缚血油脂"),
            ("exalted-flesh", "Exalted Flesh", "勇猛肉块"),
            ("gold-pickled-fowl-foot", "Gold-Pickled Fowl Foot", "黄金鸡爪"),
            ("ironjar-aromatic", "Ironjar Aromatic", "铁壶香药"),
            ("preserving-boluses", "Preserving Boluses", "腐败苔药"),
            ("spark-aromatic", "Spark Aromatic", "火花香药"),
            ("uplifting-aromatic", "Uplifting Aromatic", "振奋香药"),
            ("warming-stone", "Warming Stone", "暖石"),
        ]
    },
    "stardew-valley": {
        "name": "Stardew Valley",
        "zh_name": "星露谷物语",
        "items": [
            ("crystalarium", "Crystalarium", "宝石复制机"),
            ("iridium-band", "Iridium Band", "铱环"),
            ("keg", "Keg", "小桶"),
            ("seed-maker", "Seed Maker", "种子生产器"),
            ("lightning-rod", "Lightning Rod", "避雷针"),
            ("rain-totem", "Rain Totem", "雨水图腾"),
            ("slime-incubator", "Slime Incubator", "史莱姆孵化器"),
            ("warp-farm", "Warp Totem: Farm", "传送图腾：农场"),
            ("stairs", "Staircase", "楼梯"),
            ("wicked-statue", "Wicked Statue", "邪恶雕像"),
        ]
    },
    "hades-2": {
        "name": "Hades 2",
        "zh_name": "哈迪斯2",
        "items": [
            ("permeation-wards", "Permeation of Wards", "女巫结界的渗透"),
            ("unraveling-fateful-bond", "Unraveling a Fateful Bond", "解开宿命之缚"),
            ("aspects-night-darkness", "Aspects of Night & Darkness", "黑夜与黑暗之形态"),
            ("insight-offerings", "Insight Offerings", "祭品洞察"),
            ("consecration-ashes", "Consecration of Ashes", "灰烬祝圣"),
            ("shimmering-ambrosia", "Shimmering Ambrosia", "闪耀仙馔"),
            ("shadow-extraction", "Shadow Extraction", "暗影萃取"),
            ("greater-favor-gaia", "Greater Favor of Gaia", "盖亚的更大恩惠"),
            ("rite-vapor-cleansing", "Rite of Vapor Cleansing", "蒸汽净化仪式"),
            ("surge-stygian-wells", "Surge of Stygian Wells", "冥河之泉的涌动"),
        ]
    },
    "satisfactory": {
        "name": "Satisfactory",
        "zh_name": "幸福工厂",
        "items": [
            ("cast-screws", "Cast Screws", "铸造螺丝"),
            ("copper-alloy-ingot", "Copper Alloy Ingot", "铜合金锭"),
            ("diluted-fuel", "Diluted Fuel", "稀释燃料"),
            ("fused-wire", "Fused Wire", "熔合线"),
            ("heavy-encased-frame", "Heavy Encased Frame", "重型封装框架"),
            ("pure-ingots", "Pure Ingots", "纯净锭块"),
            ("recycled-plastic", "Recycled Plastic", "回收塑料"),
            ("silicon-circuit-board", "Silicon Circuit Board", "硅电路板"),
            ("steel-screw", "Steel Screw", "钢制螺丝"),
            ("stitched-iron-plate", "Stitched Iron Plate", "缝合铁板"),
        ]
    },
}

# ─── Blog Database Management ──────────────────────────────────────

def load_blog_database():
    """Load blog history database"""
    if BLOG_DB_FILE.exists():
        with open(BLOG_DB_FILE, 'r') as f:
            return json.load(f)
    return {"posts": [], "last_post_date": None, "items_blogged": []}

def save_blog_database(db):
    """Save blog history database"""
    with open(BLOG_DB_FILE, 'w') as f:
        json.dump(db, f, indent=2)

def select_random_item(db):
    """Select a random item that hasn't been blogged about"""
    blogged = set(db.get("items_blogged", []))
    
    all_items = []
    for game_dir, game_data in GAME_ITEMS.items():
        for item_slug, item_name, item_zh_name in game_data["items"]:
            key = f"{game_dir}/{item_slug}"
            if key not in blogged:
                all_items.append({
                    "key": key,
                    "game_dir": game_dir,
                    "game_name": game_data["name"],
                    "game_zh_name": game_data["zh_name"],
                    "slug": item_slug,
                    "name": item_name,
                    "zh_name": item_zh_name,
                })
    
    if not all_items:
        # All items have been blogged, reset
        print("All items have been blogged! Resetting database...")
        db["items_blogged"] = []
        save_blog_database(db)
        return select_random_item(db)
    
    return random.choice(all_items)

# ─── Blog Content Generation ───────────────────────────────────────

def generate_blog_content(item):
    """Generate blog content for the selected item"""
    
    game_name = item["game_name"]
    item_name = item["name"]
    item_zh_name = item["zh_name"]
    game_zh_name = item["game_zh_name"]
    
    today = datetime.now().strftime("%B %d, %Y")
    today_zh = datetime.now().strftime("%Y年%m月%d日")
    
    # English blog content
    en_content = f"""<article class="blog-post">
  <h1>{item_name} in {game_name}: Why Players Can't Stop Talking About It</h1>
  <p class="blog-meta">Published on {today} | RelicTrek Daily</p>
  
  <div class="blog-body">
    <p>{item_name} remains one of the most sought-after items in {game_name}, and the community buzz around it has only grown louder in recent weeks. From Reddit threads to YouTube tutorials, players are sharing their experiences, shortcuts, and frustrations about obtaining this rare crafting component.</p>
    
    <h2>What Makes {item_name} Special</h2>
    <p>In the world of {game_name}, few items command the same level of respect and desire as {item_name}. Whether you're a completionist aiming for 100% achievement unlock or a power gamer seeking the ultimate loadout, this item represents a significant milestone in your journey.</p>
    
    <p>According to community reports, the average player spends between 15-30 hours farming the necessary materials. But with the right strategy — the kind we break down step-by-step in our <a href="../{item['game_dir']}/{item['slug']}.html" style="color: var(--accent);">complete {item_name} guide</a> — you can cut that time in half.</p>
    
    <h2>Community Spotlight: Top Tips from Reddit</h2>
    <p>We scoured the most popular discussions from the past 30 days and compiled the top community tips:</p>
    
    <ul>
      <li><strong>Patience pays off:</strong> Many players report that rushing the process leads to mistakes. Take time to understand each material requirement before heading out.</li>
      <li><strong>Route optimization is key:</strong> The most upvoted strategy threads all emphasize planning your farming route in advance to minimize backtracking.</li>
      <li><strong>Don't skip the prep work:</strong> Players who invest in prerequisites (upgraded gear, inventory space, fast travel points) report significantly faster completion times.</li>
    </ul>
    
    <h2>Why Now Is the Perfect Time to Craft {item_name}</h2>
    <p>With recent game updates and a surge in new player activity, the community has never been more helpful. Discord servers are buzzing with veterans offering escort services, and wiki pages are being updated daily with the latest drop rate data.</p>
    
    <p>If you've been putting off crafting {item_name}, now is the time. Check out our <a href="../{item['game_dir']}/{item['slug']}.html" style="color: var(--accent);">detailed step-by-step guide</a> with exact material locations, optimal farming routes, and gotcha warnings.</p>
    
    <h2>Related Guides</h2>
    <p>Explore more {game_name} crafting guides in our <a href="../{item['game_dir']}/" style="color: var(--accent);">complete {game_name} section</a>.</p>
  </div>
</article>"""

    # Chinese blog content
    zh_content = f"""<article class="blog-post">
  <h1>{game_zh_name}{item_zh_name}：为什么玩家们都在讨论它</h1>
  <p class="blog-meta">发布于 {today_zh} | RelicTrek 每日精选</p>
  
  <div class="blog-body">
    <p>{item_zh_name}至今仍是{game_zh_name}中最受追捧的物品之一，而最近几周围绕它的社区热度更是持续升温。从Reddit讨论帖到YouTube攻略视频，玩家们纷纷分享自己的获取经历、捷径技巧和各种让人哭笑不得的翻车故事。</p>
    
    <h2>{item_zh_name}为什么如此特别</h2>
    <p>在{game_zh_name}的世界中，很少有物品能像{item_zh_name}一样获得如此高的尊重和渴望。无论你是追求100%成就解锁的 completionist，还是寻求终极配装的核心玩家，这件物品都代表着游戏旅程中的一个重要里程碑。</p>
    
    <p>根据社区报告，普通玩家平均需要花费15-30小时来刷取所需材料。但只要有正确的策略——就像我们在<a href="../{item['game_dir']}/zh/{item['slug']}.html" style="color: var(--accent);">完整{item_zh_name}攻略</a>中详细拆解的那样——你可以将这个时间缩短一半。</p>
    
    <h2>社区精选：Reddit热门技巧</h2>
    <p>我们搜集了过去30天最热门的讨论帖，整理了社区高赞技巧：</p>
    
    <ul>
      <li><strong>耐心就是效率：</strong>很多玩家反馈说急着赶路反而会犯错。出发前花点时间了解每个材料的需求，事半功倍。</li>
      <li><strong>路线规划是关键：</strong>所有高赞策略帖都强调提前规划刷取路线的重要性，减少来回奔波。</li>
      <li><strong>准备工作不能省：</strong>那些在准备工作上投入的玩家（升级装备、扩充背包、解锁传送点）反馈说完成速度快得多。</li>
    </ul>
    
    <h2>为什么现在是合成{item_zh_name}的最佳时机</h2>
    <p>随着近期的游戏更新和新玩家的大量涌入，社区从未如此活跃。Discord服务器里老玩家们纷纷提供带路服务，Wiki页面也在每日更新最新的掉率数据。</p>
    
    <p>如果你一直在拖延合成{item_zh_name}的计划，现在就是最好的时机。查看我们的<a href="../{item['game_dir']}/zh/{item['slug']}.html" style="color: var(--accent);">详细分步攻略</a>，包含精确材料位置、最优刷取路线和避坑警告。</p>
    
    <h2>相关攻略</h2>
    <p>探索更多{game_zh_name}合成攻略，请访问我们的<a href="../{item['game_dir']}/zh/" style="color: var(--accent);">完整{game_zh_name}攻略区</a>。</p>
  </div>
</article>"""

    return en_content, zh_content

# ─── HTML Page Generation ──────────────────────────────────────────

def generate_blog_html(content, lang="en", is_zh=False):
    """Generate a complete blog HTML page"""
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    date_display = datetime.now().strftime("%B %d, %Y") if lang == "en" else datetime.now().strftime("%Y年%m月%d日")
    
    html_lang = "zh-CN" if is_zh else "en"
    title_prefix = "博客" if is_zh else "Blog"
    search_placeholder = "搜索物品..." if is_zh else "Search items (e.g. Ankh Shield)..."
    
    if is_zh:
        en_link = f"../{date_str}.html"
        zh_link = "./"
        css_path = "../../css/style.css"  # blog/zh/ -> need ../../ to reach root
        js_path = "../../js/main.js"
        root_link = "../../"
        blog_link = "./"
        about_link = "../../about.html"
        game_nav_prefix = "../../"
    else:
        en_link = "./"
        zh_link = f"./zh/{date_str}.html"
        css_path = "../css/style.css"
        js_path = "../js/main.js"
        root_link = "../"
        blog_link = "./"
        about_link = "../about.html"
        game_nav_prefix = "../"
    
    # Game navigation
    nav_items = ""
    for game_dir, game_data in GAME_ITEMS.items():
        game_name_display = game_data["zh_name"] if is_zh else game_data["name"]
        if is_zh:
            nav_items += f'      <a href="{game_nav_prefix}{game_dir}/zh/">{game_name_display}</a>\n'
        else:
            nav_items += f'      <a href="{game_nav_prefix}{game_dir}/">{game_name_display}</a>\n'
    
    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-Z2SC4S5VZ9"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-Z2SC4S5VZ9');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_prefix} — RelicTrek Gaming News & Stories</title>
<meta name="description" content="Daily gaming news, crafting tips, and stories from the world of rare game items.">
<link rel="stylesheet" href="{css_path}">
<style>
.blog-post h1 {{ font-size: 28px; margin-bottom: 12px; color: var(--accent); line-height: 1.3; }}
.blog-post h2 {{ font-size: 20px; margin: 28px 0 12px; color: var(--text); border-bottom: 1px solid var(--border); padding-bottom: 8px; }}
.blog-meta {{ color: var(--text-muted); font-size: 14px; margin-bottom: 24px; font-style: italic; }}
.blog-body p {{ margin-bottom: 16px; line-height: 1.8; color: var(--text-muted); }}
.blog-body ul {{ margin: 12px 0 12px 20px; }}
.blog-body li {{ margin-bottom: 8px; line-height: 1.7; color: var(--text-muted); }}
.blog-body strong {{ color: var(--text); }}
.blog-list {{ list-style: none; margin: 0; padding: 0; }}
.blog-list-item {{ padding: 16px 0; border-bottom: 1px solid var(--border); }}
.blog-list-item:last-child {{ border-bottom: none; }}
.blog-list-item a {{ color: var(--accent); font-size: 17px; font-weight: 700; text-decoration: none; }}
.blog-list-item a:hover {{ text-decoration: underline; }}
.blog-list-item .date {{ color: var(--text-muted); font-size: 13px; margin-top: 4px; }}
</style>
</head>
<body>

<nav class="top-nav">
  <button class="menu-toggle" aria-label="Open menu">&#9776;</button>
  <a href="{root_link}" class="logo">RelicTrek</a>
  <input type="search" placeholder="{search_placeholder}" aria-label="Search">
  <div class="lang-switch">
    <button data-lang="en" onclick="window.location.href='{en_link}'" title="English">EN</button>
    <button data-lang="zh" onclick="window.location.href='{zh_link}'" title="Chinese" class="{'active' if is_zh else ''}">中文</button>
  </div>
  <div class="nav-links">
    <a href="{blog_link}" class="active">{'博客' if is_zh else 'Blog'}</a>
    <a href="{root_link}">{'游戏' if is_zh else 'Games'}</a>
    <a href="{about_link}">{'关于' if is_zh else 'About'}</a>
  </div>
</nav>

<div class="ticker-bar">
  <div class="ticker-track">
    <span class="ticker-item">
      <span class="slogan-main-text">What You Don't Know You're Missing</span>
      <span class="sep">|</span>
      <span class="slogan-sub-text">The Best Items Hide in Plain Sight</span>
    </span>
  </div>
</div>

<div class="main-layout">
  <aside class="left-sidebar">
    <h3>{'游戏' if is_zh else 'Games'}</h3>
{nav_items}  </aside>

  <main class="content-area">
    {content}
  </main>

  <aside class="right-sidebar">
    <div class="ad-slot">Ad Space</div>
    <h4>{'热门攻略' if is_zh else 'Popular Guides'}</h4>
  </aside>
</div>

<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <div class="footer-logo">&#9676; RelicTrek</div>
      <p class="footer-tagline">Every legendary item has a story. We map the journey.</p>
    </div>
    <div class="footer-links">
      <div class="footer-col">
        <div class="footer-col-title">RelicTrek</div>
        <a href="{root_link}privacy.html">{'隐私政策' if is_zh else 'Privacy'}</a>
        <a href="{root_link}terms.html">{'使用条款' if is_zh else 'Terms'}</a>
        <a href="{root_link}about.html">{'关于' if is_zh else 'About'}</a>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <span>&copy; 2025 RelicTrek.net</span>
    <span class="footer-sep">&#9676;</span>
    <span>Crafted for adventurers</span>
  </div>
</footer>

<script src="{js_path}"></script>
</body>
</html>"""

# ─── Main Execution ────────────────────────────────────────────────

def main():
    """Main blog generation routine"""
    
    force = "--force" in sys.argv
    list_items = "--list" in sys.argv
    
    # Load database
    db = load_blog_database()
    
    if list_items:
        print("=== All game items ===")
        for game_dir, game_data in GAME_ITEMS.items():
            print(f"\n{game_data['name']}:")
            for slug, name, zh_name in game_data["items"]:
                key = f"{game_dir}/{slug}"
                status = "✅ BLOGGED" if key in db.get("items_blogged", []) else "⬜ Available"
                print(f"  {status} {name} ({zh_name})")
        return
    
    # Check if today already has a post
    today_str = datetime.now().strftime("%Y-%m-%d")
    if not force and db.get("last_post_date") == today_str:
        print(f"Blog already generated for {today_str}. Use --force to regenerate.")
        return
    
    # Select random item
    item = select_random_item(db)
    print(f"Selected item: {item['name']} ({item['zh_name']}) from {item['game_name']}")
    
    # Generate content
    en_content, zh_content = generate_blog_content(item)
    
    # Generate English blog page
    date_str = datetime.now().strftime("%Y-%m-%d")
    en_html = generate_blog_html(en_content, lang="en", is_zh=False)
    en_path = BLOG_DIR / f"{date_str}.html"
    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(en_html)
    print(f"✅ English blog: blog/{date_str}.html")
    
    # Generate Chinese blog page
    zh_html = generate_blog_html(zh_content, lang="zh", is_zh=True)
    zh_path = BLOG_ZH_DIR / f"{date_str}.html"
    with open(zh_path, 'w', encoding='utf-8') as f:
        f.write(zh_html)
    print(f"✅ Chinese blog: blog/zh/{date_str}.html")
    
    # Update database
    db["posts"].append({
        "date": today_str,
        "item_key": item["key"],
        "item_name": item["name"],
        "item_zh_name": item["zh_name"],
        "game": item["game_name"],
    })
    db["last_post_date"] = today_str
    db["items_blogged"].append(item["key"])
    save_blog_database(db)
    
    # Update blog index pages with link to new post
    update_blog_index(date_str, item, db)
    
    print(f"\n🎉 Blog post for {date_str} generated successfully!")
    print(f"   Item: {item['name']} from {item['game_name']}")
    print(f"   EN: blog/{date_str}.html")
    print(f"   ZH: blog/zh/{date_str}.html")

def update_blog_index(date_str, item, db):
    """Update blog index pages to include new post link"""
    
    # Get recent posts for index
    recent_posts = db["posts"][-10:][::-1]  # Last 10, newest first
    
    # English index
    en_index = BLOG_DIR / "index.html"
    if en_index.exists():
        with open(en_index, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add blog post link
        post_links = ""
        for post in recent_posts:
            post_date = post["date"]
            display_date = datetime.strptime(post_date, "%Y-%m-%d").strftime("%B %d, %Y")
            post_title = f"{post['item_name']} in {post['game']}"
            post_links += f'      <li class="blog-list-item"><a href="{post_date}.html">{post_title}</a><div class="date">{display_date}</div></li>\n'
        
        # Replace or add blog list
        if '<ul class="blog-list">' in content:
            content = re.sub(
                r'<ul class="blog-list">.*?</ul>',
                f'<ul class="blog-list">\n{post_links}    </ul>',
                content,
                flags=re.DOTALL
            )
        
        with open(en_index, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Chinese index
    zh_index = BLOG_ZH_DIR / "index.html"
    if zh_index.exists():
        with open(zh_index, 'r', encoding='utf-8') as f:
            content = f.read()
        
        post_links = ""
        for post in recent_posts:
            post_date = post["date"]
            display_date = datetime.strptime(post_date, "%Y-%m-%d").strftime("%Y年%m月%d日")
            post_title = f"{post['game']} {post['item_zh_name']}"
            post_links += f'      <li class="blog-list-item"><a href="{post_date}.html">{post_title}</a><div class="date">{display_date}</div></li>\n'
        
        if '<ul class="blog-list">' in content:
            content = re.sub(
                r'<ul class="blog-list">.*?</ul>',
                f'<ul class="blog-list">\n{post_links}    </ul>',
                content,
                flags=re.DOTALL
            )
        
        with open(zh_index, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    main()
