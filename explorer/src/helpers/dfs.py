"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
# from getRoute import graph

graph = {
    "0": {
        "coordinates": "(60,60)",
        "elevation": 0,
        "exits": {
            "e": "4",
            "n": "10",
            "s": "2",
            "w": "1"
        },
        "terrain": "NORMAL",
        "title": "A brightly lit room"
    },
    "1": {
        "coordinates": "(59,60)",
        "elevation": 0,
        "exits": {
            "e": "0"
        },
        "terrain": "NORMAL",
        "title": "Shop"
    },
    "10": {
        "coordinates": "(60,61)",
        "elevation": 0,
        "exits": {
            "n": "19",
            "s": "0",
            "w": "43"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "100": {
        "coordinates": "(64,54)",
        "elevation": 0,
        "exits": {
            "e": "112",
            "s": "106",
            "w": "68"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "101": {
        "coordinates": "(56,62)",
        "elevation": 0,
        "exits": {
            "n": "91",
            "w": "113"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "102": {
        "coordinates": "(57,56)",
        "elevation": 0,
        "exits": {
            "s": "98",
            "w": "142"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "103": {
        "coordinates": "(65,65)",
        "elevation": 0,
        "exits": {
            "n": "160",
            "w": "69"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "104": {
        "coordinates": "(64,60)",
        "elevation": 0,
        "exits": {
            "e": "107",
            "n": "59"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "105": {
        "coordinates": "(60,53)",
        "elevation": 2,
        "exits": {
            "n": "48",
            "w": "202"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "106": {
        "coordinates": "(64,53)",
        "elevation": 0,
        "exits": {
            "n": "100",
            "s": "111",
            "w": "135"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "107": {
        "coordinates": "(65,60)",
        "elevation": 0,
        "exits": {
            "e": "121",
            "s": "120",
            "w": "104"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "108": {
        "coordinates": "(61,53)",
        "elevation": 3,
        "exits": {
            "e": "93",
            "n": "78",
            "s": "117"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "109": {
        "coordinates": "(56,55)",
        "elevation": 0,
        "exits": {
            "e": "98",
            "s": "185",
            "w": "175"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "11": {
        "coordinates": "(62,58)",
        "elevation": 1,
        "exits": {
            "e": "17",
            "w": "9"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "110": {
        "coordinates": "(58,65)",
        "elevation": 0,
        "exits": {
            "e": "76"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "111": {
        "coordinates": "(64,52)",
        "elevation": 0,
        "exits": {
            "e": "158",
            "n": "106",
            "s": "367"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "112": {
        "coordinates": "(65,54)",
        "elevation": 0,
        "exits": {
            "e": "140",
            "s": "141",
            "w": "100"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "113": {
        "coordinates": "(55,62)",
        "elevation": 0,
        "exits": {
            "e": "101",
            "s": "114"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "114": {
        "coordinates": "(55,61)",
        "elevation": 0,
        "exits": {
            "n": "113",
            "w": "176"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "115": {
        "coordinates": "(62,66)",
        "elevation": 0,
        "exits": {
            "e": "95",
            "n": "116"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "116": {
        "coordinates": "(62,67)",
        "elevation": 0,
        "exits": {
            "n": "132",
            "s": "115"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "117": {
        "coordinates": "(61,52)",
        "elevation": 2,
        "exits": {
            "e": "166",
            "n": "108",
            "s": "131",
            "w": "133"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "118": {
        "coordinates": "(65,58)",
        "elevation": 0,
        "exits": {
            "e": "137",
            "w": "42"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "119": {
        "coordinates": "(63,67)",
        "elevation": 0,
        "exits": {
            "n": "134",
            "s": "95"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "12": {
        "coordinates": "(61,57)",
        "elevation": 3,
        "exits": {
            "e": "14",
            "n": "9",
            "s": "18",
            "w": "21"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "120": {
        "coordinates": "(65,59)",
        "elevation": 0,
        "exits": {
            "e": "127",
            "n": "107"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "121": {
        "coordinates": "(66,60)",
        "elevation": 0,
        "exits": {
            "e": "143",
            "n": "128",
            "w": "107"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "122": {
        "coordinates": "(61,65)",
        "elevation": 0,
        "exits": {
            "e": "88",
            "n": "124"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "123": {
        "coordinates": "(66,62)",
        "elevation": 0,
        "exits": {
            "w": "66"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "124": {
        "coordinates": "(61,66)",
        "elevation": 0,
        "exits": {
            "n": "157",
            "s": "122"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "125": {
        "coordinates": "(58,66)",
        "elevation": 0,
        "exits": {
            "e": "83",
            "n": "165",
            "w": "237"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "126": {
        "coordinates": "(57,54)",
        "elevation": 0,
        "exits": {
            "n": "98",
            "s": "129"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "127": {
        "coordinates": "(66,59)",
        "elevation": 0,
        "exits": {
            "e": "184",
            "w": "120"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "128": {
        "coordinates": "(66,61)",
        "elevation": 0,
        "exits": {
            "e": "189",
            "s": "121"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "129": {
        "coordinates": "(57,53)",
        "elevation": 0,
        "exits": {
            "e": "194",
            "n": "126",
            "w": "?"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "13": {
        "coordinates": "(62,60)",
        "elevation": 0,
        "exits": {
            "e": "15",
            "w": "4"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "130": {
        "coordinates": "(60,66)",
        "elevation": 0,
        "exits": {
            "w": "83"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "131": {
        "coordinates": "(61,51)",
        "elevation": 1,
        "exits": {
            "n": "117",
            "s": "244",
            "w": "138"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "132": {
        "coordinates": "(62,68)",
        "elevation": 0,
        "exits": {
            "s": "116"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "133": {
        "coordinates": "(60,52)",
        "elevation": 1,
        "exits": {
            "e": "117",
            "w": "173"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "134": {
        "coordinates": "(63,68)",
        "elevation": 0,
        "exits": {
            "e": "144",
            "n": "147",
            "s": "119"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "135": {
        "coordinates": "(63,53)",
        "elevation": 0,
        "exits": {
            "e": "106",
            "s": "150"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "136": {
        "coordinates": "(57,57)",
        "elevation": 0,
        "exits": {
            "e": "49",
            "w": "148"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "137": {
        "coordinates": "(66,58)",
        "elevation": 0,
        "exits": {
            "w": "118"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "138": {
        "coordinates": "(60,51)",
        "elevation": 0,
        "exits": {
            "e": "131",
            "s": "211",
            "w": "195"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "139": {
        "coordinates": "(56,60)",
        "elevation": 0,
        "exits": {
            "e": "65",
            "w": "188"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "14": {
        "coordinates": "(62,57)",
        "elevation": 2,
        "exits": {
            "e": "37",
            "s": "34",
            "w": "12"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "140": {
        "coordinates": "(66,54)",
        "elevation": 0,
        "exits": {
            "w": "112"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "141": {
        "coordinates": "(65,53)",
        "elevation": 0,
        "exits": {
            "e": "156",
            "n": "112"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "142": {
        "coordinates": "(56,56)",
        "elevation": 0,
        "exits": {
            "e": "102",
            "w": "159"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "143": {
        "coordinates": "(67,60)",
        "elevation": 0,
        "exits": {
            "e": "212",
            "w": "121"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "144": {
        "coordinates": "(64,68)",
        "elevation": 0,
        "exits": {
            "e": "155",
            "w": "134"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "145": {
        "coordinates": "(66,64)",
        "elevation": 0,
        "exits": {
            "e": "220",
            "n": "174",
            "w": "57"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "146": {
        "coordinates": "(54,63)",
        "elevation": 0,
        "exits": {
            "e": "99",
            "n": "215",
            "s": "177",
            "w": "257"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "147": {
        "coordinates": "(63,69)",
        "elevation": 0,
        "exits": {
            "e": "153",
            "n": "200",
            "s": "134",
            "w": "151"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "148": {
        "coordinates": "(56,57)",
        "elevation": 0,
        "exits": {
            "e": "136",
            "w": "292"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "149": {
        "coordinates": "(59,54)",
        "elevation": 2,
        "exits": {
            "e": "48"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "15": {
        "coordinates": "(63,60)",
        "elevation": 0,
        "exits": {
            "w": "13"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "150": {
        "coordinates": "(63,52)",
        "elevation": 0,
        "exits": {
            "n": "135",
            "w": "166"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "151": {
        "coordinates": "(62,69)",
        "elevation": 0,
        "exits": {
            "e": "147",
            "n": "172",
            "w": "207"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "152": {
        "coordinates": "(64,67)",
        "elevation": 0,
        "exits": {
            "s": "94"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "153": {
        "coordinates": "(64,69)",
        "elevation": 0,
        "exits": {
            "e": "329",
            "w": "147"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "154": {
        "coordinates": "(66,55)",
        "elevation": 0,
        "exits": {
            "e": "193",
            "w": "85"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "155": {
        "coordinates": "(65,68)",
        "elevation": 0,
        "exits": {
            "e": "316",
            "s": "187",
            "w": "144"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "156": {
        "coordinates": "(66,53)",
        "elevation": 0,
        "exits": {
            "e": "164",
            "s": "168",
            "w": "141"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "157": {
        "coordinates": "(61,67)",
        "elevation": 0,
        "exits": {
            "n": "210",
            "s": "124",
            "w": "182"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "158": {
        "coordinates": "(65,52)",
        "elevation": 0,
        "exits": {
            "s": "167",
            "w": "111"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "159": {
        "coordinates": "(55,56)",
        "elevation": 0,
        "exits": {
            "e": "142",
            "w": "196"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "16": {
        "coordinates": "(58,59)",
        "elevation": 0,
        "exits": {
            "e": "8",
            "n": "58",
            "w": "67"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "160": {
        "coordinates": "(65,66)",
        "elevation": 0,
        "exits": {
            "s": "103"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "161": {
        "coordinates": "(56,61)",
        "elevation": 0,
        "exits": {
            "e": "74"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "162": {
        "coordinates": "(56,59)",
        "elevation": 0,
        "exits": {
            "e": "67"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "163": {
        "coordinates": "(58,54)",
        "elevation": 1,
        "exits": {
            "n": "70"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "164": {
        "coordinates": "(67,53)",
        "elevation": 0,
        "exits": {
            "e": "298",
            "n": "217",
            "w": "156"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "165": {
        "coordinates": "(58,67)",
        "elevation": 0,
        "exits": {
            "n": "203",
            "s": "125",
            "w": "204"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "166": {
        "coordinates": "(62,52)",
        "elevation": 1,
        "exits": {
            "e": "150",
            "s": "198",
            "w": "117"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "167": {
        "coordinates": "(65,51)",
        "elevation": 0,
        "exits": {
            "e": "260",
            "n": "158",
            "s": "262"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "168": {
        "coordinates": "(66,52)",
        "elevation": 0,
        "exits": {
            "e": "340",
            "n": "156"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "169": {
        "coordinates": "(65,63)",
        "elevation": 0,
        "exits": {
            "e": "186",
            "s": "66"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "17": {
        "coordinates": "(63,58)",
        "elevation": 0,
        "exits": {
            "e": "42",
            "n": "24",
            "w": "11"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "171": {
        "coordinates": "(56,58)",
        "elevation": 0,
        "exits": {
            "e": "61"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "172": {
        "coordinates": "(62,70)",
        "elevation": 0,
        "exits": {
            "n": "267",
            "s": "151"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "173": {
        "coordinates": "(59,52)",
        "elevation": 0,
        "exits": {
            "e": "133",
            "w": "214"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "174": {
        "coordinates": "(66,65)",
        "elevation": 0,
        "exits": {
            "e": "224",
            "n": "192",
            "s": "145"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "175": {
        "coordinates": "(55,55)",
        "elevation": 0,
        "exits": {
            "e": "109",
            "s": "183",
            "w": "?"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "176": {
        "coordinates": "(54,61)",
        "elevation": 0,
        "exits": {
            "e": "114",
            "w": "402"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "177": {
        "coordinates": "(54,62)",
        "elevation": 0,
        "exits": {
            "n": "146",
            "w": "346"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "178": {
        "coordinates": "(67,57)",
        "elevation": 0,
        "exits": {
            "e": "243",
            "n": "209",
            "w": "90"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "18": {
        "coordinates": "(61,56)",
        "elevation": 4,
        "exits": {
            "n": "12",
            "s": "22",
            "w": "25"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "180": {
        "coordinates": "(56,64)",
        "elevation": 0,
        "exits": {
            "s": "91"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "181": {
        "coordinates": "(67,56)",
        "elevation": 0,
        "exits": {
            "w": "97"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "182": {
        "coordinates": "(60,67)",
        "elevation": 0,
        "exits": {
            "e": "157",
            "w": "208"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "183": {
        "coordinates": "(55,54)",
        "elevation": 0,
        "exits": {
            "n": "175",
            "s": "229"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "184": {
        "coordinates": "(67,59)",
        "elevation": 0,
        "exits": {
            "e": "221",
            "w": "127"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "185": {
        "coordinates": "(56,54)",
        "elevation": 0,
        "exits": {
            "n": "109"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "186": {
        "coordinates": "(66,63)",
        "elevation": 0,
        "exits": {
            "e": "205",
            "w": "169"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "187": {
        "coordinates": "(65,67)",
        "elevation": 0,
        "exits": {
            "n": "155"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "188": {
        "coordinates": "(55,60)",
        "elevation": 0,
        "exits": {
            "e": "139",
            "w": "335"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "189": {
        "coordinates": "(67,61)",
        "elevation": 0,
        "exits": {
            "e": "255",
            "w": "128"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "19": {
        "coordinates": "(60,62)",
        "elevation": 0,
        "exits": {
            "n": "20",
            "s": "10",
            "w": "77"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "190": {
        "coordinates": "(55,64)",
        "elevation": 0,
        "exits": {
            "s": "99"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "191": {
        "coordinates": "(57,65)",
        "elevation": 0,
        "exits": {
            "s": "82"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "192": {
        "coordinates": "(66,66)",
        "elevation": 0,
        "exits": {
            "e": "223",
            "n": "201",
            "s": "174"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "193": {
        "coordinates": "(67,55)",
        "elevation": 0,
        "exits": {
            "e": "251",
            "w": "154"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "194": {
        "coordinates": "(58,53)",
        "elevation": 0,
        "exits": {
            "s": "214",
            "w": "129"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "195": {
        "coordinates": "(59,51)",
        "elevation": 0,
        "exits": {
            "e": "138",
            "s": "228",
            "w": "?"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "196": {
        "coordinates": "(54,56)",
        "elevation": 0,
        "exits": {
            "e": "159",
            "n": "222",
            "w": "?"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "198": {
        "coordinates": "(62,51)",
        "elevation": 0,
        "exits": {
            "e": "199",
            "n": "166",
            "s": "239"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "199": {
        "coordinates": "(63,51)",
        "elevation": 0,
        "exits": {
            "s": "230",
            "w": "198"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "2": {
        "coordinates": "(60,59)",
        "elevation": 0,
        "exits": {
            "e": "3",
            "n": "0",
            "s": "6"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "20": {
        "coordinates": "(60,63)",
        "elevation": 0,
        "exits": {
            "e": "27",
            "n": "63",
            "s": "19",
            "w": "46"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "200": {
        "coordinates": "(63,70)",
        "elevation": 0,
        "exits": {
            "e": "206",
            "n": "227",
            "s": "147"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "201": {
        "coordinates": "(66,67)",
        "elevation": 0,
        "exits": {
            "s": "192"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "202": {
        "coordinates": "(59,53)",
        "elevation": 1,
        "exits": {
            "e": "105"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "203": {
        "coordinates": "(58,68)",
        "elevation": 0,
        "exits": {
            "e": "299",
            "n": "268",
            "s": "165"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "204": {
        "coordinates": "(57,67)",
        "elevation": 0,
        "exits": {
            "e": "165",
            "n": "219",
            "w": "216"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "205": {
        "coordinates": "(67,63)",
        "elevation": 0,
        "exits": {
            "e": "479",
            "s": "241",
            "w": "186"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "206": {
        "coordinates": "(64,70)",
        "elevation": 0,
        "exits": {
            "e": "380",
            "n": "288",
            "w": "200"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "207": {
        "coordinates": "(61,69)",
        "elevation": 0,
        "exits": {
            "e": "151",
            "n": "231",
            "w": "290"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "208": {
        "coordinates": "(59,67)",
        "elevation": 0,
        "exits": {
            "e": "182"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "209": {
        "coordinates": "(67,58)",
        "elevation": 0,
        "exits": {
            "s": "178"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "21": {
        "coordinates": "(60,57)",
        "elevation": 2,
        "exits": {
            "e": "12",
            "w": "29"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "210": {
        "coordinates": "(61,68)",
        "elevation": 0,
        "exits": {
            "s": "157"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "211": {
        "coordinates": "(60,50)",
        "elevation": 0,
        "exits": {
            "n": "138"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "212": {
        "coordinates": "(68,60)",
        "elevation": 0,
        "exits": {
            "w": "143"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "214": {
        "coordinates": "(58,52)",
        "elevation": 0,
        "exits": {
            "e": "173",
            "n": "194",
            "w": "?"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "215": {
        "coordinates": "(54,64)",
        "elevation": 0,
        "exits": {
            "n": "246",
            "s": "146"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "216": {
        "coordinates": "(56,67)",
        "elevation": 0,
        "exits": {
            "e": "204",
            "n": "234",
            "w": "218"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "217": {
        "coordinates": "(67,54)",
        "elevation": 0,
        "exits": {
            "e": "247",
            "s": "164"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "218": {
        "coordinates": "(55,67)",
        "elevation": 0,
        "exits": {
            "e": "216",
            "s": "263",
            "w": "242"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "219": {
        "coordinates": "(57,68)",
        "elevation": 0,
        "exits": {
            "s": "204"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "22": {
        "coordinates": "(61,55)",
        "elevation": 5,
        "exits": {
            "n": "18",
            "s": "78",
            "w": "36"
        },
        "terrain": "MOUNTAIN",
        "title": "The Peak of Mt. Holloway"
    },
    "220": {
        "coordinates": "(67,64)",
        "elevation": 0,
        "exits": {
            "w": "145"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "221": {
        "coordinates": "(68,59)",
        "elevation": 0,
        "exits": {
            "e": "240",
            "s": "253",
            "w": "184"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "222": {
        "coordinates": "(54,57)",
        "elevation": 0,
        "exits": {
            "n": "305",
            "s": "196"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "223": {
        "coordinates": "(67,66)",
        "elevation": 0,
        "exits": {
            "n": "283",
            "w": "192"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "224": {
        "coordinates": "(67,65)",
        "elevation": 0,
        "exits": {
            "w": "174"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "227": {
        "coordinates": "(63,71)",
        "elevation": 0,
        "exits": {
            "n": "269",
            "s": "200"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "228": {
        "coordinates": "(59,50)",
        "elevation": 0,
        "exits": {
            "n": "195",
            "s": "281"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "229": {
        "coordinates": "(55,53)",
        "elevation": 0,
        "exits": {
            "n": "183",
            "s": "250",
            "w": "?"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "23": {
        "coordinates": "(61,61)",
        "elevation": 0,
        "exits": {
            "e": "26",
            "s": "4"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "230": {
        "coordinates": "(63,50)",
        "elevation": 0,
        "exits": {
            "e": "297",
            "n": "199",
            "s": "307"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "231": {
        "coordinates": "(61,70)",
        "elevation": 0,
        "exits": {
            "s": "207",
            "w": "248"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "234": {
        "coordinates": "(56,68)",
        "elevation": 0,
        "exits": {
            "n": "368",
            "s": "216",
            "w": "252"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "237": {
        "coordinates": "(57,66)",
        "elevation": 0,
        "exits": {
            "e": "125",
            "w": "245"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "239": {
        "coordinates": "(62,50)",
        "elevation": 0,
        "exits": {
            "n": "198",
            "w": "244"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "24": {
        "coordinates": "(63,59)",
        "elevation": 0,
        "exits": {
            "s": "17"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "240": {
        "coordinates": "(69,59)",
        "elevation": 0,
        "exits": {
            "e": "386",
            "n": "249",
            "w": "221"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "241": {
        "coordinates": "(67,62)",
        "elevation": 0,
        "exits": {
            "e": "266",
            "n": "205"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "242": {
        "coordinates": "(54,67)",
        "elevation": 0,
        "exits": {
            "e": "218",
            "n": "287",
            "s": "259",
            "w": "275"
        },
        "terrain": "TRAP",
        "title": "A Dark Cave"
    },
    "243": {
        "coordinates": "(68,57)",
        "elevation": 0,
        "exits": {
            "e": "256",
            "s": "293",
            "w": "178"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "244": {
        "coordinates": "(61,50)",
        "elevation": 0,
        "exits": {
            "e": "239",
            "n": "131"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "245": {
        "coordinates": "(56,66)",
        "elevation": 0,
        "exits": {
            "e": "237",
            "s": "254"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "246": {
        "coordinates": "(54,65)",
        "elevation": 0,
        "exits": {
            "s": "215"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "247": {
        "coordinates": "(68,54)",
        "elevation": 0,
        "exits": {
            "e": "261",
            "w": "217"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "248": {
        "coordinates": "(60,70)",
        "elevation": 0,
        "exits": {
            "e": "231",
            "n": "296",
            "w": "280"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "249": {
        "coordinates": "(69,60)",
        "elevation": 0,
        "exits": {
            "e": "282",
            "n": "265",
            "s": "240"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "25": {
        "coordinates": "(60,56)",
        "elevation": 3,
        "exits": {
            "e": "18"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "250": {
        "coordinates": "(55,52)",
        "elevation": 0,
        "exits": {
            "e": "?",
            "n": "229",
            "s": "294"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "251": {
        "coordinates": "(68,55)",
        "elevation": 0,
        "exits": {
            "e": "315",
            "w": "193"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "252": {
        "coordinates": "(55,68)",
        "elevation": 0,
        "exits": {
            "e": "234",
            "n": "284"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "253": {
        "coordinates": "(68,58)",
        "elevation": 0,
        "exits": {
            "e": "258",
            "n": "221"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "254": {
        "coordinates": "(56,65)",
        "elevation": 0,
        "exits": {
            "n": "245",
            "w": "314"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "255": {
        "coordinates": "(68,61)",
        "elevation": 0,
        "exits": {
            "w": "189"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "256": {
        "coordinates": "(69,57)",
        "elevation": 0,
        "exits": {
            "e": "327",
            "s": "360",
            "w": "243"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "257": {
        "coordinates": "(53,63)",
        "elevation": 0,
        "exits": {
            "e": "146",
            "n": "320",
            "w": "364"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "258": {
        "coordinates": "(69,58)",
        "elevation": 0,
        "exits": {
            "e": "306",
            "w": "253"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "259": {
        "coordinates": "(54,66)",
        "elevation": 0,
        "exits": {
            "n": "242",
            "w": "310"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "26": {
        "coordinates": "(62,61)",
        "elevation": 0,
        "exits": {
            "e": "55",
            "w": "23"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "260": {
        "coordinates": "(66,51)",
        "elevation": 0,
        "exits": {
            "w": "167"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "261": {
        "coordinates": "(69,54)",
        "elevation": 0,
        "exits": {
            "e": "322",
            "s": "277",
            "w": "247"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "262": {
        "coordinates": "(65,50)",
        "elevation": 0,
        "exits": {
            "e": "358",
            "n": "167",
            "s": "370"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "263": {
        "coordinates": "(55,66)",
        "elevation": 0,
        "exits": {
            "n": "218"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "265": {
        "coordinates": "(69,61)",
        "elevation": 0,
        "exits": {
            "e": "270",
            "n": "279",
            "s": "249"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "266": {
        "coordinates": "(68,62)",
        "elevation": 0,
        "exits": {
            "w": "241"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "267": {
        "coordinates": "(62,71)",
        "elevation": 0,
        "exits": {
            "n": "285",
            "s": "172",
            "w": "271"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "268": {
        "coordinates": "(58,69)",
        "elevation": 0,
        "exits": {
            "e": "411",
            "s": "203",
            "w": "312"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "269": {
        "coordinates": "(63,72)",
        "elevation": 0,
        "exits": {
            "n": "319",
            "s": "227"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "27": {
        "coordinates": "(61,63)",
        "elevation": 0,
        "exits": {
            "e": "30",
            "n": "40",
            "s": "28",
            "w": "20"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "270": {
        "coordinates": "(70,61)",
        "elevation": 0,
        "exits": {
            "e": "338",
            "n": "416",
            "w": "265"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "271": {
        "coordinates": "(61,71)",
        "elevation": 0,
        "exits": {
            "e": "267",
            "n": "337"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "275": {
        "coordinates": "(53,67)",
        "elevation": 0,
        "exits": {
            "e": "242",
            "w": "456"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "277": {
        "coordinates": "(69,53)",
        "elevation": 0,
        "exits": {
            "e": "323",
            "n": "261"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "279": {
        "coordinates": "(69,62)",
        "elevation": 0,
        "exits": {
            "s": "265"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "28": {
        "coordinates": "(61,62)",
        "elevation": 0,
        "exits": {
            "n": "27"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "280": {
        "coordinates": "(59,70)",
        "elevation": 0,
        "exits": {
            "e": "248",
            "n": "325"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "281": {
        "coordinates": "(59,49)",
        "elevation": 0,
        "exits": {
            "e": "309",
            "n": "228",
            "s": "318",
            "w": "?"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "282": {
        "coordinates": "(70,60)",
        "elevation": 0,
        "exits": {
            "w": "249"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "283": {
        "coordinates": "(67,67)",
        "elevation": 0,
        "exits": {
            "e": "313",
            "n": "331",
            "s": "223"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "284": {
        "coordinates": "(55,69)",
        "elevation": 0,
        "exits": {
            "n": "302",
            "s": "252",
            "w": "303"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "285": {
        "coordinates": "(62,72)",
        "elevation": 0,
        "exits": {
            "n": "286",
            "s": "267"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "286": {
        "coordinates": "(62,73)",
        "elevation": 0,
        "exits": {
            "n": "336",
            "s": "285",
            "w": "291"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "287": {
        "coordinates": "(54,68)",
        "elevation": 0,
        "exits": {
            "s": "242",
            "w": "339"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "288": {
        "coordinates": "(64,71)",
        "elevation": 0,
        "exits": {
            "s": "206"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "29": {
        "coordinates": "(59,57)",
        "elevation": 1,
        "exits": {
            "e": "21",
            "s": "45",
            "w": "49"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "290": {
        "coordinates": "(60,69)",
        "elevation": 0,
        "exits": {
            "e": "207"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "291": {
        "coordinates": "(61,73)",
        "elevation": 0,
        "exits": {
            "e": "286",
            "n": "410",
            "w": "347"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "292": {
        "coordinates": "(55,57)",
        "elevation": 0,
        "exits": {
            "e": "148",
            "n": "301"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "293": {
        "coordinates": "(68,56)",
        "elevation": 0,
        "exits": {
            "n": "243"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "294": {
        "coordinates": "(55,51)",
        "elevation": 0,
        "exits": {
            "n": "250",
            "s": "334"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "296": {
        "coordinates": "(60,71)",
        "elevation": 0,
        "exits": {
            "s": "248"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "297": {
        "coordinates": "(64,50)",
        "elevation": 0,
        "exits": {
            "w": "230"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "298": {
        "coordinates": "(68,53)",
        "elevation": 0,
        "exits": {
            "s": "324",
            "w": "164"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "299": {
        "coordinates": "(59,68)",
        "elevation": 0,
        "exits": {
            "e": "311",
            "w": "203"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "3": {
        "coordinates": "(61,59)",
        "elevation": 1,
        "exits": {
            "e": "5",
            "s": "9",
            "w": "2"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "30": {
        "coordinates": "(62,63)",
        "elevation": 0,
        "exits": {
            "e": "32",
            "s": "31",
            "w": "27"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "301": {
        "coordinates": "(55,58)",
        "elevation": 0,
        "exits": {
            "n": "304",
            "s": "292"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "302": {
        "coordinates": "(55,70)",
        "elevation": 0,
        "exits": {
            "n": "422",
            "s": "284"
        },
        "terrain": "TRAP",
        "title": "A Dark Cave"
    },
    "303": {
        "coordinates": "(54,69)",
        "elevation": 0,
        "exits": {
            "e": "284",
            "n": "361",
            "w": "405"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "304": {
        "coordinates": "(55,59)",
        "elevation": 0,
        "exits": {
            "s": "301"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "305": {
        "coordinates": "(54,58)",
        "elevation": 0,
        "exits": {
            "n": "?",
            "s": "222"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "306": {
        "coordinates": "(70,58)",
        "elevation": 0,
        "exits": {
            "e": "397",
            "w": "258"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "307": {
        "coordinates": "(63,49)",
        "elevation": 0,
        "exits": {
            "e": "371",
            "n": "230",
            "s": "373",
            "w": "321"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "309": {
        "coordinates": "(60,49)",
        "elevation": 0,
        "exits": {
            "e": "326",
            "s": "333",
            "w": "281"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "31": {
        "coordinates": "(62,62)",
        "elevation": 0,
        "exits": {
            "e": "33",
            "n": "30"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "310": {
        "coordinates": "(53,66)",
        "elevation": 0,
        "exits": {
            "e": "259",
            "w": "412"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "311": {
        "coordinates": "(60,68)",
        "elevation": 0,
        "exits": {
            "w": "299"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "312": {
        "coordinates": "(57,69)",
        "elevation": 0,
        "exits": {
            "e": "268",
            "n": "328"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "313": {
        "coordinates": "(68,67)",
        "elevation": 0,
        "exits": {
            "w": "283"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "314": {
        "coordinates": "(55,65)",
        "elevation": 0,
        "exits": {
            "e": "254"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "315": {
        "coordinates": "(69,55)",
        "elevation": 0,
        "exits": {
            "w": "251"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "316": {
        "coordinates": "(66,68)",
        "elevation": 0,
        "exits": {
            "n": "344",
            "w": "155"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "318": {
        "coordinates": "(59,48)",
        "elevation": 0,
        "exits": {
            "n": "281",
            "s": "487"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "319": {
        "coordinates": "(63,73)",
        "elevation": 0,
        "exits": {
            "e": "345",
            "n": "359",
            "s": "269"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "32": {
        "coordinates": "(63,63)",
        "elevation": 0,
        "exits": {
            "e": "54",
            "n": "39",
            "w": "30"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "320": {
        "coordinates": "(53,64)",
        "elevation": 0,
        "exits": {
            "n": "348",
            "s": "257"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "321": {
        "coordinates": "(62,49)",
        "elevation": 0,
        "exits": {
            "e": "307",
            "s": "413"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "322": {
        "coordinates": "(70,54)",
        "elevation": 0,
        "exits": {
            "e": "435",
            "n": "382",
            "w": "261"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "323": {
        "coordinates": "(70,53)",
        "elevation": 0,
        "exits": {
            "e": "433",
            "w": "277"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "324": {
        "coordinates": "(68,52)",
        "elevation": 0,
        "exits": {
            "e": "354",
            "n": "298",
            "s": "349"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "325": {
        "coordinates": "(59,71)",
        "elevation": 0,
        "exits": {
            "n": "353",
            "s": "280",
            "w": "374"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "326": {
        "coordinates": "(61,49)",
        "elevation": 0,
        "exits": {
            "s": "342",
            "w": "309"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "327": {
        "coordinates": "(70,57)",
        "elevation": 0,
        "exits": {
            "e": "427",
            "w": "256"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "328": {
        "coordinates": "(57,70)",
        "elevation": 0,
        "exits": {
            "e": "357",
            "n": "332",
            "s": "312",
            "w": "363"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "329": {
        "coordinates": "(65,69)",
        "elevation": 0,
        "exits": {
            "w": "153"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "33": {
        "coordinates": "(63,62)",
        "elevation": 0,
        "exits": {
            "e": "38",
            "w": "31"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "331": {
        "coordinates": "(67,68)",
        "elevation": 0,
        "exits": {
            "e": "446",
            "s": "283"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "332": {
        "coordinates": "(57,71)",
        "elevation": 0,
        "exits": {
            "n": "350",
            "s": "328"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "333": {
        "coordinates": "(60,48)",
        "elevation": 0,
        "exits": {
            "n": "309",
            "s": "378"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "334": {
        "coordinates": "(55,50)",
        "elevation": 0,
        "exits": {
            "e": "?",
            "n": "294",
            "s": "?",
            "w": "?"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "335": {
        "coordinates": "(54,60)",
        "elevation": 0,
        "exits": {
            "e": "188",
            "w": "366"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "336": {
        "coordinates": "(62,74)",
        "elevation": 0,
        "exits": {
            "s": "286"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "337": {
        "coordinates": "(61,72)",
        "elevation": 0,
        "exits": {
            "s": "271"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "338": {
        "coordinates": "(71,61)",
        "elevation": 0,
        "exits": {
            "s": "379",
            "w": "270"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "339": {
        "coordinates": "(53,68)",
        "elevation": 0,
        "exits": {
            "e": "287",
            "w": "445"
        },
        "terrain": "TRAP",
        "title": "A Dark Cave"
    },
    "34": {
        "coordinates": "(62,56)",
        "elevation": 1,
        "exits": {
            "e": "35",
            "n": "14",
            "s": "50"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "340": {
        "coordinates": "(67,52)",
        "elevation": 0,
        "exits": {
            "w": "168"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "342": {
        "coordinates": "(61,48)",
        "elevation": 0,
        "exits": {
            "n": "326",
            "s": "?"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "344": {
        "coordinates": "(66,69)",
        "elevation": 0,
        "exits": {
            "e": "390",
            "n": "392",
            "s": "316"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "345": {
        "coordinates": "(64,73)",
        "elevation": 0,
        "exits": {
            "s": "375",
            "w": "319"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "346": {
        "coordinates": "(53,62)",
        "elevation": 0,
        "exits": {
            "e": "177"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "347": {
        "coordinates": "(60,73)",
        "elevation": 0,
        "exits": {
            "e": "291",
            "n": "452",
            "s": "442"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "348": {
        "coordinates": "(53,65)",
        "elevation": 0,
        "exits": {
            "s": "320"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "349": {
        "coordinates": "(68,51)",
        "elevation": 0,
        "exits": {
            "e": "384",
            "n": "324",
            "s": "352",
            "w": "356"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "35": {
        "coordinates": "(63,56)",
        "elevation": 0,
        "exits": {
            "s": "52",
            "w": "34"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "350": {
        "coordinates": "(57,72)",
        "elevation": 0,
        "exits": {
            "e": "404",
            "n": "436",
            "s": "332"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "352": {
        "coordinates": "(68,50)",
        "elevation": 0,
        "exits": {
            "e": "485",
            "n": "349",
            "s": "362"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "353": {
        "coordinates": "(59,72)",
        "elevation": 0,
        "exits": {
            "s": "325"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "354": {
        "coordinates": "(69,52)",
        "elevation": 0,
        "exits": {
            "w": "324"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "356": {
        "coordinates": "(67,51)",
        "elevation": 0,
        "exits": {
            "e": "349"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "357": {
        "coordinates": "(58,70)",
        "elevation": 0,
        "exits": {
            "w": "328"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "358": {
        "coordinates": "(66,50)",
        "elevation": 0,
        "exits": {
            "e": "401",
            "w": "262"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "359": {
        "coordinates": "(63,74)",
        "elevation": 0,
        "exits": {
            "s": "319"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "36": {
        "coordinates": "(60,55)",
        "elevation": 4,
        "exits": {
            "e": "22",
            "s": "48",
            "w": "60"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "360": {
        "coordinates": "(69,56)",
        "elevation": 0,
        "exits": {
            "e": "398",
            "n": "256"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "361": {
        "coordinates": "(54,70)",
        "elevation": 0,
        "exits": {
            "n": "408",
            "s": "303"
        },
        "terrain": "TRAP",
        "title": "A Dark Cave"
    },
    "362": {
        "coordinates": "(68,49)",
        "elevation": 0,
        "exits": {
            "n": "352",
            "s": "399",
            "w": "463"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "363": {
        "coordinates": "(56,70)",
        "elevation": 0,
        "exits": {
            "e": "328",
            "n": "372"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "364": {
        "coordinates": "(52,63)",
        "elevation": 0,
        "exits": {
            "e": "257",
            "n": "429",
            "s": "381",
            "w": "448"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "366": {
        "coordinates": "(53,60)",
        "elevation": 0,
        "exits": {
            "e": "335"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "367": {
        "coordinates": "(64,51)",
        "elevation": 0,
        "exits": {
            "n": "111"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "368": {
        "coordinates": "(56,69)",
        "elevation": 0,
        "exits": {
            "s": "234"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "37": {
        "coordinates": "(63,57)",
        "elevation": 1,
        "exits": {
            "w": "14"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "370": {
        "coordinates": "(65,49)",
        "elevation": 0,
        "exits": {
            "e": "407",
            "n": "262",
            "s": "434"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "371": {
        "coordinates": "(64,49)",
        "elevation": 0,
        "exits": {
            "s": "475",
            "w": "307"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "372": {
        "coordinates": "(56,71)",
        "elevation": 0,
        "exits": {
            "n": "441",
            "s": "363"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "373": {
        "coordinates": "(63,48)",
        "elevation": 0,
        "exits": {
            "n": "307",
            "s": "480"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "374": {
        "coordinates": "(58,71)",
        "elevation": 0,
        "exits": {
            "e": "325"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "375": {
        "coordinates": "(64,72)",
        "elevation": 0,
        "exits": {
            "e": "385",
            "n": "345"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "378": {
        "coordinates": "(60,47)",
        "elevation": 0,
        "exits": {
            "n": "333"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "379": {
        "coordinates": "(71,60)",
        "elevation": 0,
        "exits": {
            "e": "395",
            "n": "338"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "38": {
        "coordinates": "(64,62)",
        "elevation": 0,
        "exits": {
            "e": "66",
            "s": "59",
            "w": "33"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "380": {
        "coordinates": "(65,70)",
        "elevation": 0,
        "exits": {
            "n": "424",
            "w": "206"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "381": {
        "coordinates": "(52,62)",
        "elevation": 0,
        "exits": {
            "n": "364",
            "w": "394"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "382": {
        "coordinates": "(70,55)",
        "elevation": 0,
        "exits": {
            "e": "388",
            "s": "322"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "384": {
        "coordinates": "(69,51)",
        "elevation": 0,
        "exits": {
            "w": "349"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "385": {
        "coordinates": "(65,72)",
        "elevation": 0,
        "exits": {
            "w": "375"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "386": {
        "coordinates": "(70,59)",
        "elevation": 0,
        "exits": {
            "e": "414",
            "w": "240"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "388": {
        "coordinates": "(71,55)",
        "elevation": 0,
        "exits": {
            "e": "477",
            "w": "382"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "39": {
        "coordinates": "(63,64)",
        "elevation": 0,
        "exits": {
            "e": "51",
            "n": "53",
            "s": "32",
            "w": "41"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "390": {
        "coordinates": "(67,69)",
        "elevation": 0,
        "exits": {
            "w": "344"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "392": {
        "coordinates": "(66,70)",
        "elevation": 0,
        "exits": {
            "e": "462",
            "s": "344"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "394": {
        "coordinates": "(51,62)",
        "elevation": 0,
        "exits": {
            "e": "381"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "395": {
        "coordinates": "(72,60)",
        "elevation": 0,
        "exits": {
            "e": "421",
            "s": "403",
            "w": "379"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "397": {
        "coordinates": "(71,58)",
        "elevation": 0,
        "exits": {
            "w": "306"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "398": {
        "coordinates": "(70,56)",
        "elevation": 0,
        "exits": {
            "e": "438",
            "w": "360"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "399": {
        "coordinates": "(68,48)",
        "elevation": 0,
        "exits": {
            "n": "362",
            "s": "467"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "4": {
        "coordinates": "(61,60)",
        "elevation": 0,
        "exits": {
            "e": "13",
            "n": "23",
            "w": "0"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "40": {
        "coordinates": "(61,64)",
        "elevation": 0,
        "exits": {
            "s": "27"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "401": {
        "coordinates": "(67,50)",
        "elevation": 0,
        "exits": {
            "w": "358"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "402": {
        "coordinates": "(53,61)",
        "elevation": 0,
        "exits": {
            "e": "176",
            "w": "451"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "403": {
        "coordinates": "(72,59)",
        "elevation": 0,
        "exits": {
            "n": "395"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "404": {
        "coordinates": "(58,72)",
        "elevation": 0,
        "exits": {
            "n": "481",
            "w": "350"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "405": {
        "coordinates": "(53,69)",
        "elevation": 0,
        "exits": {
            "e": "303",
            "n": "406"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "406": {
        "coordinates": "(53,70)",
        "elevation": 0,
        "exits": {
            "s": "405",
            "w": "415"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "407": {
        "coordinates": "(66,49)",
        "elevation": 0,
        "exits": {
            "s": "496",
            "w": "370"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "408": {
        "coordinates": "(54,71)",
        "elevation": 0,
        "exits": {
            "n": "458",
            "s": "361",
            "w": "423"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "41": {
        "coordinates": "(62,64)",
        "elevation": 0,
        "exits": {
            "e": "39"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "410": {
        "coordinates": "(61,74)",
        "elevation": 0,
        "exits": {
            "s": "291"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "411": {
        "coordinates": "(59,69)",
        "elevation": 0,
        "exits": {
            "w": "268"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "412": {
        "coordinates": "(52,66)",
        "elevation": 0,
        "exits": {
            "e": "310",
            "s": "488"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "413": {
        "coordinates": "(62,48)",
        "elevation": 0,
        "exits": {
            "n": "321"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "414": {
        "coordinates": "(71,59)",
        "elevation": 0,
        "exits": {
            "w": "386"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "415": {
        "coordinates": "(52,70)",
        "elevation": 0,
        "exits": {
            "e": "406",
            "w": "418"
        },
        "terrain": "TRAP",
        "title": "A Dark Cave"
    },
    "416": {
        "coordinates": "(70,62)",
        "elevation": 0,
        "exits": {
            "s": "270"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "418": {
        "coordinates": "(51,70)",
        "elevation": 0,
        "exits": {
            "e": "415",
            "n": "425",
            "s": "474"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "42": {
        "coordinates": "(64,58)",
        "elevation": 0,
        "exits": {
            "e": "118",
            "n": "44",
            "s": "80",
            "w": "17"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "421": {
        "coordinates": "(73,60)",
        "elevation": 0,
        "exits": {
            "n": "440",
            "w": "395"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "422": {
        "coordinates": "(55,71)",
        "elevation": 0,
        "exits": {
            "n": "426",
            "s": "302"
        },
        "terrain": "TRAP",
        "title": "A Dark Cave"
    },
    "423": {
        "coordinates": "(53,71)",
        "elevation": 0,
        "exits": {
            "e": "408",
            "w": "454"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "424": {
        "coordinates": "(65,71)",
        "elevation": 0,
        "exits": {
            "e": "473",
            "s": "380"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "425": {
        "coordinates": "(51,71)",
        "elevation": 0,
        "exits": {
            "s": "418",
            "w": "469"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "426": {
        "coordinates": "(55,72)",
        "elevation": 0,
        "exits": {
            "n": "457",
            "s": "422"
        },
        "terrain": "TRAP",
        "title": "A Dark Cave"
    },
    "427": {
        "coordinates": "(71,57)",
        "elevation": 0,
        "exits": {
            "e": "430",
            "w": "327"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "429": {
        "coordinates": "(52,64)",
        "elevation": 0,
        "exits": {
            "s": "364"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "43": {
        "coordinates": "(59,61)",
        "elevation": 0,
        "exits": {
            "e": "10",
            "w": "47"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "430": {
        "coordinates": "(72,57)",
        "elevation": 0,
        "exits": {
            "e": "439",
            "n": "443",
            "w": "427"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "433": {
        "coordinates": "(71,53)",
        "elevation": 0,
        "exits": {
            "e": "460",
            "s": "455",
            "w": "323"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "434": {
        "coordinates": "(65,48)",
        "elevation": 0,
        "exits": {
            "n": "370"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "435": {
        "coordinates": "(71,54)",
        "elevation": 0,
        "exits": {
            "w": "322"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "436": {
        "coordinates": "(57,73)",
        "elevation": 0,
        "exits": {
            "s": "350"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "438": {
        "coordinates": "(71,56)",
        "elevation": 0,
        "exits": {
            "e": "465",
            "w": "398"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "439": {
        "coordinates": "(73,57)",
        "elevation": 0,
        "exits": {
            "w": "430"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "44": {
        "coordinates": "(64,59)",
        "elevation": 0,
        "exits": {
            "s": "42"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "440": {
        "coordinates": "(73,61)",
        "elevation": 0,
        "exits": {
            "s": "421",
            "w": "476"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "441": {
        "coordinates": "(56,72)",
        "elevation": 0,
        "exits": {
            "s": "372"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "442": {
        "coordinates": "(60,72)",
        "elevation": 0,
        "exits": {
            "n": "347"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "443": {
        "coordinates": "(72,58)",
        "elevation": 0,
        "exits": {
            "e": "471",
            "s": "430"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "445": {
        "coordinates": "(52,68)",
        "elevation": 0,
        "exits": {
            "e": "339",
            "n": "447",
            "w": "450"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "446": {
        "coordinates": "(68,68)",
        "elevation": 0,
        "exits": {
            "e": "466",
            "w": "331"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "447": {
        "coordinates": "(52,69)",
        "elevation": 0,
        "exits": {
            "s": "445"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "448": {
        "coordinates": "(51,63)",
        "elevation": 0,
        "exits": {
            "e": "364"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "45": {
        "coordinates": "(59,56)",
        "elevation": 2,
        "exits": {
            "n": "29",
            "s": "60"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "450": {
        "coordinates": "(51,68)",
        "elevation": 0,
        "exits": {
            "e": "445"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "451": {
        "coordinates": "(52,61)",
        "elevation": 0,
        "exits": {
            "e": "402",
            "w": "453"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "452": {
        "coordinates": "(60,74)",
        "elevation": 0,
        "exits": {
            "s": "347"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "453": {
        "coordinates": "(51,61)",
        "elevation": 0,
        "exits": {
            "e": "451",
            "s": "464"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "454": {
        "coordinates": "(52,71)",
        "elevation": 0,
        "exits": {
            "e": "423",
            "n": "470"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "455": {
        "coordinates": "(71,52)",
        "elevation": 0,
        "exits": {
            "n": "433"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "456": {
        "coordinates": "(52,67)",
        "elevation": 0,
        "exits": {
            "e": "275",
            "w": "499"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "457": {
        "coordinates": "(55,73)",
        "elevation": 0,
        "exits": {
            "n": "461",
            "s": "426"
        },
        "terrain": "TRAP",
        "title": "A Dark Cave"
    },
    "458": {
        "coordinates": "(54,72)",
        "elevation": 0,
        "exits": {
            "s": "408",
            "w": "459"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "459": {
        "coordinates": "(53,72)",
        "elevation": 0,
        "exits": {
            "e": "458"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "46": {
        "coordinates": "(59,63)",
        "elevation": 0,
        "exits": {
            "e": "20",
            "w": "62"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "460": {
        "coordinates": "(72,53)",
        "elevation": 0,
        "exits": {
            "w": "433"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "461": {
        "coordinates": "(55,74)",
        "elevation": 0,
        "exits": {
            "s": "457"
        },
        "terrain": "CAVE",
        "title": "Linh's Shrine"
    },
    "462": {
        "coordinates": "(67,70)",
        "elevation": 0,
        "exits": {
            "w": "392"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "463": {
        "coordinates": "(67,49)",
        "elevation": 0,
        "exits": {
            "e": "362",
            "s": "468"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "464": {
        "coordinates": "(51,60)",
        "elevation": 0,
        "exits": {
            "n": "453"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "465": {
        "coordinates": "(72,56)",
        "elevation": 0,
        "exits": {
            "e": "498",
            "w": "438"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "466": {
        "coordinates": "(69,68)",
        "elevation": 0,
        "exits": {
            "e": "472",
            "s": "486",
            "w": "446"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "467": {
        "coordinates": "(68,47)",
        "elevation": 0,
        "exits": {
            "n": "399"
        },
        "terrain": "NORMAL",
        "title": "Pirate Ry's"
    },
    "468": {
        "coordinates": "(67,48)",
        "elevation": 0,
        "exits": {
            "n": "463"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "469": {
        "coordinates": "(50,71)",
        "elevation": 0,
        "exits": {
            "e": "425"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "47": {
        "coordinates": "(58,61)",
        "elevation": 0,
        "exits": {
            "e": "43",
            "n": "71"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "470": {
        "coordinates": "(52,72)",
        "elevation": 0,
        "exits": {
            "s": "454"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "471": {
        "coordinates": "(73,58)",
        "elevation": 0,
        "exits": {
            "w": "443"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "472": {
        "coordinates": "(70,68)",
        "elevation": 0,
        "exits": {
            "w": "466"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "473": {
        "coordinates": "(66,71)",
        "elevation": 0,
        "exits": {
            "e": "494",
            "w": "424"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "474": {
        "coordinates": "(51,69)",
        "elevation": 0,
        "exits": {
            "n": "418"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "475": {
        "coordinates": "(64,48)",
        "elevation": 0,
        "exits": {
            "n": "371",
            "s": "484"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "476": {
        "coordinates": "(72,61)",
        "elevation": 0,
        "exits": {
            "e": "440"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "477": {
        "coordinates": "(72,55)",
        "elevation": 0,
        "exits": {
            "e": "483",
            "w": "388"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "479": {
        "coordinates": "(68,63)",
        "elevation": 0,
        "exits": {
            "w": "205"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "48": {
        "coordinates": "(60,54)",
        "elevation": 3,
        "exits": {
            "n": "36",
            "s": "105",
            "w": "149"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "480": {
        "coordinates": "(63,47)",
        "elevation": 0,
        "exits": {
            "n": "373"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "481": {
        "coordinates": "(58,73)",
        "elevation": 0,
        "exits": {
            "s": "404"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "483": {
        "coordinates": "(73,55)",
        "elevation": 0,
        "exits": {
            "w": "477"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "484": {
        "coordinates": "(64,47)",
        "elevation": 0,
        "exits": {
            "n": "475"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "485": {
        "coordinates": "(69,50)",
        "elevation": 0,
        "exits": {
            "w": "352"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "486": {
        "coordinates": "(69,67)",
        "elevation": 0,
        "exits": {
            "n": "466"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "487": {
        "coordinates": "(59,47)",
        "elevation": 0,
        "exits": {
            "n": "318",
            "s": "489"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "488": {
        "coordinates": "(52,65)",
        "elevation": 0,
        "exits": {
            "n": "412"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "489": {
        "coordinates": "(59,46)",
        "elevation": 0,
        "exits": {
            "n": "487"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "49": {
        "coordinates": "(58,57)",
        "elevation": 0,
        "exits": {
            "e": "29",
            "s": "79",
            "w": "136"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "494": {
        "coordinates": "(67,71)",
        "elevation": 0,
        "exits": {
            "w": "473"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "496": {
        "coordinates": "(66,48)",
        "elevation": 0,
        "exits": {
            "n": "407"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "498": {
        "coordinates": "(73,56)",
        "elevation": 0,
        "exits": {
            "w": "465"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "499": {
        "coordinates": "(51,67)",
        "elevation": 0,
        "exits": {
            "e": "456"
        },
        "terrain": "CAVE",
        "title": "A Dark Cave"
    },
    "5": {
        "coordinates": "(62,59)",
        "elevation": 0,
        "exits": {
            "w": "3"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "50": {
        "coordinates": "(62,55)",
        "elevation": 0,
        "exits": {
            "n": "34",
            "s": "89"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "51": {
        "coordinates": "(64,64)",
        "elevation": 0,
        "exits": {
            "e": "57",
            "n": "69",
            "w": "39"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "52": {
        "coordinates": "(63,55)",
        "elevation": 0,
        "exits": {
            "e": "75",
            "n": "35",
            "s": "68"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "53": {
        "coordinates": "(63,65)",
        "elevation": 0,
        "exits": {
            "n": "95",
            "s": "39",
            "w": "88"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "54": {
        "coordinates": "(64,63)",
        "elevation": 0,
        "exits": {
            "w": "32"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "55": {
        "coordinates": "(63,61)",
        "elevation": 0,
        "exits": {
            "w": "26"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "56": {
        "coordinates": "(58,58)",
        "elevation": 0,
        "exits": {
            "e": "7",
            "w": "61"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "57": {
        "coordinates": "(65,64)",
        "elevation": 0,
        "exits": {
            "e": "145",
            "w": "51"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "58": {
        "coordinates": "(58,60)",
        "elevation": 0,
        "exits": {
            "s": "16",
            "w": "65"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "59": {
        "coordinates": "(64,61)",
        "elevation": 0,
        "exits": {
            "e": "92",
            "n": "38",
            "s": "104"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "6": {
        "coordinates": "(60,58)",
        "elevation": 0,
        "exits": {
            "n": "2",
            "w": "7"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "60": {
        "coordinates": "(59,55)",
        "elevation": 3,
        "exits": {
            "e": "36",
            "n": "45",
            "w": "70"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "61": {
        "coordinates": "(57,58)",
        "elevation": 0,
        "exits": {
            "e": "56",
            "w": "171"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "62": {
        "coordinates": "(58,63)",
        "elevation": 0,
        "exits": {
            "e": "46",
            "n": "64",
            "w": "84"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "63": {
        "coordinates": "(60,64)",
        "elevation": 0,
        "exits": {
            "n": "72",
            "s": "20",
            "w": "73"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "64": {
        "coordinates": "(58,64)",
        "elevation": 0,
        "exits": {
            "s": "62",
            "w": "82"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "65": {
        "coordinates": "(57,60)",
        "elevation": 0,
        "exits": {
            "e": "58",
            "n": "74",
            "w": "139"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "66": {
        "coordinates": "(65,62)",
        "elevation": 0,
        "exits": {
            "e": "123",
            "n": "169",
            "w": "38"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "67": {
        "coordinates": "(57,59)",
        "elevation": 0,
        "exits": {
            "e": "16",
            "w": "162"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "68": {
        "coordinates": "(63,54)",
        "elevation": 0,
        "exits": {
            "e": "100",
            "n": "52"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "69": {
        "coordinates": "(64,65)",
        "elevation": 0,
        "exits": {
            "e": "103",
            "n": "94",
            "s": "51"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "7": {
        "coordinates": "(59,58)",
        "elevation": 0,
        "exits": {
            "e": "6",
            "n": "8",
            "w": "56"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "70": {
        "coordinates": "(58,55)",
        "elevation": 2,
        "exits": {
            "e": "60",
            "s": "163",
            "w": "98"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "71": {
        "coordinates": "(58,62)",
        "elevation": 0,
        "exits": {
            "s": "47"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "72": {
        "coordinates": "(60,65)",
        "elevation": 0,
        "exits": {
            "s": "63",
            "w": "76"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "73": {
        "coordinates": "(59,64)",
        "elevation": 0,
        "exits": {
            "e": "63"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "74": {
        "coordinates": "(57,61)",
        "elevation": 0,
        "exits": {
            "n": "87",
            "s": "65",
            "w": "161"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "75": {
        "coordinates": "(64,55)",
        "elevation": 0,
        "exits": {
            "e": "85",
            "w": "52"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "76": {
        "coordinates": "(59,65)",
        "elevation": 0,
        "exits": {
            "e": "72",
            "n": "83",
            "w": "110"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "77": {
        "coordinates": "(59,62)",
        "elevation": 0,
        "exits": {
            "e": "19"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "78": {
        "coordinates": "(61,54)",
        "elevation": 4,
        "exits": {
            "n": "22",
            "s": "108"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "79": {
        "coordinates": "(58,56)",
        "elevation": 0,
        "exits": {
            "n": "49"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "8": {
        "coordinates": "(59,59)",
        "elevation": 0,
        "exits": {
            "s": "7",
            "w": "16"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "80": {
        "coordinates": "(64,57)",
        "elevation": 0,
        "exits": {
            "e": "86",
            "n": "42",
            "s": "81"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "81": {
        "coordinates": "(64,56)",
        "elevation": 0,
        "exits": {
            "n": "80"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "82": {
        "coordinates": "(57,64)",
        "elevation": 0,
        "exits": {
            "e": "64",
            "n": "191"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "83": {
        "coordinates": "(59,66)",
        "elevation": 0,
        "exits": {
            "e": "130",
            "s": "76",
            "w": "125"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "84": {
        "coordinates": "(57,63)",
        "elevation": 0,
        "exits": {
            "e": "62",
            "w": "91"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "85": {
        "coordinates": "(65,55)",
        "elevation": 0,
        "exits": {
            "e": "154",
            "w": "75"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "86": {
        "coordinates": "(65,57)",
        "elevation": 0,
        "exits": {
            "e": "90",
            "s": "96",
            "w": "80"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "87": {
        "coordinates": "(57,62)",
        "elevation": 0,
        "exits": {
            "s": "74"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "88": {
        "coordinates": "(62,65)",
        "elevation": 0,
        "exits": {
            "e": "53",
            "w": "122"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "89": {
        "coordinates": "(62,54)",
        "elevation": 1,
        "exits": {
            "n": "50",
            "s": "93"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "9": {
        "coordinates": "(61,58)",
        "elevation": 2,
        "exits": {
            "e": "11",
            "n": "3",
            "s": "12"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "90": {
        "coordinates": "(66,57)",
        "elevation": 0,
        "exits": {
            "e": "178",
            "w": "86"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "91": {
        "coordinates": "(56,63)",
        "elevation": 0,
        "exits": {
            "e": "84",
            "n": "180",
            "s": "101",
            "w": "99"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "92": {
        "coordinates": "(65,61)",
        "elevation": 0,
        "exits": {
            "w": "59"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "93": {
        "coordinates": "(62,53)",
        "elevation": 2,
        "exits": {
            "n": "89",
            "w": "108"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "94": {
        "coordinates": "(64,66)",
        "elevation": 0,
        "exits": {
            "n": "152",
            "s": "69"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "95": {
        "coordinates": "(63,66)",
        "elevation": 0,
        "exits": {
            "n": "119",
            "s": "53",
            "w": "115"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "96": {
        "coordinates": "(65,56)",
        "elevation": 0,
        "exits": {
            "e": "97",
            "n": "86"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "97": {
        "coordinates": "(66,56)",
        "elevation": 0,
        "exits": {
            "e": "181",
            "w": "96"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    },
    "98": {
        "coordinates": "(57,55)",
        "elevation": 1,
        "exits": {
            "e": "70",
            "n": "102",
            "s": "126",
            "w": "109"
        },
        "terrain": "MOUNTAIN",
        "title": "Mt. Holloway"
    },
    "99": {
        "coordinates": "(55,63)",
        "elevation": 0,
        "exits": {
            "e": "91",
            "n": "190",
            "w": "146"
        },
        "terrain": "NORMAL",
        "title": "A misty room"
    }
}

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = graph
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if not vertex in self.vertices:
            self.vertices[vertex] = set()
        else:
            print('Warning: Vertex already exists')
        
    def add_edge(self, vertex_from, vertex_to):
        """
        Add a directed edge to the graph.
        """

        if vertex_from in self.vertices and vertex_to in self.vertices:
            self.vertices[vertex_from].add(vertex_to)
        else:
            print('Warning: supplied vertex does not exist')

        # TODO -confirm intent that edges should have direciton from v1->v2
        
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        found = [starting_vertex, ]

        while q.size() > 0:
            for vertex in self.vertices[q.queue[0]]:
                if vertex not in found:
                    q.enqueue(vertex)
                    found.append(vertex)
            q.dequeue()
        
        print(f'BFT: {found}')

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        found = []

        while s.size() > 0:
            current = s.pop()

            if current not in found:
                found.append(current)
                for next_vert in self.vertices[current]:
                    s.push(next_vert)
        
        print(f'DFT: {found}')

    def dft_recursive(self, starting_vertex, visited=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        visited.append(starting_vertex)
        # print(starting_vertex)
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)
        
        return visited

    def bfs(self, graph, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        # """
        # print(f'{starting_vertex}')
        q = Queue()
        q.enqueue([starting_vertex])

        found = []

        while q.size() > 0:
            path = q.dequeue()
            # print(f'path is {path}')
            v = path[-1]
            # print(f'v is {v}')

            if v not in found:
                if v == f'{destination_vertex}':
                    break
                    # return path
                found.append(v)
                # print( f'found is {found}')
                for next_vert in graph[str(v)]["exits"]:
                    new_path = list(path)
                    new_path.append(graph[str(v)]["exits"][next_vert])
                    q.enqueue(new_path)

        # print(f'BFS: {path}')

        steps = []

        for i in range(0, len(path) - 1):
            for direction, to in graph[str(path[i])]["exits"].items():
                # print(f'direction: {direction} to: {to}')
                if to == path[i + 1]:
                    steps.append(direction)
            path = path + steps
        
        print (f'steps are {steps}')
        return steps

    def dfs(self, graph, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        found = []

        while s.size() > 0:
            path = s.pop()
            v = path[-1]

            if v not in found:
                if v == destination_vertex:
                    return path
                found.append(v)
                for next_vert in graph[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)

        print(f'BFS: {found}')
        return None





if __name__ == '__main__':
    # graph = Graph()  # Instantiate your graph
    # # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    # graph.add_vertex(1)
    # graph.add_vertex(2)
    # graph.add_vertex(3)
    # graph.add_vertex(4)
    # graph.add_vertex(5)
    # graph.add_vertex(6)
    # graph.add_vertex(7)
    # graph.add_edge(5, 3)
    # graph.add_edge(6, 3)
    # graph.add_edge(7, 1)
    # graph.add_edge(4, 7)
    # graph.add_edge(1, 2)
    # graph.add_edge(7, 6)
    # graph.add_edge(2, 4)
    # graph.add_edge(3, 5)
    # graph.add_edge(2, 3)
    # graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print(f'Recursive: {graph.dft_recursive(1)}')

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    newGraph = Graph()

    def fn(grf):
        for x in range(500):
            try:
                newGraph.bfs(grf, x, 183)
                print(f'coming from {x}')
            except:
                pass

    print(newGraph.bfs(graph, 229, 250))
    # print(fn(graph))
    # 229

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))

    
