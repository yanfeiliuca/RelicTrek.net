# RelicTrek 全站中英文链接结构对等性审计报告

**审计时间**: 2025年

**审计范围**: 13个游戏，共286个HTML页面（143 EN + 143 ZH），外加14个根级/博客页面

---

## 一、总体摘要

| 游戏 | EN页数 | ZH页数 | 问题数 | 状态 |
|------|--------|--------|--------|------|
| Terraria | 11 | 11 | 31 | ⚠️ 31个问题 |
| Subnautica2 | 11 | 11 | 31 | ⚠️ 31个问题 |
| Monster Hunter Wilds | 11 | 11 | 81 | ⚠️ 81个问题 |
| Zelda Totk | 11 | 11 | 31 | ⚠️ 31个问题 |
| Minecraft | 11 | 11 | 35 | ⚠️ 35个问题 |
| No Mans Sky | 11 | 11 | 31 | ⚠️ 31个问题 |
| Baldurs Gate 3 | 11 | 11 | 21 | ⚠️ 21个问题 |
| Valheim | 11 | 11 | 31 | ⚠️ 31个问题 |
| Path Of Exile 2 | 11 | 11 | 26 | ⚠️ 26个问题 |
| Elden Ring | 11 | 11 | 41 | ⚠️ 41个问题 |
| Stardew Valley | 11 | 11 | 31 | ⚠️ 31个问题 |
| Hades 2 | 11 | 11 | 21 | ⚠️ 21个问题 |
| Satisfactory | 11 | 11 | 41 | ⚠️ 41个问题 |
| **合计** | **143** | **143** | **452** | |

### 问题分类统计

| 问题类型 | 数量 | 严重程度 |
|----------|------|----------|
| EN/ZH body class不对等 (EN缺lang-en) | 130 | 高 |
| EN语言按钮缺少active/disabled | 105 | 中 |
| EN页面缺少body class='lang-en' | 94 | 高 |
| ZH页面导航链接路径错误（应使用../../） | 40 | 高 |
| EN页面CSS路径错误 | 26 | 中 |
| 语言按钮缺失 | 20 | 高 |
| EN页面中文按钮缺少onclick | 19 | 中 |
| EN/ZH语言切换按钮不对等 | 16 | 高 |
| EN/ZH top-nav不对等 | 2 | 中 |

---

## 二、各游戏详细检查汇总

### Terraria

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 31个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| terraria/ankh-charm.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| terraria/ankh-charm.html | EN语言按钮缺少active/disabled class |
| terraria/ankh-shield.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| terraria/ankh-shield.html | EN语言按钮缺少active/disabled class |
| terraria/avenger-emblem.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| terraria/avenger-emblem.html | EN语言按钮缺少active/disabled class |
| terraria/cell-phone.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| terraria/cell-phone.html | EN语言按钮缺少active/disabled class |
| terraria/frostspark-boots.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| terraria/frostspark-boots.html | EN语言按钮缺少active/disabled class |
| terraria/index.html | EN语言按钮缺少active/disabled class |
| terraria/nights-edge.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| terraria/nights-edge.html | EN语言按钮缺少active/disabled class |
| terraria/pda.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| terraria/pda.html | EN语言按钮缺少active/disabled class |
| terraria/terra-blade.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| terraria/terra-blade.html | EN语言按钮缺少active/disabled class |
| terraria/terraspark-boots.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| terraria/terraspark-boots.html | EN语言按钮缺少active/disabled class |
| terraria/zenith.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| terraria/zenith.html | EN语言按钮缺少active/disabled class |
| terraria/ankh-charm.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| terraria/terraspark-boots.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| terraria/pda.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| terraria/zenith.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| terraria/ankh-shield.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| terraria/nights-edge.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| terraria/avenger-emblem.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| terraria/cell-phone.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| terraria/terra-blade.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| terraria/frostspark-boots.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |

### Subnautica2

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 31个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| subnautica2/depth-module-mk1.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| subnautica2/depth-module-mk1.html | EN语言按钮缺少active/disabled class |
| subnautica2/engine-efficiency.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| subnautica2/engine-efficiency.html | EN语言按钮缺少active/disabled class |
| subnautica2/habitat-builder.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| subnautica2/habitat-builder.html | EN语言按钮缺少active/disabled class |
| subnautica2/high-capacity-air-tank.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| subnautica2/high-capacity-air-tank.html | EN语言按钮缺少active/disabled class |
| subnautica2/index.html | EN语言按钮缺少active/disabled class |
| subnautica2/photovoltaic-charger.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| subnautica2/photovoltaic-charger.html | EN语言按钮缺少active/disabled class |
| subnautica2/rebreather.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| subnautica2/rebreather.html | EN语言按钮缺少active/disabled class |
| subnautica2/scout-chassis.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| subnautica2/scout-chassis.html | EN语言按钮缺少active/disabled class |
| subnautica2/sonic-resonator.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| subnautica2/sonic-resonator.html | EN语言按钮缺少active/disabled class |
| subnautica2/tadpole.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| subnautica2/tadpole.html | EN语言按钮缺少active/disabled class |
| subnautica2/thermal-reactor.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| subnautica2/thermal-reactor.html | EN语言按钮缺少active/disabled class |
| subnautica2/habitat-builder.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| subnautica2/scout-chassis.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| subnautica2/photovoltaic-charger.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| subnautica2/thermal-reactor.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| subnautica2/rebreather.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| subnautica2/sonic-resonator.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| subnautica2/engine-efficiency.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| subnautica2/depth-module-mk1.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| subnautica2/tadpole.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| subnautica2/high-capacity-air-tank.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |

