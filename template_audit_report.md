# RelicTrek 物品页面模板格式检查报告

## 检查标准
- **标准模板**特征: `<nav class="top-nav">`, `<div class="ticker-bar">`, `<div class="main-layout">`, `<div class="lang-switch">`
- **老格式**特征: `<nav class="nav">`, `<div class="nav-logo">`, `<div class="news-ticker">`, `<div class="container">`
- **语言链接**: EN页面需有 `data-lang="zh"` 指向 `zh/{item}.html`; ZH页面需有 `data-lang="en"` 指向 `../{item}.html`

---

## 汇总统计

| 游戏 | 总页面 | OK | old_format | partial_format | link_error |
|------|--------|-----|------------|----------------|------------|
| Subnautica 2 | 20 | 20 | 0 | 0 | 0 |
| Monster Hunter Wilds | 20 | 0 | 4 | 16 | 0 |
| Minecraft | 20 | 15 | 0 | 5 | 0 |
| Path of Exile 2 | 20 | 10 | 10 | 0 | 0 |
| Elden Ring | 20 | 0 | 20 | 0 | 0 |
| Terraria (参考) | 20 | 20 | 0 | 0 | 0 |
| **总计** | **120** | **65** | **34** | **21** | **0** |

---

## Subnautica 2
### EN页面 (10/10 OK)
- depth-module-mk1.html: [ok] Standard format, links correct
- engine-efficiency.html: [ok] Standard format, links correct
- habitat-builder.html: [ok] Standard format, links correct
- high-capacity-air-tank.html: [ok] Standard format, links correct
- photovoltaic-charger.html: [ok] Standard format, links correct
- rebreather.html: [ok] Standard format, links correct
- scout-chassis.html: [ok] Standard format, links correct
- sonic-resonator.html: [ok] Standard format, links correct
- tadpole.html: [ok] Standard format, links correct
- thermal-reactor.html: [ok] Standard format, links correct

### ZH页面 (10/10 OK)
- zh/depth-module-mk1.html: [ok] Standard format, links correct
- zh/engine-efficiency.html: [ok] Standard format, links correct
- zh/habitat-builder.html: [ok] Standard format, links correct
- zh/high-capacity-air-tank.html: [ok] Standard format, links correct
- zh/photovoltaic-charger.html: [ok] Standard format, links correct
- zh/rebreather.html: [ok] Standard format, links correct
- zh/scout-chassis.html: [ok] Standard format, links correct
- zh/sonic-resonator.html: [ok] Standard format, links correct
- zh/tadpole.html: [ok] Standard format, links correct
- zh/thermal-reactor.html: [ok] Standard format, links correct

---

## Monster Hunter Wilds
### EN页面 (0/10 OK, 2 old_format, 8 partial_format)
- attack-decorations.html: [partial_format] Partial standard: missing main-layout
- charm-mighty.html: [partial_format] Partial standard: missing main-layout
- deviljho-greatsword.html: [partial_format] Partial standard: missing main-layout
- kirin-armor.html: [old_format] Uses old format: old container
- legiana-bow.html: [partial_format] Partial standard: missing main-layout
- nergigante-hammer.html: [partial_format] Partial standard: missing main-layout
- rathalos-armor.html: [partial_format] Partial standard: missing main-layout
- teostra-longsword.html: [old_format] Uses old format: old container
- vaal-hazak-set.html: [partial_format] Partial standard: missing main-layout
- xeno-jiiqa-lance.html: [partial_format] Partial standard: missing main-layout

### ZH页面 (0/10 OK, 2 old_format, 8 partial_format)
- zh/attack-decorations.html: [partial_format] Partial standard: missing main-layout
- zh/charm-mighty.html: [partial_format] Partial standard: missing main-layout
- zh/deviljho-greatsword.html: [partial_format] Partial standard: missing main-layout
- zh/kirin-armor.html: [old_format] Uses old format: old container
- zh/legiana-bow.html: [partial_format] Partial standard: missing main-layout
- zh/nergigante-hammer.html: [partial_format] Partial standard: missing main-layout
- zh/rathalos-armor.html: [partial_format] Partial standard: missing main-layout
- zh/teostra-longsword.html: [old_format] Uses old format: old container
- zh/vaal-hazak-set.html: [partial_format] Partial standard: missing main-layout
- zh/xeno-jiiqa-lance.html: [partial_format] Partial standard: missing main-layout

---

## Minecraft
### EN页面 (5/10 OK, 5 partial_format)
- anvil.html: [ok] Standard format, links correct
- beacon.html: [partial_format] Partial standard: missing main-layout, missing lang-switch
- conduit.html: [partial_format] Partial standard: missing main-layout, missing lang-switch
- enchanting-table.html: [partial_format] Partial standard: missing main-layout, missing lang-switch
- ender-chest.html: [ok] Standard format, links correct
- eye-of-ender.html: [partial_format] Partial standard: missing main-layout, missing lang-switch
- firework-rocket.html: [partial_format] Partial standard: missing main-layout, missing lang-switch
- netherite-armor.html: [ok] Standard format, links correct
- powered-rail.html: [ok] Standard format, links correct
- slow-falling-potion.html: [ok] Standard format, links correct

