# -*- coding: utf-8 -*-
"""UI JSON 模板生成 + manifest 便捷函数"""
import json
import uuid


def generate_ui_json(template, namespace, **kwargs):
    """生成 JSON UI 文件模板。

    Args:
        template: 模板类型 (screen/shop_grid/dialog/hud/tab_panel)
        namespace: 命名空间（全局唯一）

    Returns:
        {"ui_json": JSON UI 内容, "ui_defs_entry": _ui_defs 条目, "screen_name": 屏幕名, "usage_hint": 使用说明}
    """
    screen_name = kwargs.get('screen_name', namespace + '_screen')

    if template == 'screen':
        ui = {
            "namespace": namespace,
            screen_name: {
                "type": "screen",
                "controls": [{
                    "main_panel": {
                        "type": "panel",
                        "size": ["100%", "100%"],
                        "controls": [
                            {"title_label": {"type": "label", "text": kwargs.get('title', ''), "color": [1, 1, 1], "font_size": "large", "anchor_from": "top_middle", "anchor_to": "top_middle", "offset": [0, 10]}},
                            {"close_btn": {"type": "button", "size": [20, 20], "anchor_from": "top_right", "anchor_to": "top_right", "offset": [-5, 5],
                                "controls": [{"label": {"type": "label", "text": "X", "color": [1, 1, 1]}}]}}
                        ]
                    }
                }]
            }
        }

    elif template == 'shop_grid':
        columns = kwargs.get('columns', 4)
        ui = {
            "namespace": namespace,
            "item_cell": {
                "type": "panel", "size": [50, 60],
                "controls": [
                    {"item_icon": {"type": "image", "size": [32, 32], "anchor_from": "top_middle", "anchor_to": "top_middle", "offset": [0, 2]}},
                    {"item_name": {"type": "label", "text": "", "font_size": "small", "anchor_from": "bottom_middle", "anchor_to": "bottom_middle", "offset": [0, -2]}},
                    {"price_label": {"type": "label", "text": "", "color": [1, 0.84, 0], "font_size": "small", "anchor_from": "bottom_middle", "anchor_to": "bottom_middle", "offset": [0, -12]}}
                ]
            },
            screen_name: {
                "type": "screen",
                "controls": [{
                    "bg_panel": {
                        "type": "panel", "size": ["80%", "80%"],
                        "controls": [
                            {"bg_image": {"type": "image", "size": ["100%", "100%"], "texture": "textures/ui/bg_dark", "alpha": 0.8}},
                            {"title": {"type": "label", "text": kwargs.get('title', '商店'), "color": [1, 1, 1], "font_size": "large", "anchor_from": "top_middle", "anchor_to": "top_middle", "offset": [0, 8]}},
                            {"scroll_area": {
                                "type": "scroll_view", "size": ["95%", "85%"],
                                "anchor_from": "bottom_middle", "anchor_to": "bottom_middle", "offset": [0, -8],
                                "scroll_content": {
                                    "type": "grid",
                                    "grid_dimensions": [columns, 0],
                                    "grid_item_template": namespace + ".item_cell",
                                    "collection_name": "shop_items"
                                }
                            }}
                        ]
                    }
                }]
            }
        }

    elif template == 'dialog':
        ui = {
            "namespace": namespace,
            screen_name: {
                "type": "screen",
                "controls": [{
                    "dialog_panel": {
                        "type": "panel", "size": [240, 140],
                        "controls": [
                            {"bg": {"type": "image", "size": ["100%", "100%"], "texture": "textures/ui/bg_dark", "alpha": 0.9}},
                            {"title": {"type": "label", "text": kwargs.get('title', '确认'), "color": [1, 1, 1], "font_size": "large", "anchor_from": "top_middle", "anchor_to": "top_middle", "offset": [0, 10]}},
                            {"message": {"type": "label", "text": kwargs.get('message', ''), "color": [0.8, 0.8, 0.8]}},
                            {"confirm_btn": {"type": "button", "size": [80, 24], "anchor_from": "bottom_middle", "anchor_to": "bottom_middle", "offset": [-50, -10],
                                "controls": [{"label": {"type": "label", "text": kwargs.get('confirm_text', '确认'), "color": [1, 1, 1]}}]}},
                            {"cancel_btn": {"type": "button", "size": [80, 24], "anchor_from": "bottom_middle", "anchor_to": "bottom_middle", "offset": [50, -10],
                                "controls": [{"label": {"type": "label", "text": kwargs.get('cancel_text', '取消'), "color": [0.8, 0.8, 0.8]}}]}}
                        ]
                    }
                }]
            }
        }

    elif template == 'hud':
        ui = {
            "namespace": namespace,
            "hud_element": {
                "type": "panel", "size": ["100%", "100%"],
                "controls": [
                    {"info_panel": {
                        "type": "stack_panel", "orientation": "horizontal", "size": [200, 20],
                        "anchor_from": "top_left", "anchor_to": "top_left", "offset": [5, 5],
                        "controls": [
                            {"icon": {"type": "image", "size": [16, 16], "texture": kwargs.get('icon', 'textures/ui/icon')}},
                            {"spacer": {"type": "panel", "size": [4, 0]}},
                            {"value_label": {"type": "label", "text": kwargs.get('default_text', '0'), "color": [1, 1, 1]}}
                        ]
                    }},
                    {"bar_bg": {
                        "type": "image", "size": [102, 7],
                        "anchor_from": "top_left", "anchor_to": "top_left", "offset": [5, 27],
                        "texture": "textures/ui/bar_bg",
                        "controls": [{"bar_fill": {"type": "image", "size": ["100%", "100%"], "texture": "textures/ui/bar_fill", "clip_direction": "left", "clip_ratio": 1.0}}]
                    }}
                ]
            }
        }

    elif template == 'tab_panel':
        tabs = kwargs.get('tabs', ['Tab1', 'Tab2', 'Tab3'])
        tab_ctrls = []
        content_ctrls = []
        for i, tn in enumerate(tabs):
            tab_ctrls.append({"tab_{}".format(i): {
                "type": "toggle", "size": [60, 24], "toggle_name": "tab_toggle",
                "toggle_default_state": i == 0, "toggle_group_forced_index": i,
                "controls": [{"label": {"type": "label", "text": tn, "color": [1, 1, 1]}}]
            }})
            content_ctrls.append({"content_{}".format(i): {
                "type": "panel", "size": ["100%", "100%"], "visible": i == 0,
                "bindings": [{"binding_type": "view", "source_property_name": "(not (#tab_toggle - {}))".format(i), "target_property_name": "#visible"}],
                "controls": [{"placeholder": {"type": "label", "text": "{} content".format(tn), "color": [0.7, 0.7, 0.7]}}]
            }})

        ui = {
            "namespace": namespace,
            screen_name: {
                "type": "screen",
                "controls": [{
                    "main_panel": {
                        "type": "panel", "size": ["80%", "80%"],
                        "controls": [
                            {"bg": {"type": "image", "size": ["100%", "100%"], "texture": "textures/ui/bg_dark", "alpha": 0.8}},
                            {"tab_bar": {"type": "stack_panel", "orientation": "horizontal", "size": ["100%", 28],
                                "anchor_from": "top_left", "anchor_to": "top_left", "offset": [0, 4], "controls": tab_ctrls}},
                            {"content_area": {"type": "panel", "size": ["100%", "100% - 36px"],
                                "anchor_from": "bottom_left", "anchor_to": "bottom_left", "controls": content_ctrls}}
                        ]
                    }
                }]
            }
        }
    else:
        return {"error": "Unknown template: {}. Available: screen/shop_grid/dialog/hud/tab_panel".format(template)}

    ui_json = json.dumps(ui, indent=4, ensure_ascii=False)
    entry = "ui/{}.json".format(namespace)
    return {
        "ui_json": ui_json,
        "ui_defs_entry": entry,
        "screen_name": screen_name,
        "usage_hint": "1. Save to resource_pack/ui/{ns}.json\n2. Add to _ui_defs.json: \"{e}\"\n3. Python: RegisterUI(ns, screenCls) + CreateUI(ns, uiKey)".format(ns=namespace, e=entry)
    }


def generate_manifest_json(mod_name, description="", version="1.0.0"):
    """生成行为包+资源包 manifest.json（UUID自动生成）"""
    from .templates import BedrockJsonGenerator

    v = [int(x) for x in version.split(".")]
    vt = (v[0] if len(v) > 0 else 1, v[1] if len(v) > 1 else 0, v[2] if len(v) > 2 else 0)
    bh, bm = str(uuid.uuid4()), str(uuid.uuid4())
    rh, rm = str(uuid.uuid4()), str(uuid.uuid4())

    beh = BedrockJsonGenerator.generate_behavior_pack_manifest(
        mod_name, description or mod_name, bh, bm, vt, resource_pack_uuid=rh)
    res = BedrockJsonGenerator.generate_resource_pack_manifest(
        mod_name, description or mod_name, rh, rm, vt)

    return {
        "behavior_manifest": beh,
        "resource_manifest": res,
        "note": "UUID已自动生成，行为包通过dependencies关联资源包。"
    }
