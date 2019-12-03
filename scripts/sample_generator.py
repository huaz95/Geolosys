"""
    Author: Jose Stovall
    Geolosys: https://github.com/oitsjustjose/Geolosys
"""
import json
import sys

from pip._vendor.colorama import Fore


def get_model(variant: str) -> dict:
    """Generates the sample model from the given variant string"""
    return {
        "source": "[120,-38,99,98,22,-56,-51,-52,75,77,46,74,76,43,81,53,118,76,-52,44,-78,103,-112,71,22,41,46,-55,-49,75,-75,47,75,44,-54,76,-52,43,-79,5,-13,24,20,113,43,72,-55,-52,47,-54,44,73,101,104,96,108,97,101,96,80,96,24,88,-32,64,-111,110,38,-42,41,12,12,-116,20,-104,33,-75,68,-127,-127,109,2,-7,102,72,45,97,96,96,3,98,-42,0,-14,-12,103,45,-127,-104,65,-111,126,-96,-5,89,-55,116,-65,24,5,122,65,-128,-111,-62,-8,99,-32,96,0,0,-81,-58,42,32]",
        "textures": {"particle": "minecraft:block/gravel", "ore": "geolosys:blocks/{}".format(variant),
                     "stone": "minecraft:block/gravel"}, "elements": [{"from": [7, 0, 4], "to": [8, 0, 5], "faces": {
            "down": {"uv": [7, 12, 8, 11], "texture": "#ore", "cullface": "down"}}},
                                                                      {"from": [5, 0, 5], "to": [7, 0, 6], "faces": {
                                                                          "down": {"uv": [5, 11, 7, 10],
                                                                                   "texture": "#ore",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [8, 0, 5], "to": [10, 0, 6], "faces": {
                                                                          "down": {"uv": [8, 11, 10, 10],
                                                                                   "texture": "#ore",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [5, 0, 6], "to": [6, 0, 10], "faces": {
                                                                          "down": {"uv": [5, 10, 6, 6],
                                                                                   "texture": "#ore",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [10, 0, 6], "to": [11, 0, 8], "faces": {
                                                                          "down": {"uv": [10, 10, 11, 8],
                                                                                   "texture": "#ore",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [9, 0, 10], "to": [11, 0, 11], "faces": {
                                                                          "down": {"uv": [9, 6, 11, 5],
                                                                                   "texture": "#ore",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [11, 0, 8], "to": [12, 0, 10], "faces": {
                                                                          "down": {"uv": [11, 8, 12, 6],
                                                                                   "texture": "#ore",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [7, 0, 11], "to": [9, 0, 12], "faces": {
                                                                          "down": {"uv": [7, 5, 9, 4],
                                                                                   "texture": "#ore",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [6, 0, 10], "to": [7, 0, 11], "faces": {
                                                                          "down": {"uv": [6, 6, 7, 5],
                                                                                   "texture": "#ore",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [8, 0, 4], "to": [8, 1, 5], "faces": {
                                                                          "east": {"uv": [12, 16, 11, 15],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [9, 1, 5], "to": [9, 2, 6], "faces": {
                                                                          "east": {"uv": [11, 15, 10, 14],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [9, 2, 6], "to": [9, 3, 7], "faces": {
                                                                          "east": {"uv": [10, 14, 9, 13],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [9, 0, 11], "to": [9, 1, 12], "faces": {
                                                                          "east": {"uv": [5, 16, 4, 15],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [10, 0, 5], "to": [10, 1, 6], "faces": {
                                                                          "east": {"uv": [11, 16, 10, 15],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [10, 1, 6], "to": [10, 2, 7], "faces": {
                                                                          "east": {"uv": [10, 15, 9, 14],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [10, 1, 7], "to": [10, 3, 8], "faces": {
                                                                          "east": {"uv": [9, 15, 8, 13],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [10, 2, 8], "to": [10, 3, 10], "faces": {
                                                                          "east": {"uv": [8, 14, 6, 13],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [10, 1, 10], "to": [10, 2, 11],
                                                                       "faces": {"east": {"uv": [6, 15, 5, 14],
                                                                                          "texture": "#ore"}}},
                                                                      {"from": [11, 0, 6], "to": [11, 1, 8], "faces": {
                                                                          "east": {"uv": [10, 16, 8, 15],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [11, 0, 10], "to": [11, 1, 11],
                                                                       "faces": {"east": {"uv": [6, 16, 5, 15],
                                                                                          "texture": "#ore"}}},
                                                                      {"from": [11, 1, 8], "to": [11, 2, 10], "faces": {
                                                                          "east": {"uv": [8, 15, 6, 14],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [12, 0, 8], "to": [12, 1, 10], "faces": {
                                                                          "east": {"uv": [8, 16, 6, 15],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [5, 0, 5], "to": [5, 1, 7], "faces": {
                                                                          "west": {"uv": [5, 16, 7, 15],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [5, 0, 7], "to": [5, 2, 9], "faces": {
                                                                          "west": {"uv": [7, 16, 9, 14],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [5, 0, 9], "to": [5, 1, 10], "faces": {
                                                                          "west": {"uv": [9, 16, 10, 15],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [6, 1, 6], "to": [6, 2, 7], "faces": {
                                                                          "west": {"uv": [6, 15, 7, 14],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [6, 2, 7], "to": [6, 3, 9], "faces": {
                                                                          "west": {"uv": [7, 14, 9, 13],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [6, 0, 10], "to": [6, 1, 11], "faces": {
                                                                          "west": {"uv": [10, 16, 11, 15],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [6, 1, 9], "to": [6, 2, 10], "faces": {
                                                                          "west": {"uv": [9, 15, 10, 14],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [7, 0, 4], "to": [7, 1, 5], "faces": {
                                                                          "west": {"uv": [4, 16, 5, 15],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [7, 1, 5], "to": [7, 2, 6], "faces": {
                                                                          "west": {"uv": [5, 15, 6, 14],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [7, 2, 6], "to": [7, 3, 7], "faces": {
                                                                          "west": {"uv": [6, 14, 7, 13],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [7, 2, 9], "to": [7, 3, 10], "faces": {
                                                                          "west": {"uv": [9, 14, 10, 13],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [7, 1, 10], "to": [7, 2, 11], "faces": {
                                                                          "west": {"uv": [10, 15, 11, 14],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [7, 0, 11], "to": [7, 1, 12], "faces": {
                                                                          "west": {"uv": [11, 16, 12, 15],
                                                                                   "texture": "#ore"}}},
                                                                      {"from": [7, 1, 4], "to": [8, 1, 5], "faces": {
                                                                          "up": {"uv": [7, 4, 8, 5],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [5, 1, 5], "to": [7, 1, 6], "faces": {
                                                                          "up": {"uv": [5, 5, 7, 6],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [9, 1, 5], "to": [10, 1, 6], "faces": {
                                                                          "up": {"uv": [9, 5, 10, 6],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [5, 1, 6], "to": [6, 1, 7], "faces": {
                                                                          "up": {"uv": [5, 6, 6, 7],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [10, 1, 6], "to": [11, 1, 8], "faces": {
                                                                          "up": {"uv": [10, 6, 11, 8],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [11, 1, 8], "to": [12, 1, 10], "faces": {
                                                                          "up": {"uv": [11, 8, 12, 10],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [5, 1, 9], "to": [6, 1, 10], "faces": {
                                                                          "up": {"uv": [5, 9, 6, 10],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [6, 1, 10], "to": [7, 1, 11], "faces": {
                                                                          "up": {"uv": [6, 10, 7, 11],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [10, 1, 10], "to": [11, 1, 11],
                                                                       "faces": {"up": {"uv": [10, 10, 11, 11],
                                                                                        "texture": "#ore"}}},
                                                                      {"from": [7, 1, 11], "to": [9, 1, 12], "faces": {
                                                                          "up": {"uv": [7, 11, 9, 12],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [7, 2, 5], "to": [9, 2, 6], "faces": {
                                                                          "up": {"uv": [7, 5, 9, 6],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [6, 2, 6], "to": [7, 2, 7], "faces": {
                                                                          "up": {"uv": [6, 6, 7, 7],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [9, 2, 6], "to": [10, 2, 7], "faces": {
                                                                          "up": {"uv": [9, 6, 10, 7],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [5, 2, 7], "to": [6, 2, 9], "faces": {
                                                                          "up": {"uv": [5, 7, 6, 9],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [7, 2, 10], "to": [10, 2, 11], "faces": {
                                                                          "up": {"uv": [7, 10, 10, 11],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [10, 2, 8], "to": [11, 2, 10], "faces": {
                                                                          "up": {"uv": [10, 8, 11, 10],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [6, 2, 9], "to": [7, 2, 10], "faces": {
                                                                          "up": {"uv": [6, 9, 7, 10],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [7, 3, 6], "to": [9, 3, 7], "faces": {
                                                                          "up": {"uv": [7, 6, 9, 7],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [6, 3, 7], "to": [10, 3, 9], "faces": {
                                                                          "up": {"uv": [6, 7, 10, 9],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [7, 3, 9], "to": [10, 3, 10], "faces": {
                                                                          "up": {"uv": [7, 9, 10, 10],
                                                                                 "texture": "#ore"}}},
                                                                      {"from": [5, 1, 9], "to": [6, 2, 9], "faces": {
                                                                          "south": {"uv": [5, 15, 6, 14],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [6, 2, 9], "to": [7, 3, 9], "faces": {
                                                                          "south": {"uv": [6, 14, 7, 13],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [5, 0, 10], "to": [6, 1, 10], "faces": {
                                                                          "south": {"uv": [5, 16, 6, 15],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [11, 0, 10], "to": [12, 1, 10],
                                                                       "faces": {"south": {"uv": [11, 16, 12, 15],
                                                                                           "texture": "#ore"}}},
                                                                      {"from": [6, 1, 10], "to": [7, 2, 10], "faces": {
                                                                          "south": {"uv": [6, 15, 7, 14],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [10, 1, 10], "to": [11, 2, 10],
                                                                       "faces": {"south": {"uv": [10, 15, 11, 14],
                                                                                           "texture": "#ore"}}},
                                                                      {"from": [7, 2, 10], "to": [10, 3, 10], "faces": {
                                                                          "south": {"uv": [7, 14, 10, 13],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [6, 0, 11], "to": [7, 1, 11], "faces": {
                                                                          "south": {"uv": [6, 16, 7, 15],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [9, 0, 11], "to": [11, 1, 11], "faces": {
                                                                          "south": {"uv": [9, 16, 11, 15],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [7, 1, 11], "to": [10, 2, 11], "faces": {
                                                                          "south": {"uv": [7, 15, 10, 14],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [7, 0, 12], "to": [9, 1, 12], "faces": {
                                                                          "south": {"uv": [7, 16, 9, 15],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [7, 0, 4], "to": [8, 1, 4], "faces": {
                                                                          "north": {"uv": [9, 16, 8, 15],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [5, 0, 5], "to": [7, 1, 5], "faces": {
                                                                          "north": {"uv": [11, 16, 9, 15],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [8, 0, 5], "to": [10, 1, 5], "faces": {
                                                                          "north": {"uv": [8, 16, 6, 15],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [7, 1, 5], "to": [9, 2, 5], "faces": {
                                                                          "north": {"uv": [9, 15, 7, 14],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [10, 0, 6], "to": [11, 1, 6], "faces": {
                                                                          "north": {"uv": [6, 16, 5, 15],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [6, 1, 6], "to": [7, 2, 6], "faces": {
                                                                          "north": {"uv": [10, 15, 9, 14],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [9, 1, 6], "to": [10, 2, 6], "faces": {
                                                                          "north": {"uv": [7, 15, 6, 14],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [7, 2, 6], "to": [9, 3, 6], "faces": {
                                                                          "north": {"uv": [9, 14, 7, 13],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [5, 1, 7], "to": [6, 2, 7], "faces": {
                                                                          "north": {"uv": [11, 15, 10, 14],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [6, 2, 7], "to": [7, 3, 7], "faces": {
                                                                          "north": {"uv": [10, 14, 9, 13],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [9, 2, 7], "to": [10, 3, 7], "faces": {
                                                                          "north": {"uv": [7, 14, 6, 13],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [11, 0, 8], "to": [12, 1, 8], "faces": {
                                                                          "north": {"uv": [5, 16, 4, 15],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [10, 1, 8], "to": [11, 2, 8], "faces": {
                                                                          "north": {"uv": [6, 15, 5, 14],
                                                                                    "texture": "#ore"}}},
                                                                      {"from": [6, 0, 2], "to": [7, 0, 3], "faces": {
                                                                          "down": {"uv": [6, 14, 7, 13],
                                                                                   "texture": "#stone",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [7, 0, 5], "to": [8, 0, 6], "faces": {
                                                                          "down": {"uv": [7, 11, 8, 10],
                                                                                   "texture": "#stone",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [12, 0, 5], "to": [13, 0, 6], "faces": {
                                                                          "down": {"uv": [12, 11, 13, 10],
                                                                                   "texture": "#stone",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [2, 0, 6], "to": [3, 0, 7], "faces": {
                                                                          "down": {"uv": [2, 10, 3, 9],
                                                                                   "texture": "#stone",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [6, 0, 6], "to": [10, 0, 8], "faces": {
                                                                          "down": {"uv": [6, 10, 10, 8],
                                                                                   "texture": "#stone",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [12, 0, 12], "to": [13, 0, 13],
                                                                       "faces": {"down": {"uv": [12, 4, 13, 3],
                                                                                          "texture": "#stone",
                                                                                          "cullface": "down"}}},
                                                                      {"from": [7, 0, 10], "to": [9, 0, 11], "faces": {
                                                                          "down": {"uv": [7, 6, 9, 5],
                                                                                   "texture": "#stone",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [5, 0, 12], "to": [6, 0, 13], "faces": {
                                                                          "down": {"uv": [5, 4, 6, 3],
                                                                                   "texture": "#stone",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [6, 0, 8], "to": [11, 0, 10], "faces": {
                                                                          "down": {"uv": [6, 8, 11, 6],
                                                                                   "texture": "#stone",
                                                                                   "cullface": "down"}}},
                                                                      {"from": [3, 0, 6], "to": [3, 1, 7], "faces": {
                                                                          "east": {"uv": [10, 16, 9, 15],
                                                                                   "texture": "#stone"}}},
                                                                      {"from": [6, 0, 12], "to": [6, 1, 13], "faces": {
                                                                          "east": {"uv": [4, 16, 3, 15],
                                                                                   "texture": "#stone"}}},
                                                                      {"from": [7, 0, 2], "to": [7, 1, 3], "faces": {
                                                                          "east": {"uv": [14, 16, 13, 15],
                                                                                   "texture": "#stone"}}},
                                                                      {"from": [13, 0, 5], "to": [13, 1, 6], "faces": {
                                                                          "east": {"uv": [11, 16, 10, 15],
                                                                                   "texture": "#stone"}}},
                                                                      {"from": [13, 0, 12], "to": [13, 1, 13],
                                                                       "faces": {"east": {"uv": [4, 16, 3, 15],
                                                                                          "texture": "#stone"}}},
                                                                      {"from": [2, 0, 6], "to": [2, 1, 7], "faces": {
                                                                          "west": {"uv": [6, 16, 7, 15],
                                                                                   "texture": "#stone"}}},
                                                                      {"from": [5, 0, 12], "to": [5, 1, 13], "faces": {
                                                                          "west": {"uv": [12, 16, 13, 15],
                                                                                   "texture": "#stone"}}},
                                                                      {"from": [6, 0, 2], "to": [6, 1, 3], "faces": {
                                                                          "west": {"uv": [2, 16, 3, 15],
                                                                                   "texture": "#stone"}}},
                                                                      {"from": [12, 0, 5], "to": [12, 1, 6], "faces": {
                                                                          "west": {"uv": [5, 16, 6, 15],
                                                                                   "texture": "#stone"}}},
                                                                      {"from": [12, 0, 12], "to": [12, 1, 13],
                                                                       "faces": {"west": {"uv": [12, 16, 13, 15],
                                                                                          "texture": "#stone"}}},
                                                                      {"from": [6, 1, 2], "to": [7, 1, 3], "faces": {
                                                                          "up": {"uv": [6, 2, 7, 3],
                                                                                 "texture": "#stone"}}},
                                                                      {"from": [12, 1, 5], "to": [13, 1, 6], "faces": {
                                                                          "up": {"uv": [12, 5, 13, 6],
                                                                                 "texture": "#stone"}}},
                                                                      {"from": [2, 1, 6], "to": [3, 1, 7], "faces": {
                                                                          "up": {"uv": [2, 6, 3, 7],
                                                                                 "texture": "#stone"}}},
                                                                      {"from": [12, 1, 12], "to": [13, 1, 13],
                                                                       "faces": {"up": {"uv": [12, 12, 13, 13],
                                                                                        "texture": "#stone"}}},
                                                                      {"from": [5, 1, 12], "to": [6, 1, 13], "faces": {
                                                                          "up": {"uv": [5, 12, 6, 13],
                                                                                 "texture": "#stone"}}},
                                                                      {"from": [6, 0, 3], "to": [7, 1, 3], "faces": {
                                                                          "south": {"uv": [6, 16, 7, 15],
                                                                                    "texture": "#stone"}}},
                                                                      {"from": [12, 0, 6], "to": [13, 1, 6], "faces": {
                                                                          "south": {"uv": [12, 16, 13, 15],
                                                                                    "texture": "#stone"}}},
                                                                      {"from": [2, 0, 7], "to": [3, 1, 7], "faces": {
                                                                          "south": {"uv": [2, 16, 3, 15],
                                                                                    "texture": "#stone"}}},
                                                                      {"from": [5, 0, 13], "to": [6, 1, 13], "faces": {
                                                                          "south": {"uv": [5, 16, 6, 15],
                                                                                    "texture": "#stone"}}},
                                                                      {"from": [12, 0, 13], "to": [13, 1, 13],
                                                                       "faces": {"south": {"uv": [12, 16, 13, 15],
                                                                                           "texture": "#stone"}}},
                                                                      {"from": [6, 0, 2], "to": [7, 1, 2], "faces": {
                                                                          "north": {"uv": [10, 16, 9, 15],
                                                                                    "texture": "#stone"}}},
                                                                      {"from": [12, 0, 5], "to": [13, 1, 5], "faces": {
                                                                          "north": {"uv": [4, 16, 3, 15],
                                                                                    "texture": "#stone"}}},
                                                                      {"from": [2, 0, 6], "to": [3, 1, 6], "faces": {
                                                                          "north": {"uv": [14, 16, 13, 15],
                                                                                    "texture": "#stone"}}},
                                                                      {"from": [5, 0, 12], "to": [6, 1, 12], "faces": {
                                                                          "north": {"uv": [11, 16, 10, 15],
                                                                                    "texture": "#stone"}}},
                                                                      {"from": [12, 0, 12], "to": [13, 1, 12],
                                                                       "faces": {"north": {"uv": [4, 16, 3, 15],
                                                                                           "texture": "#stone"}}}],
        "display": {"thirdperson": {"rotation": [10, -45, 170], "translation": [0, 1.5, -2.75],
                                    "scale": [0.375, 0.375, 0.375]}}}


def generate_states(states: list) -> None:
    for state in states:
        json_doc = {"variants": {"": [{"model": "geolosys:block/{}".format(state)}]}}
        with open("./blockstates/{}.json".format(state), "w") as file:
            file.write(json.dumps(json_doc))
            print(
                    Fore.BLUE
                    + "Wrote ./blockstates/{}.json to disk".format(state)
                    + Fore.RESET
            )


def generate_item_models(states: list) -> None:
    for state in states:
        json_doc = {"parent": "geolosys:block/{}".format(state)}
        with open("./models/item/{}.json".format(state), "w") as file:
            file.write(json.dumps(json_doc))
            print(Fore.BLUE + "Wrote ./models/item/{}.json to disk".format(state) + Fore.RESET)


def generate_block_models(states: list) -> None:
    for state in states:
        json_doc = get_model(state.replace("_sample", ""))
        with open("./models/block/{}.json".format(state), "w") as file:
            file.write(json.dumps(json_doc))
            print(Fore.BLUE + "Wrote ./models/block/{}.json to disk".format(state) + Fore.RESET)


def main(block_state: bool, item_model: bool, block_model: bool) -> None:
    """
    The main program logic which generates blockstates based on the array below
    Args:
        block_state (bool): trigger whether or not to generate blockstates
        item_model (bool): trigger whether or not to generate item models
        block_model (bool): trigger whether or not to generate block models
    """
    states = [
        "hematite_ore_sample",
        "limonite_ore_sample",
        "malachite_ore_sample",
        "azurite_ore_sample",
        "cassiterite_ore_sample",
        "teallite_ore_sample",
        "galena_ore_sample",
        "bauxite_ore_sample",
        "platinum_ore_sample",
        "autunite_ore_sample",
        "sphalerite_ore_sample",
        "coal_ore_sample",
        "cinnabar_ore_sample",
        "gold_ore_sample",
        "lapis_ore_sample",
        "quartz_ore_sample",
        "kimberlite_ore_sample",
        "beryl_ore_sample",
    ]

    if block_state:
        generate_states(states)
    if item_model:
        generate_item_models(states)
    if block_model:
        generate_block_models(states)


if __name__ == "__main__":

    def print_help() -> None:
        """Prints the help prompt for the user to know their options"""
        print(Fore.YELLOW + "Possible arguments:" + Fore.RESET)
        print(Fore.CYAN + "    -i: Generate Item Models" + Fore.RESET)
        print(Fore.CYAN + "    -b: Generate Block Models" + Fore.RESET)
        print(Fore.CYAN + "    -s: Generate BlockStates" + Fore.RESET)
        print(Fore.CYAN + "    -a: Generate All" + Fore.RESET)
        print(Fore.CYAN + "    -h, ? : This screen" + Fore.RESET)


    possible_args = {
        "-a": False,
        "-i": False,
        "-b": False,
        "-s": False,
        "-h": False,
        "?": False,
    }

    for arg in sys.argv[1:]:
        for arg_name in possible_args:
            if arg_name in arg:
                possible_args[arg_name] = True
    if not any(list(possible_args.values())):
        print(Fore.RED + "No arguments given." + Fore.RESET)
        print_help()
        exit()

    if possible_args["-h"] or possible_args["?"]:
        print_help()
        exit()

    if possible_args["-a"]:
        main(True, True, True)
    else:
        main(possible_args["-s"], possible_args["-i"], possible_args["-b"])