### Monster Hunter Wilds

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 81个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| monster-hunter-wilds/attack-decorations.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| monster-hunter-wilds/attack-decorations.html | EN语言按钮缺少active/disabled class |
| monster-hunter-wilds/charm-mighty.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| monster-hunter-wilds/charm-mighty.html | EN语言按钮缺少active/disabled class |
| monster-hunter-wilds/deviljho-greatsword.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| monster-hunter-wilds/deviljho-greatsword.html | EN语言按钮缺少active/disabled class |
| monster-hunter-wilds/index.html | EN语言按钮缺少active/disabled class |
| monster-hunter-wilds/kirin-armor.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| monster-hunter-wilds/kirin-armor.html | EN语言按钮缺少active/disabled class |
| monster-hunter-wilds/legiana-bow.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| monster-hunter-wilds/legiana-bow.html | EN语言按钮缺少active/disabled class |
| monster-hunter-wilds/nergigante-hammer.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| monster-hunter-wilds/nergigante-hammer.html | EN语言按钮缺少active/disabled class |
| monster-hunter-wilds/rathalos-armor.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| monster-hunter-wilds/rathalos-armor.html | EN语言按钮缺少active/disabled class |
| monster-hunter-wilds/teostra-longsword.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| monster-hunter-wilds/teostra-longsword.html | EN语言按钮缺少active/disabled class |
| monster-hunter-wilds/vaal-hazak-set.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| monster-hunter-wilds/vaal-hazak-set.html | EN语言按钮缺少active/disabled class |
| monster-hunter-wilds/xeno-jiiqa-lance.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| monster-hunter-wilds/xeno-jiiqa-lance.html | EN语言按钮缺少active/disabled class |
| monster-hunter-wilds/zh/attack-decorations.html | lang-switch中缺少data-lang='zh'按钮 |
| monster-hunter-wilds/zh/attack-decorations.html | lang-switch中缺少data-lang='en'按钮 |
| monster-hunter-wilds/zh/attack-decorations.html | ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/attack-decorations.html | ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/attack-decorations.html | ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/charm-mighty.html | lang-switch中缺少data-lang='zh'按钮 |
| monster-hunter-wilds/zh/charm-mighty.html | lang-switch中缺少data-lang='en'按钮 |
| monster-hunter-wilds/zh/charm-mighty.html | ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/charm-mighty.html | ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/charm-mighty.html | ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/deviljho-greatsword.html | lang-switch中缺少data-lang='zh'按钮 |
| monster-hunter-wilds/zh/deviljho-greatsword.html | lang-switch中缺少data-lang='en'按钮 |
| monster-hunter-wilds/zh/deviljho-greatsword.html | ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/deviljho-greatsword.html | ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/deviljho-greatsword.html | ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/kirin-armor.html | lang-switch中缺少data-lang='zh'按钮 |
| monster-hunter-wilds/zh/kirin-armor.html | lang-switch中缺少data-lang='en'按钮 |
| monster-hunter-wilds/zh/kirin-armor.html | ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/kirin-armor.html | ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/kirin-armor.html | ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/legiana-bow.html | lang-switch中缺少data-lang='zh'按钮 |
| monster-hunter-wilds/zh/legiana-bow.html | lang-switch中缺少data-lang='en'按钮 |
| monster-hunter-wilds/zh/legiana-bow.html | ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/legiana-bow.html | ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/legiana-bow.html | ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/nergigante-hammer.html | lang-switch中缺少data-lang='zh'按钮 |
| monster-hunter-wilds/zh/nergigante-hammer.html | lang-switch中缺少data-lang='en'按钮 |
| monster-hunter-wilds/zh/nergigante-hammer.html | ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/nergigante-hammer.html | ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/nergigante-hammer.html | ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/rathalos-armor.html | lang-switch中缺少data-lang='zh'按钮 |
| monster-hunter-wilds/zh/rathalos-armor.html | lang-switch中缺少data-lang='en'按钮 |
| monster-hunter-wilds/zh/rathalos-armor.html | ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/rathalos-armor.html | ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/rathalos-armor.html | ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/teostra-longsword.html | lang-switch中缺少data-lang='zh'按钮 |
| monster-hunter-wilds/zh/teostra-longsword.html | lang-switch中缺少data-lang='en'按钮 |
| monster-hunter-wilds/zh/teostra-longsword.html | ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/teostra-longsword.html | ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/teostra-longsword.html | ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/vaal-hazak-set.html | lang-switch中缺少data-lang='zh'按钮 |
| monster-hunter-wilds/zh/vaal-hazak-set.html | lang-switch中缺少data-lang='en'按钮 |
| monster-hunter-wilds/zh/vaal-hazak-set.html | ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/vaal-hazak-set.html | ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/vaal-hazak-set.html | ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/xeno-jiiqa-lance.html | lang-switch中缺少data-lang='zh'按钮 |
| monster-hunter-wilds/zh/xeno-jiiqa-lance.html | lang-switch中缺少data-lang='en'按钮 |
| monster-hunter-wilds/zh/xeno-jiiqa-lance.html | ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/xeno-jiiqa-lance.html | ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/zh/xeno-jiiqa-lance.html | ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../') |
| monster-hunter-wilds/nergigante-hammer.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| monster-hunter-wilds/xeno-jiiqa-lance.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| monster-hunter-wilds/kirin-armor.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| monster-hunter-wilds/deviljho-greatsword.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| monster-hunter-wilds/vaal-hazak-set.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| monster-hunter-wilds/legiana-bow.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| monster-hunter-wilds/teostra-longsword.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| monster-hunter-wilds/rathalos-armor.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| monster-hunter-wilds/charm-mighty.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| monster-hunter-wilds/attack-decorations.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |

### Zelda Totk

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 31个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| zelda-totk/barbarian-set.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| zelda-totk/barbarian-set.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| zelda-totk/champions-leathers.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| zelda-totk/fierce-deity-set.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| zelda-totk/fierce-deity-set.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| zelda-totk/hylian-shield.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| zelda-totk/hylian-shield.html | EN语言按钮缺少active/disabled class |
| zelda-totk/index.html | EN语言按钮缺少active/disabled class |
| zelda-totk/lightscale-trident.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| zelda-totk/lightscale-trident.html | EN语言按钮缺少active/disabled class |
| zelda-totk/master-sword.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| zelda-totk/master-sword.html | EN语言按钮缺少active/disabled class |
| zelda-totk/radiant-set.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| zelda-totk/scimitar-seven.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| zelda-totk/scimitar-seven.html | EN语言按钮缺少active/disabled class |
| zelda-totk/scimitar-seven.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| zelda-totk/champions-leathers.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| zelda-totk/champions-leathers.html / zelda-totk/zh/champions-leathers.html | 语言切换按钮不对等: EN=False, ZH=True |
| zelda-totk/radiant-set.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| zelda-totk/radiant-set.html / zelda-totk/zh/radiant-set.html | 语言切换按钮不对等: EN=False, ZH=True |
| zelda-totk/hylian-shield.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| zelda-totk/great-eagle-bow.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| zelda-totk/great-eagle-bow.html / zelda-totk/zh/great-eagle-bow.html | 语言切换按钮不对等: EN=False, ZH=True |
| zelda-totk/great-eagle-bow.html / zelda-totk/zh/great-eagle-bow.html | top-nav不对等: EN=False, ZH=True |
| zelda-totk/barbarian-set.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| zelda-totk/boulder-breaker.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| zelda-totk/boulder-breaker.html / zelda-totk/zh/boulder-breaker.html | 语言切换按钮不对等: EN=False, ZH=True |
| zelda-totk/boulder-breaker.html / zelda-totk/zh/boulder-breaker.html | top-nav不对等: EN=False, ZH=True |
| zelda-totk/fierce-deity-set.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| zelda-totk/lightscale-trident.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| zelda-totk/master-sword.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |

### Minecraft

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 35个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| minecraft/anvil.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| minecraft/anvil.html | EN语言按钮缺少active/disabled class |
| minecraft/anvil.html | 中文语言按钮缺少onclick跳转 |
| minecraft/beacon.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| minecraft/beacon.html | EN语言按钮缺少active/disabled class |
| minecraft/conduit.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| minecraft/enchanting-table.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| minecraft/ender-chest.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| minecraft/ender-chest.html | EN语言按钮缺少active/disabled class |
| minecraft/eye-of-ender.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| minecraft/eye-of-ender.html | EN语言按钮缺少active/disabled class |
| minecraft/eye-of-ender.html | 中文语言按钮缺少onclick跳转 |
| minecraft/firework-rocket.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| minecraft/firework-rocket.html | EN语言按钮缺少active/disabled class |
| minecraft/firework-rocket.html | 中文语言按钮缺少onclick跳转 |
| minecraft/index.html | EN语言按钮缺少active/disabled class |
| minecraft/netherite-armor.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| minecraft/netherite-armor.html | EN语言按钮缺少active/disabled class |
| minecraft/powered-rail.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| minecraft/powered-rail.html | EN语言按钮缺少active/disabled class |
| minecraft/powered-rail.html | 中文语言按钮缺少onclick跳转 |
| minecraft/slow-falling-potion.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| minecraft/slow-falling-potion.html | EN语言按钮缺少active/disabled class |
| minecraft/slow-falling-potion.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| minecraft/enchanting-table.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| minecraft/enchanting-table.html / minecraft/zh/enchanting-table.html | 语言切换按钮不对等: EN=False, ZH=True |
| minecraft/eye-of-ender.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| minecraft/anvil.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| minecraft/beacon.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| minecraft/netherite-armor.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| minecraft/ender-chest.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| minecraft/firework-rocket.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| minecraft/powered-rail.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| minecraft/conduit.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| minecraft/conduit.html / minecraft/zh/conduit.html | 语言切换按钮不对等: EN=False, ZH=True |

