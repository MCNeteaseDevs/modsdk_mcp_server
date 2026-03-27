# -*- coding: utf-8 -*-
"""UI JSON 模板生成 + manifest 便捷函数"""
import json
import uuid


def _make_button(name, size, label_text, label_color=None, anchor_from="center", anchor_to="center", offset=None):
    """生成符合官方规范的 button 控件（继承 common.button + 4状态子控件）。"""
    ctrl = {
        "size": size,
        "button_mappings": [],
        "anchor_from": anchor_from,
        "anchor_to": anchor_to,
    }
    if offset:
        ctrl["offset"] = offset
    ctrl["controls"] = [
        {"default": {"type": "image", "texture": "textures/ui/button_borderless_light", "size": ["100%", "100%"]}},
        {"hover": {"type": "image", "texture": "textures/ui/button_borderless_lighthover", "size": ["100%", "100%"]}},
        {"pressed": {"type": "image", "texture": "textures/ui/button_borderless_lightpressed", "size": ["100%", "100%"]}},
        {"button_label": {"type": "label", "text": label_text, "color": label_color or [1, 1, 1], "layer": 1}},
    ]
    return {"{}@common.button".format(name): ctrl}


def generate_ui_json(template, namespace, **kwargs):
    """生成 JSON UI 文件模板。

    Args:
        template: 模板类型 (screen/shop_grid/dialog/hud/tab_panel)
        namespace: 命名空间（全局唯一）

    Returns:
        {"ui_json": JSON UI 内容, "ui_defs_entry": _ui_defs 条目, "screen_name": 屏幕名, "usage_hint": 使用说明}
    """
    screen_name = kwargs.get('screen_name', namespace + '_screen')
    usage_extra = ""

    if template == 'screen':
        ui = {
            "namespace": namespace,
            screen_name: {
                "type": "screen",
                "absorbs_input": True,
                "is_showing_menu": True,
                "render_game_behind": True,
                "controls": [{
                    "main_panel": {
                        "type": "panel",
                        "size": ["100%", "100%"],
                        "controls": [
                            {"title_label": {"type": "label", "text": kwargs.get('title', ''), "color": [1, 1, 1], "font_size": "large", "anchor_from": "top_middle", "anchor_to": "top_middle", "offset": [0, 10]}},
                            _make_button("close_btn", [20, 20], "X", anchor_from="top_right", anchor_to="top_right", offset=[-5, 5]),
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
                    {"price_label": {"type": "label", "text": "", "color": [1, 0.84, 0], "font_size": "small", "anchor_from": "bottom_middle", "anchor_to": "bottom_middle", "offset": [0, -12]}},
                ]
            },
            "shop_grid_content": {
                "type": "grid",
                "grid_dimensions": [columns, 0],
                "grid_item_template": namespace + ".item_cell",
                "collection_name": "shop_items",
                "grid_rescaling_type": "none",
                "maximum_grid_items": 0,
                "size": ["100%", "default"],
            },
            screen_name: {
                "type": "screen",
                "absorbs_input": True,
                "is_showing_menu": True,
                "controls": [{
                    "bg_panel": {
                        "type": "panel", "size": ["80%", "80%"],
                        "controls": [
                            {"bg_image": {"type": "image", "size": ["100%", "100%"], "texture": "textures/ui/White", "color": [0.1, 0.1, 0.1], "alpha": 0.8}},
                            {"title": {"type": "label", "text": kwargs.get('title', '商店'), "color": [1, 1, 1], "font_size": "large", "anchor_from": "top_middle", "anchor_to": "top_middle", "offset": [0, 8]}},
                            {"scroll_area@common.scrolling_panel": {
                                "size": ["95%", "85%"],
                                "anchor_from": "bottom_middle", "anchor_to": "bottom_middle", "offset": [0, -8],
                                "$scrolling_content": namespace + ".shop_grid_content",
                                "$show_background": False,
                            }},
                        ]
                    }
                }]
            }
        }
        usage_extra = "\n4. [重要] grid与scroll_view一起使用时，必须监听GridComponentSizeChangedClientEvent，否则滚动时内容错位。详见UI说明文档grid章节注2。"

    elif template == 'dialog':
        ui = {
            "namespace": namespace,
            screen_name: {
                "type": "screen",
                "absorbs_input": True,
                "is_showing_menu": True,
                "controls": [{
                    "dialog_panel": {
                        "type": "panel", "size": [240, 140],
                        "controls": [
                            {"bg": {"type": "image", "size": ["100%", "100%"], "texture": "textures/ui/White", "color": [0.1, 0.1, 0.1], "alpha": 0.9}},
                            {"title": {"type": "label", "text": kwargs.get('title', '确认'), "color": [1, 1, 1], "font_size": "large", "anchor_from": "top_middle", "anchor_to": "top_middle", "offset": [0, 10]}},
                            {"message": {"type": "label", "text": kwargs.get('message', ''), "color": [0.8, 0.8, 0.8]}},
                            _make_button("confirm_btn", [80, 24], kwargs.get('confirm_text', '确认'), anchor_from="bottom_middle", anchor_to="bottom_middle", offset=[-50, -10]),
                            _make_button("cancel_btn", [80, 24], kwargs.get('cancel_text', '取消'), label_color=[0.8, 0.8, 0.8], anchor_from="bottom_middle", anchor_to="bottom_middle", offset=[50, -10]),
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
                            {"value_label": {"type": "label", "text": kwargs.get('default_text', '0'), "color": [1, 1, 1]}},
                            {"value_label": {"type": "label", "text": kwargs.get('default_text', '0'), "color": [1, 1, 1]}}
                        ]
                    }},
                    {"bar_bg": {
                        "type": "image", "size": [102, 7],
                        "anchor_from": "top_left", "anchor_to": "top_left", "offset": [5, 27],
                        "texture": "textures/ui/bar_bg",
                        "controls": [{"bar_fill": {"type": "image", "size": ["100%", "100%"], "texture": "textures/ui/bar_fill", "clip_direction": "left", "clip_ratio": 0.0}}],
                    }},
                ]
            },
            screen_name: {
                "type": "screen",
                "is_showing_menu": False,
                "force_render_below": True,
                "render_game_behind": True,
                "absorbs_input": False,
                "controls": [{"hud@" + namespace + ".hud_element": {}}],
            }
        }

    elif template == 'tab_panel':
        tabs = kwargs.get('tabs', ['Tab1', 'Tab2', 'Tab3'])
        tab_ctrls = []
        content_ctrls = []
        for i, tn in enumerate(tabs):
            tab_ctrls.append({"tab_{}@common_toggles.switch_toggle_collection".format(i): {
                "size": [60, 24],
                "$toggle_name": "tab_toggle",
                "$toggle_default_state": i == 0,
                "$toggle_group_forced_index": i,
                "$default_texture": "textures/ui/toggle_off",
                "$hover_texture": "textures/ui/toggle_on",
                "$pressed_texture": "textures/ui/toggle_off_hover",
                "$pressed_no_hover_texture": "textures/ui/toggle_on_hover",
                "$toggle_state_binding_name": "#tab_toggle_state",
                "controls": [{"label": {"type": "label", "text": tn, "color": [1, 1, 1], "layer": 2}}],
            }})
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
                "absorbs_input": True,
                "is_showing_menu": True,
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
        "usage_hint": "1. Save to resource_pack/ui/{ns}.json\n2. Add to _ui_defs.json: {{\"ui_defs\": [\"ui/{ns}.json\"]}}\n3. Python: RegisterUI(ns, uiKey, clsPath, '{ns}.{sn}') + CreateUI(ns, uiKey){extra}".format(
            ns=namespace, sn=screen_name, e=entry, extra=usage_extra)
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
