from telethon import TelegramClient, events, sync
#
from time import gmtime, strftime
from emoji import emojize
import asyncio
#

import module.client,  module.test,  module.bombs,  module.help,  module.loading,  module.emoji, module.type,  module.magicrun,  module.animation,  module.animation2, module.mute, module.fuck,  module.tr,  module.userinfo,  module.base64, module.snow
#
client = module.client.client
#
with client as friday:
	friday.add_event_handler(module.test.test) 
with client as friday:
	friday.add_event_handler(module.bombs.bombs)
with client as friday:
	friday.add_event_handler(module.help.help) 
with client as friday:
	friday.add_event_handler(module.loading.loading) 
with client as friday:
	friday.add_event_handler(module.emoji.itachi) 
with client as friday:
	friday.add_event_handler(module.type.type) 
with client as friday:
	friday.add_event_handler(module.magicrun.magicrun) 	
with client as friday:
	friday.add_event_handler(module.animation.lul)
with client as friday:
	friday.add_event_handler(module.animation.snake)
with client as friday:
	friday.add_event_handler(module.animation.nothappy)
with client as friday:
	friday.add_event_handler(module.animation.clock)
with client as friday:
	friday.add_event_handler(module.animation.muah)
with client as friday:
	friday.add_event_handler(module.animation.heart)	
with client as friday:
	friday.add_event_handler(module.animation.gym)
with client as friday:
	friday.add_event_handler(module.animation.earth)
with client as friday:
	friday.add_event_handler(module.animation.moon)
with client as friday:
	friday.add_event_handler(module.animation.candy)
with client as friday:
	friday.add_event_handler(module.animation.smoon)
with client as friday:
	friday.add_event_handler(module.animation.tmoon)
with client as friday:
	friday.add_event_handler(module.animation.clown)
with client as friday:
	friday.add_event_handler(module.animation2.star)
with client as friday:
	friday.add_event_handler(module.animation2.boxs)		
with client as friday:
	friday.add_event_handler(module.animation2.rain)
with client as friday:
	friday.add_event_handler(module.animation2.clol)
with client as friday:
	friday.add_event_handler(module.animation2.odra)
with client as friday:
	friday.add_event_handler(module.animation2.fleaveme)		
with client as friday:
	friday.add_event_handler(module.animation2.loveu)
with client as friday:
	friday.add_event_handler(module.animation2.plane)
with client as friday:
	friday.add_event_handler(module.animation2.police)
with client as friday:
	friday.add_event_handler(module.animation2.jio)		
with client as friday:
	friday.add_event_handler(module.animation2.solarsystem)
with client as friday:
	friday.add_event_handler(module.mute.mute)		
with client as friday:
	friday.add_event_handler(module.fuck.fuck)															
with client as friday:
	friday.add_event_handler(module.tr.tr)
with client as friday:
	friday.add_event_handler(module.userinfo.userinfo)
with client as friday:
	friday.add_event_handler(module.base64.runb64)				
with client as friday:
	friday.add_event_handler(module.snow.snow)				

	

client.start()
print("""
██╗   ██╗███████╗███████╗██████╗ ██████╗  ██████╗ ████████╗
██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██║   ██║███████╗█████╗  ██████╔╝██████╔╝██║   ██║   ██║   
██║   ██║╚════██║██╔══╝  ██╔══██╗██╔══██╗██║   ██║   ██║   
╚██████╔╝███████║███████╗██║  ██║██████╔╝╚██████╔╝   ██║   
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝   

\033[1;32mUSERBOT STARTED""")

client.run_until_disconnected()