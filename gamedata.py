from collections import namedtuple

server_maintainance_start = "1:59:00"
server_maintainance_end = "2:20:00"

healthTable = {
"you are fit":6,
"you are exhausted":5,
"you are weak":4,
"you are skinny":3,
"you are bony":2,
"you are dying":1,
"you are dead":0
}

hungerTable = {
"you are not hungry.":0,
"you\\'re hungry":1,
"you\\'re veryhungry":2,
"you\\'re very hungry":2,
"you\\'re very\\nhungry":2,
"you're very very hungry":3 #check this
}

scrape_strings = {
"hunger":"hunger\s*:\s*",
"health":"(health|fitness)\s*:\s*",
"activity":"activity\s*:\s*",
}


stat_strings = {
"str":"strength",
"int":"intelligence",
"charisma":"charisma",
"rep":"reputation points"
}


activity_strings = {
"mine":'you are working in the mine', 
"imw":'you are working for the province',
"travel":'traveling',
"none":'none',
"lake":'fishing',
"orchard":'picking fruit',
"forest":'cut wood',
"search":"Search for valuable resources",
}


resource_strings = {
"lake":"lake",
"orchard":"orchard",
"forest":"forest",
}


item_strings = {
"boat":"canoe",
"small ladder":"small ladder",
"large ladder":"large ladder",
"axe":"obsidian axe",
}

GameStrings = namedtuple('GameStrings', ['scrape', 'stats', 'activity', 'resource', 'items'])
game_strings = GameStrings(scrape = scrape_strings, stats = stat_strings, activity = activity_strings,
                           resource = resource_strings, items = item_strings)

item_map = {
"money":0,
"pound":0,
"pounds":0,

"tortilla":50,
"tortillas":50,
"bread":50,
"loaf of bread":50,
"loaves of bread":50,
"fruit":51,
"fruits":51,
"corn":52,
"beans":52,
"bean":52,
"bag of corn":52,
"bags of corn":52,
"egg":53,
"eggs":53,
"milk":53,
"bottle of milk":53,
"bottles of milk":53,
"fish":54,
"fishes":54,
"meat":55,
"piece of meat":55,
"pieces of meat":55,
"wheat":56,
"bag of wheat":56,
"bags of wheat":56,
"flour":57,
"bag of flour":57,
"bags of flour":57,

"half-hundredweight of pig":60,
"half-hundredweights of pig":60,
"wool":61,
"ball of wool":61,
"balls of wool":61,
"hide":62,
"hides":62,

"vegetable":64,
"vegetables":64,
"wood":65,
"wood bushel":65,
"wood bushels":65,
"small ladder":66,
"small ladders":66,
"large ladder":67,
"large ladders":67,
"oar":68,
"oars":68,
"shaft":70,
"shafts":70,
"boat":71,
"boats":71,

"axe":73,
"axes":73,

"iron ore":76,
"ounces of iron ore":76,
"ounce of iron ore":76,
"unhooped bucket":77,
"unhooped buckets":77,
"buckets":78,
"bucket":78,
"knife":79,
"knives":79,

#fuck the clothing

"sword":105,
"swords":105,
"shield":106,
"shields":106,

"sprig of marjoram":352,
"sprigs of marjoram":352,
"feverfew blossom":353,
"feverfew blossoms":353,
"lime leaf":354,
"lime leaves":354,
"celery stalk":355,
"celery stalks":355,
"sprig of lavender":356,
"sprigs of lavender":356,
"anise flower":357,
"anise flowers":357,
"rosemary sprig":358,
"rosemary sprigs":358,
"sprig of rosemary":358,
"sprigs of rosemary":358,
"thyme branch":359,
"thyme branches":359,
"piece of white willow bark":360,
"pieces of white willow bark":360,
"angelica sprig":361,
"angelica sprigs":361,
"borage flower":362,
"borage flowers":362,
"mint leaf":363,
"mint leaves":363,
"chamomile flower":364,
"chamomile flowers":364,
"black elder berry":365,
"black elder berries":365
}


hp_info = {   
"bread":2,
"loaves of bread":2,
"loaf of bread":2,
"tortilla":2,
"tortillas":2,
"fruit":1,
"fruits":1,
"bean":1,
"beans":1,
"corn":1,
"bags of corn":1,
"bag of corn":1,
"bag of beans":1,
"bags of beans":1,
"egg":1,
"eggs":1,
"milk":1,
"bottle of milk":1,
"bottles of milk":1,
"egg":1,
"eggs":1,
"fish":2,
"fishes":2,
"meat":2,
"piece of meat":2,
"pieces of meat":2,
"vegetable":1,
"vegetables":1
}


r_food_map = {
50:"bread",
51:"fruits",
52:"corn",
53:"milk",
54:"fish",
55:"meat",
64:"vegetables"
}


field_map = {
"wheat":1,
"corn":2,
"vegetables":6,
"vegetable":6
}

node_map = {
    
}

r_field_map = {
1:"wheat",
2:"corn",
6:"vegetables"
}

__all__ = ["server_maintainance_start", "server_maintainance_end", "healthTable", "hungerTable", 
           "game_strings", "item_map", "hp_info", "r_food_map", "node_map", "field_map", "r_field_map"]