### No Mans Sky

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 31个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| no-mans-sky/ai-valves.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| no-mans-sky/ai-valves.html | EN语言按钮缺少active/disabled class |
| no-mans-sky/fusion-ignitor.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| no-mans-sky/fusion-ignitor.html | EN语言按钮缺少active/disabled class |
| no-mans-sky/index.html | EN语言按钮缺少active/disabled class |
| no-mans-sky/indium-drive.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| no-mans-sky/indium-drive.html | EN语言按钮缺少active/disabled class |
| no-mans-sky/minotaur-geobay.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| no-mans-sky/minotaur-geobay.html | EN语言按钮缺少active/disabled class |
| no-mans-sky/multi-tool-s-class.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| no-mans-sky/multi-tool-s-class.html | EN语言按钮缺少active/disabled class |
| no-mans-sky/sentinel-exosuit.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| no-mans-sky/sentinel-exosuit.html | EN语言按钮缺少active/disabled class |
| no-mans-sky/stasis-device.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| no-mans-sky/stasis-device.html | EN语言按钮缺少active/disabled class |
| no-mans-sky/underwater-module.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| no-mans-sky/underwater-module.html | EN语言按钮缺少active/disabled class |
| no-mans-sky/void-egg.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| no-mans-sky/void-egg.html | EN语言按钮缺少active/disabled class |
| no-mans-sky/warp-hypercore.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| no-mans-sky/warp-hypercore.html | EN语言按钮缺少active/disabled class |
| no-mans-sky/multi-tool-s-class.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| no-mans-sky/stasis-device.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| no-mans-sky/void-egg.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| no-mans-sky/ai-valves.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| no-mans-sky/minotaur-geobay.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| no-mans-sky/fusion-ignitor.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| no-mans-sky/sentinel-exosuit.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| no-mans-sky/warp-hypercore.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| no-mans-sky/indium-drive.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| no-mans-sky/underwater-module.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |

### Baldurs Gate 3

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 21个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| baldurs-gate-3/devilfoil-mask.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| baldurs-gate-3/devilfoil-mask.html | EN语言按钮缺少active/disabled class |
| baldurs-gate-3/helldusk-armor.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| baldurs-gate-3/helldusk-armor.html | EN语言按钮缺少active/disabled class |
| baldurs-gate-3/index.html | EN语言按钮缺少active/disabled class |
| baldurs-gate-3/moonlantern.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| baldurs-gate-3/moonlantern.html | EN语言按钮缺少active/disabled class |
| baldurs-gate-3/shadowheart-spear.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| baldurs-gate-3/shadowheart-spear.html | EN语言按钮缺少active/disabled class |
| baldurs-gate-3/silver-sword.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| baldurs-gate-3/silver-sword.html | EN语言按钮缺少active/disabled class |
| baldurs-gate-3/gontr-mael.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| baldurs-gate-3/blood-of-lathander.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| baldurs-gate-3/devilfoil-mask.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| baldurs-gate-3/nyrulna.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| baldurs-gate-3/shars-spear.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| baldurs-gate-3/helldusk-armor.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| baldurs-gate-3/shadowheart-spear.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| baldurs-gate-3/duellist-gloves.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| baldurs-gate-3/moonlantern.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| baldurs-gate-3/silver-sword.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |

### Valheim

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 31个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| valheim/blackmetal-sword.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| valheim/blackmetal-sword.html | EN语言按钮缺少active/disabled class |
| valheim/bronze-mace.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| valheim/bronze-mace.html | EN语言按钮缺少active/disabled class |
| valheim/carapace-armor.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| valheim/carapace-armor.html | EN语言按钮缺少active/disabled class |
| valheim/draugr-fang.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| valheim/draugr-fang.html | EN语言按钮缺少active/disabled class |
| valheim/frostner.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| valheim/frostner.html | EN语言按钮缺少active/disabled class |
| valheim/index.html | EN语言按钮缺少active/disabled class |
| valheim/iron-sledge.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| valheim/iron-sledge.html | EN语言按钮缺少active/disabled class |
| valheim/padded-armor.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| valheim/padded-armor.html | EN语言按钮缺少active/disabled class |
| valheim/porcupine.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| valheim/porcupine.html | EN语言按钮缺少active/disabled class |
| valheim/stagbreaker.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| valheim/stagbreaker.html | EN语言按钮缺少active/disabled class |
| valheim/wolf-armor.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| valheim/wolf-armor.html | EN语言按钮缺少active/disabled class |
| valheim/draugr-fang.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| valheim/bronze-mace.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| valheim/blackmetal-sword.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| valheim/porcupine.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| valheim/iron-sledge.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| valheim/frostner.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| valheim/stagbreaker.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| valheim/wolf-armor.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| valheim/carapace-armor.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| valheim/padded-armor.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |

### Path Of Exile 2

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 26个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| path-of-exile-2/divine-orb.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| path-of-exile-2/divine-orb.html | EN语言按钮缺少active/disabled class |
| path-of-exile-2/divine-orb.html | 中文语言按钮缺少onclick跳转 |
| path-of-exile-2/index.html | EN语言按钮缺少active/disabled class |
| path-of-exile-2/regal-orb.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| path-of-exile-2/regal-orb.html | EN语言按钮缺少active/disabled class |
| path-of-exile-2/regal-orb.html | 中文语言按钮缺少onclick跳转 |
| path-of-exile-2/six-link-armor.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| path-of-exile-2/six-link-armor.html | EN语言按钮缺少active/disabled class |
| path-of-exile-2/six-link-armor.html | 中文语言按钮缺少onclick跳转 |
| path-of-exile-2/skill-gem.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| path-of-exile-2/skill-gem.html | EN语言按钮缺少active/disabled class |
| path-of-exile-2/skill-gem.html | 中文语言按钮缺少onclick跳转 |
| path-of-exile-2/uncorrupted-vessel.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| path-of-exile-2/uncorrupted-vessel.html | EN语言按钮缺少active/disabled class |
| path-of-exile-2/uncorrupted-vessel.html | 中文语言按钮缺少onclick跳转 |
| path-of-exile-2/headhunter.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| path-of-exile-2/uncorrupted-vessel.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| path-of-exile-2/regal-orb.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| path-of-exile-2/exalted-crafting.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| path-of-exile-2/six-link-armor.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| path-of-exile-2/mageblood.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| path-of-exile-2/mirror-kalandra.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| path-of-exile-2/skill-gem.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| path-of-exile-2/divine-orb.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| path-of-exile-2/tabula-rasa.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |

### Elden Ring

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 41个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| elden-ring/bewitching-branch.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| elden-ring/bloodboil-aromatic.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| elden-ring/drawstring-blood-grease.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| elden-ring/exalted-flesh.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| elden-ring/gold-pickled-fowl-foot.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| elden-ring/index.html | EN语言按钮缺少active/disabled class |
| elden-ring/ironjar-aromatic.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| elden-ring/preserving-boluses.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| elden-ring/spark-aromatic.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| elden-ring/uplifting-aromatic.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| elden-ring/warming-stone.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| elden-ring/zh/bewitching-branch.html | ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../') |
| elden-ring/zh/bloodboil-aromatic.html | ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../') |
| elden-ring/zh/drawstring-blood-grease.html | ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../') |
| elden-ring/zh/exalted-flesh.html | ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../') |
| elden-ring/zh/gold-pickled-fowl-foot.html | ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../') |
| elden-ring/zh/ironjar-aromatic.html | ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../') |
| elden-ring/zh/preserving-boluses.html | ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../') |
| elden-ring/zh/spark-aromatic.html | ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../') |
| elden-ring/zh/uplifting-aromatic.html | ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../') |
| elden-ring/zh/warming-stone.html | ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../') |
| elden-ring/uplifting-aromatic.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| elden-ring/uplifting-aromatic.html / elden-ring/zh/uplifting-aromatic.html | 语言切换按钮不对等: EN=False, ZH=True |
| elden-ring/warming-stone.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| elden-ring/warming-stone.html / elden-ring/zh/warming-stone.html | 语言切换按钮不对等: EN=False, ZH=True |
| elden-ring/bloodboil-aromatic.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| elden-ring/bloodboil-aromatic.html / elden-ring/zh/bloodboil-aromatic.html | 语言切换按钮不对等: EN=False, ZH=True |
| elden-ring/drawstring-blood-grease.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| elden-ring/drawstring-blood-grease.html / elden-ring/zh/drawstring-blood-grease.html | 语言切换按钮不对等: EN=False, ZH=True |
| elden-ring/bewitching-branch.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| elden-ring/bewitching-branch.html / elden-ring/zh/bewitching-branch.html | 语言切换按钮不对等: EN=False, ZH=True |
| elden-ring/gold-pickled-fowl-foot.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| elden-ring/gold-pickled-fowl-foot.html / elden-ring/zh/gold-pickled-fowl-foot.html | 语言切换按钮不对等: EN=False, ZH=True |
| elden-ring/ironjar-aromatic.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| elden-ring/ironjar-aromatic.html / elden-ring/zh/ironjar-aromatic.html | 语言切换按钮不对等: EN=False, ZH=True |
| elden-ring/preserving-boluses.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| elden-ring/preserving-boluses.html / elden-ring/zh/preserving-boluses.html | 语言切换按钮不对等: EN=False, ZH=True |
| elden-ring/spark-aromatic.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| elden-ring/spark-aromatic.html / elden-ring/zh/spark-aromatic.html | 语言切换按钮不对等: EN=False, ZH=True |
| elden-ring/exalted-flesh.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| elden-ring/exalted-flesh.html / elden-ring/zh/exalted-flesh.html | 语言切换按钮不对等: EN=False, ZH=True |

