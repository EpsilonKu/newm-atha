from __future__ import annotations
from typing import Any, TYPE_CHECKING, Optional

import json
import logging
from dasbus.connection import SessionMessageBus  # type: ignore


if TYPE_CHECKING:
    from ..layout import Layout

logger = logging.getLogger(__name__)


class Command:
    __dbus_xml__ = """
    <node>
        <interface name="org.newm.Command">
            <method name="Call">
                <arg direction="in" name="args" type="s" />
                <arg direction="out" name="return" type="s" />
            </method>
        </interface>
    </node>
    """

    def __init__(self, layout: Layout):
        self.layout = layout

    def Call(self, args: str) -> str:
        args_dict = json.loads(args)
        try:
            if args_dict['cmd'] == 'launcher':
                self.layout.launch_app(args_dict['app'])
                res_dict = { 'msg': 'OK' }
            elif args_dict['cmd'] == 'current-window-title':
                w = self.layout.find_focused_view()
                if w is None:
                    res_dict = {'msg':'no focused window'}
                res_dict = {'msg': w.title}
            elif args_dict['cmd'] == 'current-window-ssd':
                w = self.layout.find_focused_window()
                if w is None:
                     res_dict = {'msg':'no focused window'}
                __res = False if w._ssd  == None else True
                res_dict = {'msg': str(__res)}
            elif args_dict['cmd'] == 'current-workspace-num':
               res_dict = {'msg':str(self.layout.get_active_workspace._handle)}
            else:
                res_dict = { 'msg': str(self.layout.command(args_dict['cmd'], args_dict['arg'] if 'arg' in args_dict else None)) }
            return json.dumps(res_dict)
        except Exception as e:
            return json.dumps({ 'exception': str(e) })


def send_dbus_command(args: dict[str, Any]) -> Optional[dict[str, Any]]:
    bus = SessionMessageBus()
    proxy = bus.get_proxy("org.newm.Command", "/org/newm/Command")
    res = proxy.Call(json.dumps(args))
    try:
        return json.loads(res)
    except:
        return None