### ZH页面 (10/10 OK)
- zh/anvil.html: [ok] Standard format, links correct
- zh/beacon.html: [ok] Standard format, links correct
- zh/conduit.html: [ok] Standard format, links correct
- zh/enchanting-table.html: [ok] Standard format, links correct
- zh/ender-chest.html: [ok] Standard format, links correct
- zh/eye-of-ender.html: [ok] Standard format, links correct
- zh/firework-rocket.html: [ok] Standard format, links correct
- zh/netherite-armor.html: [ok] Standard format, links correct
- zh/powered-rail.html: [ok] Standard format, links correct
- zh/slow-falling-potion.html: [ok] Standard format, links correct

---

## Path of Exile 2
### EN页面 (5/10 OK, 5 old_format)
- divine-orb.html: [ok] Standard format, links correct
- exalted-crafting.html: [old_format] Uses old format: old nav, old container
- headhunter.html: [old_format] Uses old format: old nav, old container
- mageblood.html: [old_format] Uses old format: old nav, old container
- mirror-kalandra.html: [old_format] Uses old format: old nav, old container
- regal-orb.html: [ok] Standard format, links correct
- six-link-armor.html: [ok] Standard format, links correct
- skill-gem.html: [ok] Standard format, links correct
- tabula-rasa.html: [old_format] Uses old format: old nav, old container
- uncorrupted-vessel.html: [ok] Standard format, links correct

### ZH页面 (5/10 OK, 5 old_format)
- zh/divine-orb.html: [ok] Standard format, links correct
- zh/exalted-crafting.html: [old_format] Uses old format: old nav, old container
- zh/headhunter.html: [old_format] Uses old format: old nav, old container
- zh/mageblood.html: [old_format] Uses old format: old nav, old container
- zh/mirror-kalandra.html: [old_format] Uses old format: old nav, old container
- zh/regal-orb.html: [ok] Standard format, links correct
- zh/six-link-armor.html: [ok] Standard format, links correct
- zh/skill-gem.html: [ok] Standard format, links correct
- zh/tabula-rasa.html: [old_format] Uses old format: old nav, old container
- zh/uncorrupted-vessel.html: [ok] Standard format, links correct

---

## Elden Ring
### EN页面 (0/10 OK, 10 old_format)
- bewitching-branch.html: [old_format] Uses old format: old nav-logo, old container
- bloodboil-aromatic.html: [old_format] Uses old format: old nav-logo, old container
- drawstring-blood-grease.html: [old_format] Uses old format: old nav-logo, old container
- exalted-flesh.html: [old_format] Uses old format: old nav-logo, old container
- gold-pickled-fowl-foot.html: [old_format] Uses old format: old nav-logo, old container
- ironjar-aromatic.html: [old_format] Uses old format: old nav-logo, old container
- preserving-boluses.html: [old_format] Uses old format: old nav-logo, old container
- spark-aromatic.html: [old_format] Uses old format: old nav-logo, old container
- uplifting-aromatic.html: [old_format] Uses old format: old nav-logo, old container
- warming-stone.html: [old_format] Uses old format: old nav-logo, old container

### ZH页面 (0/10 OK, 10 old_format)
- zh/bewitching-branch.html: [old_format] Uses old format: old nav-logo, old container
- zh/bloodboil-aromatic.html: [old_format] Uses old format: old nav-logo, old container
- zh/drawstring-blood-grease.html: [old_format] Uses old format: old nav-logo, old container
- zh/exalted-flesh.html: [old_format] Uses old format: old nav-logo, old container
- zh/gold-pickled-fowl-foot.html: [old_format] Uses old format: old nav-logo, old container
- zh/ironjar-aromatic.html: [old_format] Uses old format: old nav-logo, old container
- zh/preserving-boluses.html: [old_format] Uses old format: old nav-logo, old container
- zh/spark-aromatic.html: [old_format] Uses old format: old nav-logo, old container
- zh/uplifting-aromatic.html: [old_format] Uses old format: old nav-logo, old container
- zh/warming-stone.html: [old_format] Uses old format: old nav-logo, old container

---

## Terraria (参考标准)
### EN页面 (10/10 OK)
- ankh-charm.html: [ok] Standard format, links correct
- ankh-shield.html: [ok] Standard format, links correct
- avenger-emblem.html: [ok] Standard format, links correct
- cell-phone.html: [ok] Standard format, links correct
- frostspark-boots.html: [ok] Standard format, links correct
- nights-edge.html: [ok] Standard format, links correct
- pda.html: [ok] Standard format, links correct
- terra-blade.html: [ok] Standard format, links correct
- terraspark-boots.html: [ok] Standard format, links correct
- zenith.html: [ok] Standard format, links correct

### ZH页面 (10/10 OK)
- zh/ankh-charm.html: [ok] Standard format, links correct
- zh/ankh-shield.html: [ok] Standard format, links correct
- zh/avenger-emblem.html: [ok] Standard format, links correct
- zh/cell-phone.html: [ok] Standard format, links correct
- zh/frostspark-boots.html: [ok] Standard format, links correct
- zh/nights-edge.html: [ok] Standard format, links correct
- zh/pda.html: [ok] Standard format, links correct
- zh/terra-blade.html: [ok] Standard format, links correct
- zh/terraspark-boots.html: [ok] Standard format, links correct
- zh/zenith.html: [ok] Standard format, links correct