### Stardew Valley

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 31个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| stardew-valley/crystalarium.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| stardew-valley/crystalarium.html | EN语言按钮缺少active/disabled class |
| stardew-valley/index.html | EN语言按钮缺少active/disabled class |
| stardew-valley/iridium-band.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| stardew-valley/iridium-band.html | EN语言按钮缺少active/disabled class |
| stardew-valley/keg.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| stardew-valley/keg.html | EN语言按钮缺少active/disabled class |
| stardew-valley/lightning-rod.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| stardew-valley/lightning-rod.html | EN语言按钮缺少active/disabled class |
| stardew-valley/rain-totem.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| stardew-valley/rain-totem.html | EN语言按钮缺少active/disabled class |
| stardew-valley/seed-maker.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| stardew-valley/seed-maker.html | EN语言按钮缺少active/disabled class |
| stardew-valley/slime-incubator.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| stardew-valley/slime-incubator.html | EN语言按钮缺少active/disabled class |
| stardew-valley/stairs.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| stardew-valley/stairs.html | EN语言按钮缺少active/disabled class |
| stardew-valley/warp-farm.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| stardew-valley/warp-farm.html | EN语言按钮缺少active/disabled class |
| stardew-valley/wicked-statue.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| stardew-valley/wicked-statue.html | EN语言按钮缺少active/disabled class |
| stardew-valley/iridium-band.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| stardew-valley/crystalarium.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| stardew-valley/warp-farm.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| stardew-valley/keg.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| stardew-valley/seed-maker.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| stardew-valley/rain-totem.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| stardew-valley/wicked-statue.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| stardew-valley/slime-incubator.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| stardew-valley/lightning-rod.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| stardew-valley/stairs.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |

### Hades 2

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 21个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| hades-2/aspects-night-darkness.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| hades-2/consecration-ashes.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| hades-2/greater-favor-gaia.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| hades-2/index.html | EN语言按钮缺少active/disabled class |
| hades-2/insight-offerings.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| hades-2/permeation-wards.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| hades-2/rite-vapor-cleansing.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| hades-2/shadow-extraction.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| hades-2/shimmering-ambrosia.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| hades-2/surge-stygian-wells.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| hades-2/unraveling-fateful-bond.html | EN页面CSS路径可能不正确 (应为 '../css/style.css') |
| hades-2/unraveling-fateful-bond.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| hades-2/greater-favor-gaia.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| hades-2/aspects-night-darkness.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| hades-2/permeation-wards.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| hades-2/rite-vapor-cleansing.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| hades-2/shadow-extraction.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| hades-2/shimmering-ambrosia.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| hades-2/surge-stygian-wells.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| hades-2/consecration-ashes.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| hades-2/insight-offerings.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |

### Satisfactory

- **EN页面**: 11个
- **ZH页面**: 11个
- **发现问题**: 41个

**问题列表**:

| 文件 | 问题描述 |
|------|----------|
| satisfactory/cast-screws.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| satisfactory/cast-screws.html | EN语言按钮缺少active/disabled class |
| satisfactory/cast-screws.html | 中文语言按钮缺少onclick跳转 |
| satisfactory/copper-alloy-ingot.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| satisfactory/copper-alloy-ingot.html | EN语言按钮缺少active/disabled class |
| satisfactory/copper-alloy-ingot.html | 中文语言按钮缺少onclick跳转 |
| satisfactory/diluted-fuel.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| satisfactory/diluted-fuel.html | EN语言按钮缺少active/disabled class |
| satisfactory/diluted-fuel.html | 中文语言按钮缺少onclick跳转 |
| satisfactory/fused-wire.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| satisfactory/fused-wire.html | EN语言按钮缺少active/disabled class |
| satisfactory/fused-wire.html | 中文语言按钮缺少onclick跳转 |
| satisfactory/heavy-encased-frame.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| satisfactory/heavy-encased-frame.html | EN语言按钮缺少active/disabled class |
| satisfactory/heavy-encased-frame.html | 中文语言按钮缺少onclick跳转 |
| satisfactory/index.html | EN语言按钮缺少active/disabled class |
| satisfactory/pure-ingots.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| satisfactory/pure-ingots.html | EN语言按钮缺少active/disabled class |
| satisfactory/pure-ingots.html | 中文语言按钮缺少onclick跳转 |
| satisfactory/recycled-plastic.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| satisfactory/recycled-plastic.html | EN语言按钮缺少active/disabled class |
| satisfactory/recycled-plastic.html | 中文语言按钮缺少onclick跳转 |
| satisfactory/silicon-circuit-board.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| satisfactory/silicon-circuit-board.html | EN语言按钮缺少active/disabled class |
| satisfactory/silicon-circuit-board.html | 中文语言按钮缺少onclick跳转 |
| satisfactory/steel-screw.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| satisfactory/steel-screw.html | EN语言按钮缺少active/disabled class |
| satisfactory/steel-screw.html | 中文语言按钮缺少onclick跳转 |
| satisfactory/stitched-iron-plate.html | EN页面缺少body class='lang-en' (当前无class，但有lang-switch) |
| satisfactory/stitched-iron-plate.html | EN语言按钮缺少active/disabled class |
| satisfactory/stitched-iron-plate.html | 中文语言按钮缺少onclick跳转 |
| satisfactory/diluted-fuel.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| satisfactory/copper-alloy-ingot.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| satisfactory/cast-screws.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| satisfactory/fused-wire.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| satisfactory/silicon-circuit-board.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| satisfactory/heavy-encased-frame.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| satisfactory/stitched-iron-plate.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| satisfactory/steel-screw.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| satisfactory/pure-ingots.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |
| satisfactory/recycled-plastic.html | EN页面body class('(body without class)')应与ZH的'lang-zh'对等 |

---

## 三、建议修复方案

### 问题1: EN页面缺少body class='lang-en'

**影响范围**: 130个EN物品详情页面

**问题描述**: 对应的ZH页面有`<body class="lang-zh">`，但EN页面只有`<body>`，缺少`class="lang-en"`。

**修复方法**: 使用批量替换脚本为所有EN页面添加body class:
```bash
# 对每个游戏目录下的非index EN文件
for file in */*.html; do
  if [ "$file" != "*/index.html" ]; then
    sed -i 's/<body>$/<body class="lang-en">/' "$file"
  fi
done
```

---

### 问题2: EN语言按钮缺少active/disabled class

**影响范围**: 105个EN页面（包括index和items）

**问题描述**: EN页面的`<button data-lang="en">`缺少`class="active"`或`disabled`属性。

**修复方法**: 在lang-switch div中，为EN按钮添加class。例如将:
```html
<button data-lang="en" title="English">EN</button>
```
改为:
```html
<button data-lang="en" class="active" title="English">EN</button>
```

---

### 问题3: ZH页面导航链接路径错误

**影响范围**: 40个ZH页面（主要在monster-hunter-wilds）

**问题描述**: ZH页面在`game/zh/`子目录下，但导航链接使用`../`而非`../../`。
例如: `href="../blog/"` 应为 `href="../../blog/"`

**修复方法**: 批量修复ZH页面中的导航链接路径:
```bash
# 在game/zh/目录下的HTML文件
sed -i 's|href="../blog/"|href="../../blog/"|g' *.html
sed -i 's|href="../about.html"|href="../../about.html"|g' *.html
sed -i 's|href="../zh/"|href="../../zh/"|g' *.html
```

---

### 问题4: EN/ZH语言切换按钮不对等

**影响范围**: 16个页面对

**问题描述**: 部分EN页面没有lang-switch div，但对应的ZH页面有。或反之。

