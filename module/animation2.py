import asyncio
from collections import deque
from telethon import TelegramClient, events


@events.register(events.NewMessage(pattern=r".star", outgoing=True))
async def star(event):
    if event.fwd_from:
        return
    deq = deque(list("π¦β¨π¦β¨π¦β¨π¦β¨"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@events.register(events.NewMessage(pattern=r".boxs"))
async def boxs(event):
    if event.fwd_from:
        return
    deq = deque(list("π₯π§π¨π©π¦πͺπ«β¬β¬"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@events.register(events.NewMessage(pattern=f".rain", outgoing=True))
async def rain(event):
    if event.fwd_from:
        return
    deq = deque(list("π¬βοΈπ©π¨π§π¦π₯βπ€"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@events.register(events.NewMessage(pattern=r".clol"))
async def clol(event):
    if event.fwd_from:
        return
    deq = deque(list("π€π§π€¨π€π§π€¨"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@events.register(events.NewMessage(pattern=r".odra"))
async def odra(event):
    if event.fwd_from:
        return
    deq = deque(list("πΆππΆππΆππΆπ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)



@events.register(events.NewMessage(pattern=".fleaveme"))
async def fleaveme(event):
    animation_interval = 1
    animation_ttl = range(0, 10)
    animation_chars = [
        "β¬β¬β¬\nβ¬β¬β¬\nβ¬β¬β¬",
        "β¬β¬β¬\nβ¬πβ¬\nβ¬β¬β¬",
        "β¬β¬οΈβ¬\nβ¬πβ¬\nβ¬β¬β¬",
        "β¬β¬οΈβοΈ\nβ¬πβ¬\nβ¬β¬β¬",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβ¬β¬β¬",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβ¬β¬βοΈ",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβ¬β¬οΈβοΈ",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβοΈβ¬οΈβοΈ",
        "β¬β¬οΈβοΈ\nβ¬οΈπβ‘οΈ\nβοΈβ¬οΈβοΈ",
        "βοΈβ¬οΈβοΈ\nβ¬οΈπβ‘οΈ\nβοΈβ¬οΈβοΈ",
    ]
    if event.fwd_from:
        return
    await event.edit("fleaveme....")
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@events.register(events.NewMessage(pattern=".loveu", outgoing=True))
async def loveu(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 70)
    await event.edit("loveu")
    animation_chars = [
        "π",
        "π©βπ¨",
        "π",
        "π",
        "π€£",
        "π",
        "π",
        "π",
        "π",
        "βΊ",
        "π",
        "π€",
        "π€¨",
        "π",
        "π",
        "πΆ",
        "π£",
        "π₯",
        "π?",
        "π€",
        "π―",
        "π΄",
        "π",
        "π",
        "βΉ",
        "π",
        "π",
        "π",
        "π",
        "π’",
        "π­",
        "π€―",
        "π",
        "β€",
        "i Love Youβ€",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


@events.register(events.NewMessage(pattern=".plane", outgoing=True))
async def plane(event):
    if event.fwd_from:
        return
    await event.edit("β-------------")
    await event.edit("-β------------")
    await event.edit("--β-----------")
    await event.edit("---β----------")
    await event.edit("----β---------")
    await event.edit("-----β--------")
    await event.edit("------β-------")
    await event.edit("-------β------")
    await event.edit("--------β-----")
    await event.edit("---------β----")
    await event.edit("----------β---")
    await event.edit("-----------β--")
    await event.edit("------------β-")
    await event.edit("-------------β")
    await asyncio.sleep(3)
    await event.delete()


@events.register(events.NewMessage(pattern=r".police"))
async def police(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 12)
    await event.edit("Police")
    animation_chars = [
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        f"{1} **Police iz Here**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@events.register(events.NewMessage(pattern=".jio", outgoing=True))
async def jio(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 19)
    await event.edit("jio network boosting...")
    animation_chars = [
        "`Connecting To JIO NETWORK ....`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "*Optimising JIO NETWORK...*",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "**JIO NETWORK Boosted....**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 19])


@events.register(events.NewMessage(pattern=f".solarsystem", outgoing=True))
async def solarsystem(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 80)
    await event.edit("solarsystem")
    animation_chars = [
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])
