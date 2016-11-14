##########################################################
## ADVENTURE GAME STARTS HERE
##########################################################
import random
from adven import *

# start by creating the game system
game = Game("Tunnel Collapse")

# define and describe a couple of locations
deadend = game.new_location(
"Dead End {e}",
"""The air is damp and your arms ache from trying to mine gold
from this barren mountain.  It must have been hours since you
last saw anyone, not even the overbearing foreman.\n
You decide checking to see if anyone is sharing in your bad luck
is enough cause to take a break.\n""")

tunnel = game.new_location(
"Tunnel {e, w}",
"""You don't believe you will ever get used to this oppressive heat
this far into the mountain.  You expect to find someone around the
upcoming bend in the tunnel.\n""")

tunnelbend = game.new_location(
"A Bend in the Tunnel {e, w}",
"""You start talking about how poor your luck is as you round the
turn hoping to see that someone is having the same streak of bad
luck as you.\n
No one is in sight.  You see a pick that is on the ground and shards
of rock in various piles.  There is also a cage with a canary in it
on the ground.\n""")

intersection = game.new_location(
"Tunnel Intersection {n,e,s,w}",
"""You have come to a 4-way intersection in the tunnel, foot prints
lead in all directions.\n""")

i1_n1 = game.new_location(
"Tunnel {n,s}",
"""You head north from the intersection, hoping to find some of your
fellow miners.  Worry starts to creep into your head.\n""")

i1_s1 = game.new_location(
"Tunnel {n,s}",
"""You head north from the intersection, hoping to find some of your
fellow miners.  Worry starts to creep into your head.\n""")

i1_e1 = game.new_location(
"Tunnel {e,w}",
"""You head north from the intersection, hoping to find some of your
fellow miners.  Worry starts to creep into your head.\n""")

i1_n2 = game.new_location(
"Dark Tunnel {n,s}",
"""Continuing north from the intersection, you notice some footprints
on the ground leading further into the tunnel, getting darker and darker.\n""")

i1_n3 = game.new_location(
"Steep Inclined Tunnel {n,s}",
"""It is getting oppressively dark as you notice the tunnel climbing upwards.
You'll have to find a lightsource to continue forward.\n""")

i1_n4 = game.new_location(
"Mine Shaft {s, down}",
"""Lighting the torch, you are able to continue to the end of this section
of tunnel.  You slowly approach a verticle mine shaft that has fell into
disrepair.\n
You notice that there has been a newly made rope attached to a wooden crane
arm, did someone go down?\n""")




# room connections
game.new_connection(
"Tunnel",
deadend, tunnel,
[EAST], [WEST])

game.new_connection(
"Tunnel",
tunnel, tunnelbend,
[EAST], [WEST])

game.new_connection(
"Tunnel Intersection",
tunnelbend, intersection,
[EAST],[WEST])

game.new_connection(
"Tunnel",
intersection, i1_n1,
[NORTH],[SOUTH])

game.new_connection(
"Tunnel",
intersection, i1_s1,
[SOUTH], [NORTH])

game.new_connection(
"Tunnel",
intersection, i1_e1,
[EAST], [WEST])

game.new_connection(
"Dark Tunnel",
i1_n1, i1_n2,
[NORTH, FORWARD], [SOUTH, BACK])

game.new_connection(
"Steep Incline",
i1_n2, i1_n3,
[NORTH, FORWARD], [SOUTH, BACK])

game.new_connection(
"Dark Mine Shaft",
i1_n3, i1_n4,
[NORTH, FORWARD], [SOUTH, BACK])

# Now let's add some items, by providing a single word name and a longer
# description.
shard = deadend.new_object(
"rock",
"""Shard of chipped rock you have fractured off the walls of the mine have
started to pile up""")

cage = tunnelbend.add_object(
Container(
"birdcage",
"""There is a standard issue birdcage, hopefully the bird it carried
is still around."""))

pick = tunnelbend.new_object(
"mining pick",
"""A well-cared for pick, it's obvious its owner cared about his job,
which makes you wonder why they left it on the ground.""")

torch = i1_n2.new_object(
"torch",
"""This torch still holds some heat from when it was lit, someone just
recently doused it.""")

cage.new_object(
"bird seed",
"""you see some bird seed on the bottom of the cage.""")

# NPC Characters
canary = Animal("canary")
canary.set_location(i1_e1)
canary.set_allowed_locations = (
[i1_e1, intersection, i1_n1, i1_n2, i1_n3, i1_s1, tunnelbend, tunnel, deadend])
game.add_actor(canary)

#Function to feed the Canary, keep in mind that while this either feeds
#the bird or not, you could call the Die("you die") function to kill the player,
# or the player.terminate() or canary.terminate() function!
def feed_canary(game, thing):
    if not "bird seed" in game.player.inventory and "rock" in game.player.inventory:
        game.output(
        """Thinking the shard of rock you are holding is a seed, the canary
        flies over and snatches it out of your hand, and then plummets to the
         ground.""")
        canary.terminate()
    if "bird seed" in game.player.inventory and not "rock" in game.player.inventory:
        game.output(
        """You sprinkle some bird seed onto your palm and after a few minutes
        the canary lands on your hand and starts pecking at the seed before
        flying away again.""")
    else:
        game.output("Feed canary with what?")

canary.add_phrase("feed canary", feed_canary)


# And we can make the torch required to proceed down the dark tunnel
i1_n4.make_requirement(torch)


player = game.new_player(deadend)


game.run()