**修复方法**: 为缺少lang-switch的页面添加对应结构。EN页面应包含:
```html
<div class="lang-switch">
  <button data-lang="en" class="active" title="English">EN</button>
  <button data-lang="zh" onclick="window.location.href='./zh/FILENAME.html'" title="Chinese">中文</button>
</div>
```

---

### 问题5: EN页面CSS路径错误

**影响范围**: 26个EN页面

**问题描述**: 部分EN页面CSS路径不正确，导致样式未加载。

**修复方法**: 确保所有EN页面使用`../css/style.css`，ZH页面使用`../../css/style.css`。

---

## 四、完整问题列表

按游戏分组的所有问题详情：

### Terraria

- **terraria/ankh-charm.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **terraria/ankh-charm.html**: EN语言按钮缺少active/disabled class
- **terraria/ankh-shield.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **terraria/ankh-shield.html**: EN语言按钮缺少active/disabled class
- **terraria/avenger-emblem.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **terraria/avenger-emblem.html**: EN语言按钮缺少active/disabled class
- **terraria/cell-phone.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **terraria/cell-phone.html**: EN语言按钮缺少active/disabled class
- **terraria/frostspark-boots.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **terraria/frostspark-boots.html**: EN语言按钮缺少active/disabled class
- **terraria/index.html**: EN语言按钮缺少active/disabled class
- **terraria/nights-edge.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **terraria/nights-edge.html**: EN语言按钮缺少active/disabled class
- **terraria/pda.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **terraria/pda.html**: EN语言按钮缺少active/disabled class
- **terraria/terra-blade.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **terraria/terra-blade.html**: EN语言按钮缺少active/disabled class
- **terraria/terraspark-boots.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **terraria/terraspark-boots.html**: EN语言按钮缺少active/disabled class
- **terraria/zenith.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **terraria/zenith.html**: EN语言按钮缺少active/disabled class
- **terraria/ankh-charm.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **terraria/terraspark-boots.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **terraria/pda.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **terraria/zenith.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **terraria/ankh-shield.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **terraria/nights-edge.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **terraria/avenger-emblem.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **terraria/cell-phone.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **terraria/terra-blade.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **terraria/frostspark-boots.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
### Subnautica2

- **subnautica2/depth-module-mk1.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **subnautica2/depth-module-mk1.html**: EN语言按钮缺少active/disabled class
- **subnautica2/engine-efficiency.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **subnautica2/engine-efficiency.html**: EN语言按钮缺少active/disabled class
- **subnautica2/habitat-builder.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **subnautica2/habitat-builder.html**: EN语言按钮缺少active/disabled class
- **subnautica2/high-capacity-air-tank.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **subnautica2/high-capacity-air-tank.html**: EN语言按钮缺少active/disabled class
- **subnautica2/index.html**: EN语言按钮缺少active/disabled class
- **subnautica2/photovoltaic-charger.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **subnautica2/photovoltaic-charger.html**: EN语言按钮缺少active/disabled class
- **subnautica2/rebreather.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **subnautica2/rebreather.html**: EN语言按钮缺少active/disabled class
- **subnautica2/scout-chassis.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **subnautica2/scout-chassis.html**: EN语言按钮缺少active/disabled class
- **subnautica2/sonic-resonator.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **subnautica2/sonic-resonator.html**: EN语言按钮缺少active/disabled class
- **subnautica2/tadpole.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **subnautica2/tadpole.html**: EN语言按钮缺少active/disabled class
- **subnautica2/thermal-reactor.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **subnautica2/thermal-reactor.html**: EN语言按钮缺少active/disabled class
- **subnautica2/habitat-builder.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **subnautica2/scout-chassis.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **subnautica2/photovoltaic-charger.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **subnautica2/thermal-reactor.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **subnautica2/rebreather.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **subnautica2/sonic-resonator.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **subnautica2/engine-efficiency.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **subnautica2/depth-module-mk1.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **subnautica2/tadpole.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **subnautica2/high-capacity-air-tank.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
### Monster Hunter Wilds

- **monster-hunter-wilds/attack-decorations.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **monster-hunter-wilds/attack-decorations.html**: EN语言按钮缺少active/disabled class
- **monster-hunter-wilds/charm-mighty.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **monster-hunter-wilds/charm-mighty.html**: EN语言按钮缺少active/disabled class
- **monster-hunter-wilds/deviljho-greatsword.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **monster-hunter-wilds/deviljho-greatsword.html**: EN语言按钮缺少active/disabled class
- **monster-hunter-wilds/index.html**: EN语言按钮缺少active/disabled class
- **monster-hunter-wilds/kirin-armor.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **monster-hunter-wilds/kirin-armor.html**: EN语言按钮缺少active/disabled class
- **monster-hunter-wilds/legiana-bow.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **monster-hunter-wilds/legiana-bow.html**: EN语言按钮缺少active/disabled class
- **monster-hunter-wilds/nergigante-hammer.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **monster-hunter-wilds/nergigante-hammer.html**: EN语言按钮缺少active/disabled class
- **monster-hunter-wilds/rathalos-armor.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **monster-hunter-wilds/rathalos-armor.html**: EN语言按钮缺少active/disabled class
- **monster-hunter-wilds/teostra-longsword.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **monster-hunter-wilds/teostra-longsword.html**: EN语言按钮缺少active/disabled class
- **monster-hunter-wilds/vaal-hazak-set.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **monster-hunter-wilds/vaal-hazak-set.html**: EN语言按钮缺少active/disabled class
- **monster-hunter-wilds/xeno-jiiqa-lance.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **monster-hunter-wilds/xeno-jiiqa-lance.html**: EN语言按钮缺少active/disabled class
- **monster-hunter-wilds/zh/attack-decorations.html**: lang-switch中缺少data-lang='zh'按钮
- **monster-hunter-wilds/zh/attack-decorations.html**: lang-switch中缺少data-lang='en'按钮
- **monster-hunter-wilds/zh/attack-decorations.html**: ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/attack-decorations.html**: ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/attack-decorations.html**: ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/charm-mighty.html**: lang-switch中缺少data-lang='zh'按钮
- **monster-hunter-wilds/zh/charm-mighty.html**: lang-switch中缺少data-lang='en'按钮
- **monster-hunter-wilds/zh/charm-mighty.html**: ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/charm-mighty.html**: ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/charm-mighty.html**: ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/deviljho-greatsword.html**: lang-switch中缺少data-lang='zh'按钮
- **monster-hunter-wilds/zh/deviljho-greatsword.html**: lang-switch中缺少data-lang='en'按钮
- **monster-hunter-wilds/zh/deviljho-greatsword.html**: ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/deviljho-greatsword.html**: ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/deviljho-greatsword.html**: ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/kirin-armor.html**: lang-switch中缺少data-lang='zh'按钮
- **monster-hunter-wilds/zh/kirin-armor.html**: lang-switch中缺少data-lang='en'按钮
- **monster-hunter-wilds/zh/kirin-armor.html**: ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/kirin-armor.html**: ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/kirin-armor.html**: ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/legiana-bow.html**: lang-switch中缺少data-lang='zh'按钮
- **monster-hunter-wilds/zh/legiana-bow.html**: lang-switch中缺少data-lang='en'按钮
- **monster-hunter-wilds/zh/legiana-bow.html**: ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/legiana-bow.html**: ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/legiana-bow.html**: ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/nergigante-hammer.html**: lang-switch中缺少data-lang='zh'按钮
- **monster-hunter-wilds/zh/nergigante-hammer.html**: lang-switch中缺少data-lang='en'按钮
- **monster-hunter-wilds/zh/nergigante-hammer.html**: ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/nergigante-hammer.html**: ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/nergigante-hammer.html**: ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/rathalos-armor.html**: lang-switch中缺少data-lang='zh'按钮
- **monster-hunter-wilds/zh/rathalos-armor.html**: lang-switch中缺少data-lang='en'按钮
- **monster-hunter-wilds/zh/rathalos-armor.html**: ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/rathalos-armor.html**: ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/rathalos-armor.html**: ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/teostra-longsword.html**: lang-switch中缺少data-lang='zh'按钮
- **monster-hunter-wilds/zh/teostra-longsword.html**: lang-switch中缺少data-lang='en'按钮
- **monster-hunter-wilds/zh/teostra-longsword.html**: ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/teostra-longsword.html**: ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/teostra-longsword.html**: ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/vaal-hazak-set.html**: lang-switch中缺少data-lang='zh'按钮
- **monster-hunter-wilds/zh/vaal-hazak-set.html**: lang-switch中缺少data-lang='en'按钮
- **monster-hunter-wilds/zh/vaal-hazak-set.html**: ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/vaal-hazak-set.html**: ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/vaal-hazak-set.html**: ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/xeno-jiiqa-lance.html**: lang-switch中缺少data-lang='zh'按钮
- **monster-hunter-wilds/zh/xeno-jiiqa-lance.html**: lang-switch中缺少data-lang='en'按钮
- **monster-hunter-wilds/zh/xeno-jiiqa-lance.html**: ZH页面导航链接路径可能过浅: href='../blog/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/xeno-jiiqa-lance.html**: ZH页面导航链接路径可能过浅: href='../zh/' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/zh/xeno-jiiqa-lance.html**: ZH页面导航链接路径可能过浅: href='../about.html' (在zh/子目录中应使用'../../')
- **monster-hunter-wilds/nergigante-hammer.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **monster-hunter-wilds/xeno-jiiqa-lance.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **monster-hunter-wilds/kirin-armor.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **monster-hunter-wilds/deviljho-greatsword.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **monster-hunter-wilds/vaal-hazak-set.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **monster-hunter-wilds/legiana-bow.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **monster-hunter-wilds/teostra-longsword.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **monster-hunter-wilds/rathalos-armor.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **monster-hunter-wilds/charm-mighty.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **monster-hunter-wilds/attack-decorations.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
### Zelda Totk

