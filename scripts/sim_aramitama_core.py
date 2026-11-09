#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
『荒魂の國 - 乱世漂泊録 -』 コアメカニクス検証シミュレータ (MASTER VISION v2.2)
=============================================================================
検証項目:
  1. 乗算ハイブリッドクラフト到達品質モデル（第5章5-5・第8章8-3・第11章11-1）
  2. 30人マルチ×100日間『数打ち』vs『真打（生涯3振）』銘の流通・噂話確率検証（第7章7-3・第8章8-2）
  3. 『太陽の影の長さ＝瘴気の潮位』＆日蝕（黒き日輪）汽水域濃度計算モデル（第10章10-4）
  4. 属性タグ×引き算による「マルチ解法（別解）試練」判定エンジン（第6章6-2）
  5. 外殻ゲージ＆部位破壊4拍サイクル・刃の損耗（考証10 §6 / data/combat_5_attributes.json）
"""
import json
import math
from pathlib import Path

COMBAT_JSON = Path(__file__).resolve().parent.parent / "data" / "combat_5_attributes.json"

def calc_craft_quality(skill: float, material: float, facility_mult: float, env_mult: float) -> dict:
    """
    【到達品質】＝ ベース(技量×0.6 ＋ 素材×0.4) × 工房設備倍率(1.0〜1.4) × 環境共鳴倍率(1.0〜1.3)
    """
    base = skill * 0.6 + material * 0.4
    score = round(base * facility_mult * env_mult, 1)
    if score >= 120.0:
        grade = "【神宝・真打（銘入れ解禁）】"
    elif score >= 95.0:
        grade = "【業物（上級品）】"
    elif score >= 60.0:
        grade = "【良作（実用品・数打ち）】"
    else:
        grade = "【並作・なまくら】"
    return {"skill": skill, "material": material, "facility": facility_mult, "env": env_mult, "score": score, "grade": grade}

def sim_shinuchi_circulation(players: int = 30, days: int = 100, shinuchi_per_gen: int = 3) -> dict:
    """
    数打ち無制限銘入れ vs 1世代3振の『真打』限定銘入れの有名NPC装着率比較
    """
    kazuuchi_total = players * (days // 3)  # 3日に1本製作 = 990本
    famous_warlords = 30
    kazuuchi_adoption_rate = round((famous_warlords / kazuuchi_total) * 100, 1)

    shinuchi_total = players * shinuchi_per_gen  # 1世代3振 × 30人 = 90本
    historical_holders = 60  # 有名武将30＋曲者家臣・高僧・他PC主武装30
    shinuchi_adoption_rate = round((historical_holders / shinuchi_total) * 100, 1)

    return {
        "kazuuchi_total_blades": kazuuchi_total,
        "kazuuchi_famous_rate_pct": kazuuchi_adoption_rate,
        "shinuchi_total_blades": shinuchi_total,
        "shinuchi_famous_rate_pct": shinuchi_adoption_rate
    }

def calc_brackish_miasma(terrain_depth: float, shadow_intensity: float, barrier_power: float) -> dict:
    """
    【その場所の今の瘴気濃度】＝ ①地形の深さ(0〜50) ＋ ②今の影の濃さ(0〜60) － ③結界からの陽気(0〜80)
    """
    density = max(0.0, round(terrain_depth + shadow_intensity - barrier_power, 1))
    if density == 0:
        zone = "安全圏（陽だまり / 乾いた道祖神）"
    elif density < 30:
        zone = "薄汽水（河川側 / 白っぽい日差し・路傍の彼岸花）"
    elif density < 65:
        zone = "中汽水（中間帯 / 足首の白靄・松明が五寸に縮む）"
    else:
        zone = "濃汽水（海側・常世の波打ち際 / 膝丈の黒霧・松明消滅）"
    return {"density": density, "zone": zone}

def evaluate_trial_namakura_boar(action_tags: list) -> dict:
    """
    試練①『なまくら刀の一太刀』マルチ解法判定デモ
    なまくら古刀の許容硬度 = 20 / 泥鎧の大猪の初期装甲硬度 = 80
    """
    blade_limit = 20
    boar_armor = 80
    applied_methods = []

    if "mouth_open_timing" in action_tags:
        boar_armor -= 65
        applied_methods.append("正攻法：突進後の口内露出タイミング狙い (-65)")
    if "water_wetland_lure" in action_tags:
        boar_armor -= 65
        applied_methods.append("別解A：湿地・水辺への誘導による泥鎧ふやかし (-65)")
    if "strong_sake_bait" in action_tags or "sleep_herb" in action_tags:
        boar_armor -= 70
        applied_methods.append("別解B：強い濁り酒・眠り草餌による泥酔無防備化 (-70)")

    effective_armor = max(0, boar_armor)
    passed = effective_armor <= blade_limit
    return {
        "action_tags": action_tags,
        "applied_methods": applied_methods,
        "effective_armor": effective_armor,
        "blade_limit": blade_limit,
        "passed": passed,
        "master_comment": "見事じゃ！理（ことわり）を知ればなまくらでも大猪の牙は折れるわい！" if passed else "馬鹿者！泥が乾いて硬いうちに正面から斬るから刃が欠けるのじゃ！"
    }


def load_combat_data(path: Path = COMBAT_JSON) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def blade_state(durability: float, max_durability: float, stages: list) -> str:
    """残り耐久の割合から刃の状態（刃こぼれ・目釘のゆるみ・曲がり/折れ）を返す"""
    ratio = durability / max_durability if max_durability else 0.0
    if ratio <= 0:
        return next(s["state"] for s in stages if "at_ratio" in s)
    for s in sorted((s for s in stages if "below_ratio" in s), key=lambda s: s["below_ratio"]):
        if ratio < s["below_ratio"]:
            return s["state"]
    return "健全"


def sim_shell_combat_cycle(weapon_id: str, motion_id: str, base_damage: float,
                           initial_shell: float = 80.0, initial_durability: int = 40,
                           data: dict = None) -> dict:
    """
    外殻破壊4拍サイクル（剥がす➔断つ➔穿つ➔鎮める）の損耗・ダメージ計算モデル
    モーションの属性配分・衝撃・刃の負担は data/combat_5_attributes.json から読む。
    - 外殻減少量 = 打撃の割合(blunt/10) × 衝撃値 × base_coefficient(10)
    - 外殻が残っている間: 刃の負担 × blade_strain_multiplier(3.0)
    - 外殻破壊後: 打撃 × 1.0 / 切断 × 1.5 / 貫通 × 1.75 を、手の属性配分で加重平均する
      （刃のない道具に斬ダメージが付かないようにするため）
    """
    data = data or load_combat_data()
    weapon = next(w for w in data["weapon_classes"] if w["id"] == weapon_id)
    motion = next(m for m in weapon["motions"] if m["id"] == motion_id)
    hp = data["hit_parameters"]
    gauge = data["shell_gauge"]

    blunt_ratio = motion["attrs"].get("blunt", 0) / 10
    impact = hp["impact_scale"][motion["impact"]]
    strain = hp["blade_strain_scale"][motion["blade_strain"]]
    shell_decay_per_hit = blunt_ratio * impact * gauge["base_coefficient"]
    hits_to_break = math.ceil(initial_shell / shell_decay_per_hit) if shell_decay_per_hit > 0 else None

    has_blade = weapon["blade_strain"] != "なし"
    intact_strain_mult = gauge["states"]["intact"]["blade_strain_multiplier"]
    strain_before_break = (hits_to_break or 0) * strain * intact_strain_mult
    remaining = max(0.0, initial_durability - strain_before_break)
    stages = data["blade_durability"]["stages"]

    broken_mult = gauge["states"]["broken"]["damage_multiplier"]
    attrs = motion["attrs"]
    attr_total = sum(attrs.values()) or 1
    post_break_mult = sum(v / attr_total * broken_mult.get(k, 1.0) for k, v in attrs.items())

    return {
        "weapon": weapon["name"],
        "motion": motion["name"],
        "label": f"打撃{motion['attrs'].get('blunt', 0)}割・衝撃{motion['impact']}{impact}・刃の負担{motion['blade_strain']}",
        "shell_decay_per_hit": round(shell_decay_per_hit, 1),
        "hits_to_break": hits_to_break,
        "strain_before_break": strain_before_break,
        "remaining_durability": remaining if has_blade else None,
        "blade_state": blade_state(remaining, initial_durability, stages) if has_blade else "刃なし",
        "post_break_damage": round(base_damage * post_break_mult, 1),
    }

if __name__ == "__main__":
    print("=" * 72)
    print("⛩️ 『荒魂の國 - 乱世漂泊録 -』 コアメカニクス検証シミュレータ (v2.2)")
    print("=" * 72)

    print("\n[1] 乗算ハイブリッド・クラフト品質計算式の検証:")
    cases = [
        ("見習い（序幕・若者初期）", 30, 40, 1.0, 1.0),
        ("2代目若造（低技量で先代の最高設備を使用）", 35, 50, 1.4, 1.2),
        ("免許皆伝直後（技量80・奥出雲真砂）", 80, 80, 1.25, 1.15),
        ("極意皆伝・一代吹き（技量100・玉鋼・神火共鳴）", 100, 95, 1.35, 1.25),
    ]
    for label, sk, mat, fac, env in cases:
        res = calc_craft_quality(sk, mat, fac, env)
        print(f"  - {label}: スコア {res['score']} ➔ {res['grade']}")

    print("\n[2] 30人マルチ・100日間『数打ち』vs『真打』流通確率:")
    circ = sim_shinuchi_circulation()
    print(f"  - 数打ち全銘入れ時 ({circ['kazuuchi_total_blades']}振): 有名武将装着率 = {circ['kazuuchi_famous_rate_pct']}%")
    print(f"  - 生涯3振『真打』限定時 ({circ['shinuchi_total_blades']}振): 歴史担い手装着率 = {circ['shinuchi_famous_rate_pct']}%")

    print("\n[3] 『太陽の影の長さ＝瘴気の潮位』＆日蝕シミュレーション（神門水海・白鹿山）:")
    tide_cases = [
        ("神門水海・正午の引き潮（影最短）", 25, 5, 10),
        ("神門水海・夕暮れの上げ潮（里結び前）", 25, 45, 10),
        ("神門水海・夕暮れの上げ潮（里結び完成後）", 25, 45, 55),
        ("白鹿山・真昼の皆既日蝕『黒き日輪』（太陽高度0化）", 40, 60, 20),
    ]
    for label, depth, shadow, barrier in tide_cases:
        t_res = calc_brackish_miasma(depth, shadow, barrier)
        print(f"  - {label}: 濃度 {t_res['density']} ➔ {t_res['zone']}")

    print("\n[4] マルチ解法試練『なまくら刀の一太刀』属性タグ判定:")
    for tags in [["frontal_slash"], ["water_wetland_lure"], ["strong_sake_bait"]]:
        tr = evaluate_trial_namakura_boar(tags)
        status = "【合格】" if tr["passed"] else "【不合格】"
        print(f"  - タグ {tags}: 実効装甲={tr['effective_armor']} <= 刀許容={tr['blade_limit']} {status} 『{tr['master_comment']}』")


    print("\n[5] 外殻ゲージ計算＆部位破壊4拍サイクル（泥猪の頭 外殻80・なまくら刀耐久40）:")
    combat_data = load_combat_data()
    combat_test_cases = [
        ("uchigatana", "mine_uchi", 20.0),
        ("uchigatana", "uchikomi", 25.0),
        ("odachi", "furioroshi", 35.0),
        ("yari", "tataki", 25.0),
        ("kakeya", "furioroshi", 30.0),
        ("otsuchi", "furioroshi", 35.0),
        ("kanasaibo", "furioroshi", 45.0),
    ]
    for w_id, m_id, dmg in combat_test_cases:
        c_res = sim_shell_combat_cycle(w_id, m_id, dmg, data=combat_data)
        dur = "刃なし" if c_res["remaining_durability"] is None else f"{c_res['remaining_durability']:g}/40・{c_res['blade_state']}"
        print(f"  - {c_res['weapon']}【{c_res['motion']}】（{c_res['label']}）: 1撃の外殻削り={c_res['shell_decay_per_hit']} ➔ 外殻80破壊まで【{c_res['hits_to_break']}回】 (破壊時の刃={dur}, 外殻破壊後の1撃={c_res['post_break_damage']})")
