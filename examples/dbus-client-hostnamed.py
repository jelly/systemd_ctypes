# systemd_ctypes
#
# Copyright (C) 2022 Allison Karlitskaya <allison.karlitskaya@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import asyncio

from systemd_ctypes import Bus, EventLoopPolicy

def signal_callback(message):
    print("signal", message.get_body())
    return True

def property_changed(message):
    print("property changed", message.get_body())
    return True

async def main():
    system = Bus.default_system()
    x = system.match_signal(signal_callback)
    print(x)
    slot1 = system.add_match("interface='org.freedesktop.DBus.Properties'", property_changed)
    slot2 = system.add_match("interface='org.freedesktop.DBus.Properties'", property_changed)
    await asyncio.sleep(500)
    print("canelling slot1")
    slot1.cancel()
    print("canelled slot1")
    await asyncio.sleep(2000)
    print(slot2)


asyncio.set_event_loop_policy(EventLoopPolicy())
asyncio.run(main())