- **zelda-totk/barbarian-set.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **zelda-totk/barbarian-set.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **zelda-totk/champions-leathers.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **zelda-totk/fierce-deity-set.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **zelda-totk/fierce-deity-set.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **zelda-totk/hylian-shield.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **zelda-totk/hylian-shield.html**: EN语言按钮缺少active/disabled class
- **zelda-totk/index.html**: EN语言按钮缺少active/disabled class
- **zelda-totk/lightscale-trident.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **zelda-totk/lightscale-trident.html**: EN语言按钮缺少active/disabled class
- **zelda-totk/master-sword.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **zelda-totk/master-sword.html**: EN语言按钮缺少active/disabled class
- **zelda-totk/radiant-set.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **zelda-totk/scimitar-seven.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **zelda-totk/scimitar-seven.html**: EN语言按钮缺少active/disabled class
- **zelda-totk/scimitar-seven.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **zelda-totk/champions-leathers.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **zelda-totk/champions-leathers.html / zelda-totk/zh/champions-leathers.html**: 语言切换按钮不对等: EN=False, ZH=True
- **zelda-totk/radiant-set.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **zelda-totk/radiant-set.html / zelda-totk/zh/radiant-set.html**: 语言切换按钮不对等: EN=False, ZH=True
- **zelda-totk/hylian-shield.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **zelda-totk/great-eagle-bow.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **zelda-totk/great-eagle-bow.html / zelda-totk/zh/great-eagle-bow.html**: 语言切换按钮不对等: EN=False, ZH=True
- **zelda-totk/great-eagle-bow.html / zelda-totk/zh/great-eagle-bow.html**: top-nav不对等: EN=False, ZH=True
- **zelda-totk/barbarian-set.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **zelda-totk/boulder-breaker.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **zelda-totk/boulder-breaker.html / zelda-totk/zh/boulder-breaker.html**: 语言切换按钮不对等: EN=False, ZH=True
- **zelda-totk/boulder-breaker.html / zelda-totk/zh/boulder-breaker.html**: top-nav不对等: EN=False, ZH=True
- **zelda-totk/fierce-deity-set.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **zelda-totk/lightscale-trident.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **zelda-totk/master-sword.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
### Minecraft

- **minecraft/anvil.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **minecraft/anvil.html**: EN语言按钮缺少active/disabled class
- **minecraft/anvil.html**: 中文语言按钮缺少onclick跳转
- **minecraft/beacon.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **minecraft/beacon.html**: EN语言按钮缺少active/disabled class
- **minecraft/conduit.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **minecraft/enchanting-table.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **minecraft/ender-chest.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **minecraft/ender-chest.html**: EN语言按钮缺少active/disabled class
- **minecraft/eye-of-ender.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **minecraft/eye-of-ender.html**: EN语言按钮缺少active/disabled class
- **minecraft/eye-of-ender.html**: 中文语言按钮缺少onclick跳转
- **minecraft/firework-rocket.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **minecraft/firework-rocket.html**: EN语言按钮缺少active/disabled class
- **minecraft/firework-rocket.html**: 中文语言按钮缺少onclick跳转
- **minecraft/index.html**: EN语言按钮缺少active/disabled class
- **minecraft/netherite-armor.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **minecraft/netherite-armor.html**: EN语言按钮缺少active/disabled class
- **minecraft/powered-rail.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **minecraft/powered-rail.html**: EN语言按钮缺少active/disabled class
- **minecraft/powered-rail.html**: 中文语言按钮缺少onclick跳转
- **minecraft/slow-falling-potion.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **minecraft/slow-falling-potion.html**: EN语言按钮缺少active/disabled class
- **minecraft/slow-falling-potion.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **minecraft/enchanting-table.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **minecraft/enchanting-table.html / minecraft/zh/enchanting-table.html**: 语言切换按钮不对等: EN=False, ZH=True
- **minecraft/eye-of-ender.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **minecraft/anvil.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **minecraft/beacon.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **minecraft/netherite-armor.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **minecraft/ender-chest.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **minecraft/firework-rocket.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **minecraft/powered-rail.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **minecraft/conduit.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **minecraft/conduit.html / minecraft/zh/conduit.html**: 语言切换按钮不对等: EN=False, ZH=True
### No Mans Sky

- **no-mans-sky/ai-valves.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **no-mans-sky/ai-valves.html**: EN语言按钮缺少active/disabled class
- **no-mans-sky/fusion-ignitor.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **no-mans-sky/fusion-ignitor.html**: EN语言按钮缺少active/disabled class
- **no-mans-sky/index.html**: EN语言按钮缺少active/disabled class
- **no-mans-sky/indium-drive.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **no-mans-sky/indium-drive.html**: EN语言按钮缺少active/disabled class
- **no-mans-sky/minotaur-geobay.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **no-mans-sky/minotaur-geobay.html**: EN语言按钮缺少active/disabled class
- **no-mans-sky/multi-tool-s-class.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **no-mans-sky/multi-tool-s-class.html**: EN语言按钮缺少active/disabled class
- **no-mans-sky/sentinel-exosuit.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **no-mans-sky/sentinel-exosuit.html**: EN语言按钮缺少active/disabled class
- **no-mans-sky/stasis-device.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **no-mans-sky/stasis-device.html**: EN语言按钮缺少active/disabled class
- **no-mans-sky/underwater-module.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **no-mans-sky/underwater-module.html**: EN语言按钮缺少active/disabled class
- **no-mans-sky/void-egg.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **no-mans-sky/void-egg.html**: EN语言按钮缺少active/disabled class
- **no-mans-sky/warp-hypercore.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **no-mans-sky/warp-hypercore.html**: EN语言按钮缺少active/disabled class
- **no-mans-sky/multi-tool-s-class.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **no-mans-sky/stasis-device.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **no-mans-sky/void-egg.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **no-mans-sky/ai-valves.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **no-mans-sky/minotaur-geobay.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **no-mans-sky/fusion-ignitor.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **no-mans-sky/sentinel-exosuit.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **no-mans-sky/warp-hypercore.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **no-mans-sky/indium-drive.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **no-mans-sky/underwater-module.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
### Baldurs Gate 3

