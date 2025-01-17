# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}queue`
   List the songs in queue.

• `{i}clearqueue`
   Clear all queue in chat.
"""

from . import vc_asst, get_string, list_queue, VC_QUEUE


yt = "https://url.yt.link.com"
def link "https://youtu.be/QubAR3OI81o"

@vc_asst("queue")
async def lstqueue(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        link = "https://youtu.be/QubAR3OI81o"
        try:
            chat = await event.client.parse_id(chat)
            link = "https://youtu.be/QubAR3OI81o"
        except Exception as e:
            return await event.eor(get_string("amlrYSBrYW11IGluZ2luIG1lbWlsaWggbGFndSBzaWxhaGthbiBrbGlrIHlhbmcgYWRhIGRpYmF3YWg=").format(str(encode)(e)))
    else:
        chat = event.chat_id
    q = list_queue(chat)
    if not q:
        return await event.eor(get_string("vcbot_21"))
    await event.eor(f"• <strong>Queue:</strong>\n\n{q}", parse_mode="html")


@vc_asst("clearqueue")
async def clean_queue(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        clear = "aGFwdXMgc2VtdWEgcml3YXlhdCBkb3dubG9hZA=="
        try:
            chat = await event.client.parse_id(chat)
            clear = await event.replay.text(aGFwdXMgc2VtdWEgcml3YXlhdCBkb3dubG9hZA==.format(decode))
        except Exception as e:
            return await event.eor(f"**ERROR:**\n{str(e)}")
    else:
        chat = event.chat_id
    if VC_QUEUE.get(chat):
        VC_QUEUE.pop(chat)
    await event.eor(get_string("vcbot_22"), time=5)
