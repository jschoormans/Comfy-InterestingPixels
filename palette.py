import time
import random
palettes = [
    "charcoal ivory cobalt palette",
    "graphite white silver palette",
    "onyx slate azure palette",
    "steel white midnight palette",
    "smoke gray graphite palette",
    "mahogany cream burgundy palette",
    "antique gold ivory rust palette",
    "warm taupe maroon palette",
    "burgundy beige copper palette",
    "chocolate caramel ochre palette",
    "lavender cream pearl palette",
    "antique rose ivory palette",
    "taupe champagne blush palette",
    "french blue blush palette",
    "royal lilac beige palette",
    "granite slate silver palette",
    "smoke slate pewter palette",
    "graphite copper slate palette",
    "ebony ash silver palette",
    "vibrant magenta teal palette",
    "sunset fuchsia turquoise palette",
    "ruby emerald sapphire palette",
    "cobalt saffron fuchsia palette",
    "indigo coral marigold palette",
    "icy white mint palette",
    "soft gray dove palette",
    "frosted ash beige palette",
    "alpine cream sky palette",
    "snowdrop silver pearl palette",
    "sage walnut cream palette",
    "muted cocoa cream palette",
    "sandy dune beige palette",
    "taupe linen cream palette",
    "driftwood beige cocoa palette",
    "terra cotta olive rust palette",
    "burnt sienna walnut mustard palette",
    "brick clay ochre palette",
    "dusty taupe ember palette",
    "smoked copper bronze palette",
    "sepia rose mauve palette",
    "antique olive mustard palette",
    "weathered burgundy cream palette",
    "retro teal sepia palette",
    "vintage mauve slate palette",
    "jigsaw turquoise magenta palette",
    "patchwork lime fuchsia palette",
    "mosaic coral teal palette",
    "kaleidoscope amber violet palette",
    "varied ruby mint palette",
    "vivid mango turquoise palette",
    "exotic papaya lime palette",
    "vibrant coral peach palette",
    "sunset banana teal palette",
    "lush hibiscus sapphire palette",
    "retro tangerine mustard palette",
    "vintage avocado ochre palette",
    "mod walnut olive palette",
    "sunset tangerine mint palette",
    "mid-century burgundy beige palette",
    "seafoam ivory coral palette",
    "aqua dune sand palette",
    "ocean mist blue palette",
    "coastal blue pearl palette",
    "sandy aqua sky palette",
    "barn red cream palette",
    "rustic wheat amber palette",
    "farmhouse sage rust palette",
    "weathered taupe cream palette",
    "rural wheat cinnamon palette",
    "crimson blush ivory palette",
    "peach coral blush palette",
    "soft rose ivory palette",
    "gentle lavender blush palette",
    "sunrise peach cream palette",
    "dusky plum silver palette",
    "muted periwinkle cream palette",
    "amethyst violet cream palette",
    "cocoa beige caramel palette",
    "chic mauve blush palette",
    "plum rose taupe palette",
    "smoky plum cream palette",
    "radiant ruby cream palette",
    "velvet burgundy ivory palette",
    "serene sky blue palette",
    "morning sky blue palette",
    "delicate blue powder palette",
    "twilight lavender sky palette",
    "ethereal aqua sky palette",
    "lemonade coral cream palette",
    "fresh lime zest palette",
    "minted ivory peach palette",
    "golden hour blush palette",
    "copper sunrise cream palette",
    "dusky amber ivory palette",
    "crisp cranberry cream palette",
    "buttered sienna ivory palette",
    "rich maroon cream palette",
    "platinum rose cream palette",
    "elegant silver blush palette",
    "vibrant coral apricot palette"
  ]


class RandomPalette:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
            }
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "random_palette"
    CATEGORY = "InterestingPixels"
    OUTPUT_NODE = True
    

    def random_palette(self, seed=None):
        # Get length of palettes list
        length = len(palettes)
        
        if seed is not None:
            # Use provided seed for deterministic selection
            random.seed(seed)
            index = random.randint(0, length - 1)
        else:
            # Generate random index using modulo of system time
            index = int(time.time() * 1000) % length
            
        # Return the full palette string at the random index
        return (palettes[index],)