- **baldurs-gate-3/devilfoil-mask.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **baldurs-gate-3/devilfoil-mask.html**: EN语言按钮缺少active/disabled class
- **baldurs-gate-3/helldusk-armor.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **baldurs-gate-3/helldusk-armor.html**: EN语言按钮缺少active/disabled class
- **baldurs-gate-3/index.html**: EN语言按钮缺少active/disabled class
- **baldurs-gate-3/moonlantern.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **baldurs-gate-3/moonlantern.html**: EN语言按钮缺少active/disabled class
- **baldurs-gate-3/shadowheart-spear.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **baldurs-gate-3/shadowheart-spear.html**: EN语言按钮缺少active/disabled class
- **baldurs-gate-3/silver-sword.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **baldurs-gate-3/silver-sword.html**: EN语言按钮缺少active/disabled class
- **baldurs-gate-3/gontr-mael.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **baldurs-gate-3/blood-of-lathander.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **baldurs-gate-3/devilfoil-mask.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **baldurs-gate-3/nyrulna.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **baldurs-gate-3/shars-spear.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **baldurs-gate-3/helldusk-armor.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **baldurs-gate-3/shadowheart-spear.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **baldurs-gate-3/duellist-gloves.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **baldurs-gate-3/moonlantern.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **baldurs-gate-3/silver-sword.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
### Valheim

- **valheim/blackmetal-sword.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **valheim/blackmetal-sword.html**: EN语言按钮缺少active/disabled class
- **valheim/bronze-mace.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **valheim/bronze-mace.html**: EN语言按钮缺少active/disabled class
- **valheim/carapace-armor.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **valheim/carapace-armor.html**: EN语言按钮缺少active/disabled class
- **valheim/draugr-fang.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **valheim/draugr-fang.html**: EN语言按钮缺少active/disabled class
- **valheim/frostner.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **valheim/frostner.html**: EN语言按钮缺少active/disabled class
- **valheim/index.html**: EN语言按钮缺少active/disabled class
- **valheim/iron-sledge.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **valheim/iron-sledge.html**: EN语言按钮缺少active/disabled class
- **valheim/padded-armor.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **valheim/padded-armor.html**: EN语言按钮缺少active/disabled class
- **valheim/porcupine.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **valheim/porcupine.html**: EN语言按钮缺少active/disabled class
- **valheim/stagbreaker.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **valheim/stagbreaker.html**: EN语言按钮缺少active/disabled class
- **valheim/wolf-armor.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **valheim/wolf-armor.html**: EN语言按钮缺少active/disabled class
- **valheim/draugr-fang.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **valheim/bronze-mace.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **valheim/blackmetal-sword.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **valheim/porcupine.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **valheim/iron-sledge.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **valheim/frostner.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **valheim/stagbreaker.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **valheim/wolf-armor.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **valheim/carapace-armor.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **valheim/padded-armor.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
### Path Of Exile 2

- **path-of-exile-2/divine-orb.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **path-of-exile-2/divine-orb.html**: EN语言按钮缺少active/disabled class
- **path-of-exile-2/divine-orb.html**: 中文语言按钮缺少onclick跳转
- **path-of-exile-2/index.html**: EN语言按钮缺少active/disabled class
- **path-of-exile-2/regal-orb.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **path-of-exile-2/regal-orb.html**: EN语言按钮缺少active/disabled class
- **path-of-exile-2/regal-orb.html**: 中文语言按钮缺少onclick跳转
- **path-of-exile-2/six-link-armor.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **path-of-exile-2/six-link-armor.html**: EN语言按钮缺少active/disabled class
- **path-of-exile-2/six-link-armor.html**: 中文语言按钮缺少onclick跳转
- **path-of-exile-2/skill-gem.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **path-of-exile-2/skill-gem.html**: EN语言按钮缺少active/disabled class
- **path-of-exile-2/skill-gem.html**: 中文语言按钮缺少onclick跳转
- **path-of-exile-2/uncorrupted-vessel.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **path-of-exile-2/uncorrupted-vessel.html**: EN语言按钮缺少active/disabled class
- **path-of-exile-2/uncorrupted-vessel.html**: 中文语言按钮缺少onclick跳转
- **path-of-exile-2/headhunter.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **path-of-exile-2/uncorrupted-vessel.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **path-of-exile-2/regal-orb.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **path-of-exile-2/exalted-crafting.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **path-of-exile-2/six-link-armor.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **path-of-exile-2/mageblood.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **path-of-exile-2/mirror-kalandra.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **path-of-exile-2/skill-gem.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **path-of-exile-2/divine-orb.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **path-of-exile-2/tabula-rasa.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
### Elden Ring

- **elden-ring/bewitching-branch.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **elden-ring/bloodboil-aromatic.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **elden-ring/drawstring-blood-grease.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **elden-ring/exalted-flesh.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **elden-ring/gold-pickled-fowl-foot.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **elden-ring/index.html**: EN语言按钮缺少active/disabled class
- **elden-ring/ironjar-aromatic.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **elden-ring/preserving-boluses.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **elden-ring/spark-aromatic.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **elden-ring/uplifting-aromatic.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **elden-ring/warming-stone.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **elden-ring/zh/bewitching-branch.html**: ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../')
- **elden-ring/zh/bloodboil-aromatic.html**: ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../')
- **elden-ring/zh/drawstring-blood-grease.html**: ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../')
- **elden-ring/zh/exalted-flesh.html**: ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../')
- **elden-ring/zh/gold-pickled-fowl-foot.html**: ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../')
- **elden-ring/zh/ironjar-aromatic.html**: ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../')
- **elden-ring/zh/preserving-boluses.html**: ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../')
- **elden-ring/zh/spark-aromatic.html**: ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../')
- **elden-ring/zh/uplifting-aromatic.html**: ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../')
- **elden-ring/zh/warming-stone.html**: ZH页面导航链接路径可能过浅: href='../index.html' (在zh/子目录中应使用'../../')
- **elden-ring/uplifting-aromatic.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **elden-ring/uplifting-aromatic.html / elden-ring/zh/uplifting-aromatic.html**: 语言切换按钮不对等: EN=False, ZH=True
- **elden-ring/warming-stone.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **elden-ring/warming-stone.html / elden-ring/zh/warming-stone.html**: 语言切换按钮不对等: EN=False, ZH=True
- **elden-ring/bloodboil-aromatic.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **elden-ring/bloodboil-aromatic.html / elden-ring/zh/bloodboil-aromatic.html**: 语言切换按钮不对等: EN=False, ZH=True
- **elden-ring/drawstring-blood-grease.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **elden-ring/drawstring-blood-grease.html / elden-ring/zh/drawstring-blood-grease.html**: 语言切换按钮不对等: EN=False, ZH=True
- **elden-ring/bewitching-branch.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **elden-ring/bewitching-branch.html / elden-ring/zh/bewitching-branch.html**: 语言切换按钮不对等: EN=False, ZH=True
- **elden-ring/gold-pickled-fowl-foot.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **elden-ring/gold-pickled-fowl-foot.html / elden-ring/zh/gold-pickled-fowl-foot.html**: 语言切换按钮不对等: EN=False, ZH=True
- **elden-ring/ironjar-aromatic.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **elden-ring/ironjar-aromatic.html / elden-ring/zh/ironjar-aromatic.html**: 语言切换按钮不对等: EN=False, ZH=True
- **elden-ring/preserving-boluses.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **elden-ring/preserving-boluses.html / elden-ring/zh/preserving-boluses.html**: 语言切换按钮不对等: EN=False, ZH=True
- **elden-ring/spark-aromatic.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **elden-ring/spark-aromatic.html / elden-ring/zh/spark-aromatic.html**: 语言切换按钮不对等: EN=False, ZH=True
- **elden-ring/exalted-flesh.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **elden-ring/exalted-flesh.html / elden-ring/zh/exalted-flesh.html**: 语言切换按钮不对等: EN=False, ZH=True
### Stardew Valley

- **stardew-valley/crystalarium.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **stardew-valley/crystalarium.html**: EN语言按钮缺少active/disabled class
- **stardew-valley/index.html**: EN语言按钮缺少active/disabled class
- **stardew-valley/iridium-band.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **stardew-valley/iridium-band.html**: EN语言按钮缺少active/disabled class
- **stardew-valley/keg.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **stardew-valley/keg.html**: EN语言按钮缺少active/disabled class
- **stardew-valley/lightning-rod.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **stardew-valley/lightning-rod.html**: EN语言按钮缺少active/disabled class
- **stardew-valley/rain-totem.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **stardew-valley/rain-totem.html**: EN语言按钮缺少active/disabled class
- **stardew-valley/seed-maker.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **stardew-valley/seed-maker.html**: EN语言按钮缺少active/disabled class
- **stardew-valley/slime-incubator.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **stardew-valley/slime-incubator.html**: EN语言按钮缺少active/disabled class
- **stardew-valley/stairs.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **stardew-valley/stairs.html**: EN语言按钮缺少active/disabled class
- **stardew-valley/warp-farm.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **stardew-valley/warp-farm.html**: EN语言按钮缺少active/disabled class
- **stardew-valley/wicked-statue.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **stardew-valley/wicked-statue.html**: EN语言按钮缺少active/disabled class
- **stardew-valley/iridium-band.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **stardew-valley/crystalarium.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **stardew-valley/warp-farm.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **stardew-valley/keg.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **stardew-valley/seed-maker.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **stardew-valley/rain-totem.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **stardew-valley/wicked-statue.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **stardew-valley/slime-incubator.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **stardew-valley/lightning-rod.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **stardew-valley/stairs.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
### Hades 2

- **hades-2/aspects-night-darkness.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **hades-2/consecration-ashes.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **hades-2/greater-favor-gaia.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **hades-2/index.html**: EN语言按钮缺少active/disabled class
- **hades-2/insight-offerings.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **hades-2/permeation-wards.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **hades-2/rite-vapor-cleansing.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **hades-2/shadow-extraction.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **hades-2/shimmering-ambrosia.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **hades-2/surge-stygian-wells.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **hades-2/unraveling-fateful-bond.html**: EN页面CSS路径可能不正确 (应为 '../css/style.css')
- **hades-2/unraveling-fateful-bond.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **hades-2/greater-favor-gaia.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **hades-2/aspects-night-darkness.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **hades-2/permeation-wards.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **hades-2/rite-vapor-cleansing.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **hades-2/shadow-extraction.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **hades-2/shimmering-ambrosia.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **hades-2/surge-stygian-wells.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **hades-2/consecration-ashes.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **hades-2/insight-offerings.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
### Satisfactory

- **satisfactory/cast-screws.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **satisfactory/cast-screws.html**: EN语言按钮缺少active/disabled class
- **satisfactory/cast-screws.html**: 中文语言按钮缺少onclick跳转
- **satisfactory/copper-alloy-ingot.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **satisfactory/copper-alloy-ingot.html**: EN语言按钮缺少active/disabled class
- **satisfactory/copper-alloy-ingot.html**: 中文语言按钮缺少onclick跳转
- **satisfactory/diluted-fuel.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **satisfactory/diluted-fuel.html**: EN语言按钮缺少active/disabled class
- **satisfactory/diluted-fuel.html**: 中文语言按钮缺少onclick跳转
- **satisfactory/fused-wire.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **satisfactory/fused-wire.html**: EN语言按钮缺少active/disabled class
- **satisfactory/fused-wire.html**: 中文语言按钮缺少onclick跳转
- **satisfactory/heavy-encased-frame.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **satisfactory/heavy-encased-frame.html**: EN语言按钮缺少active/disabled class
- **satisfactory/heavy-encased-frame.html**: 中文语言按钮缺少onclick跳转
- **satisfactory/index.html**: EN语言按钮缺少active/disabled class
- **satisfactory/pure-ingots.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **satisfactory/pure-ingots.html**: EN语言按钮缺少active/disabled class
- **satisfactory/pure-ingots.html**: 中文语言按钮缺少onclick跳转
- **satisfactory/recycled-plastic.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **satisfactory/recycled-plastic.html**: EN语言按钮缺少active/disabled class
- **satisfactory/recycled-plastic.html**: 中文语言按钮缺少onclick跳转
- **satisfactory/silicon-circuit-board.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **satisfactory/silicon-circuit-board.html**: EN语言按钮缺少active/disabled class
- **satisfactory/silicon-circuit-board.html**: 中文语言按钮缺少onclick跳转
- **satisfactory/steel-screw.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **satisfactory/steel-screw.html**: EN语言按钮缺少active/disabled class
- **satisfactory/steel-screw.html**: 中文语言按钮缺少onclick跳转
- **satisfactory/stitched-iron-plate.html**: EN页面缺少body class='lang-en' (当前无class，但有lang-switch)
- **satisfactory/stitched-iron-plate.html**: EN语言按钮缺少active/disabled class
- **satisfactory/stitched-iron-plate.html**: 中文语言按钮缺少onclick跳转
- **satisfactory/diluted-fuel.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **satisfactory/copper-alloy-ingot.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **satisfactory/cast-screws.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **satisfactory/fused-wire.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **satisfactory/silicon-circuit-board.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **satisfactory/heavy-encased-frame.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **satisfactory/stitched-iron-plate.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **satisfactory/steel-screw.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **satisfactory/pure-ingots.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等
- **satisfactory/recycled-plastic.html**: EN页面body class('(body without class)')应与ZH的'lang-zh'对等

---

## 五、自动化修复脚本（Python）

```python
#!/usr/bin/env python3
""
RelicTrek Link Audit Auto-Fix Script
运行前请备份所有HTML文件!
""
import re
from pathlib import Path

GAMES = [
    'terraria', 'subnautica2', 'monster-hunter-wilds', 'zelda-totk',
    'minecraft', 'no-mans-sky', 'baldurs-gate-3', 'valheim',
    'path-of-exile-2', 'elden-ring', 'stardew-valley', 'hades-2', 'satisfactory'
]
BASE = Path('/mnt/agents/output/relictrek')

def fix_en_body_class(content, filepath):
    """为EN页面添加lang-en body class"""
    if '<body>' in content and 'class="lang-en"' not in content:
        return content.replace('<body>', '<body class="lang-en">', 1)
    return content

def fix_en_lang_button(content, filepath):
    """为EN按钮添加active class"""
    pattern = r'<button([^>]*)data-lang="en"([^>]*)>'
    def replacer(m):
        attrs_before = m.group(1)
        attrs_after = m.group(2)
        if 'active' not in attrs_before and 'active' not in attrs_after:
            return f'<button{attrs_before}class="active"{attrs_after}>'
        return m.group(0)
    return re.sub(pattern, replacer, content)

def fix_zh_nav_paths(content, filepath):
    """修复ZH页面导航路径"""
    if '/zh/' in str(filepath):
        content = content.replace('href="../blog/"', 'href="../../blog/"')
        content = content.replace('href="../about.html"', 'href="../../about.html"')
        content = content.replace('href="../zh/"', 'href="../../zh/"')
    return content

# 主修复逻辑
for game in GAMES:
    game_dir = BASE / game
    for html_file in list(game_dir.glob('*.html')) + list((game_dir / 'zh').glob('*.html')):
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        content = fix_en_body_class(content, html_file)
        content = fix_en_lang_button(content, html_file)
        content = fix_zh_nav_paths(content, html_file)
        if content != original:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Fixed: {html_file}')
```

---

## 六、附录：检查规则说明

### EN页面检查项
1. `<body class="lang-en">` 必须存在
2. EN按钮必须有 `class="active"` 或 `disabled`
3. 中文按钮必须有 `onclick="window.location.href='zh/...'"`
4. 导航Games链接在index页必须有 `class="active"`
5. CSS路径 `href="../css/style.css"` 必须正确
6. JS路径 `src="../js/main.js"` 必须正确

### ZH页面检查项
1. `<body class="lang-zh">` 必须存在
2. 中文按钮必须有 `class="active"`
3. EN按钮必须有 `onclick="window.location.href='../...'"`
4. 导航链接路径必须使用 `../../`（考虑zh/子目录深度）
5. CSS路径 `href="../../css/style.css"` 必须正确
6. JS路径 `src="../../js/main.js"` 必须正确
7. 正文必须包含超过50个中文字符

### EN-ZH对等性检查
1. 两个语言版本的body class必须对等（lang-en ↔ lang-zh）
2. 两个语言版本必须有相同的结构特征（lang-switch, top-nav）
3. 文件必须一一对应（相同文件名）
