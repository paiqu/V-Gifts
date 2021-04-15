"""
    This file organise keywords
"""
import json

KEYWORD_DICT = {
    # for men
    0: ["men", "man", "dad", "groom", "bridegroom", "father's", 
        "men's", "man's", "family", ],
    # for women
    1: ["women", "woman", "mom", "bride", "mother", "women's", "woman's", 
        "family", "mother's", "lady", "ladies", ],
    # for children
    2: ["lego", "toy", "piano", "bag", "teen", "kid", "kids", "family", "girls", 
        "girl", "boys", "boy", "birthday",],
    # for friends
    3: ["whiskey", "cocktail", "music", "music box", "bluetooth", "bag", "friendship", 
        "friend", "friends",  ],
    # for elder
    4: ["grandma", "grandmother", "grandpa", "grandfather", "family", ],
    # for relationship
    5: ["couple", "love", "candle", ],
    # foods
    6: ["cooking", "organic", "grilling", "grill", "cook", "pork", "beef", "snack",
        "sweet", "hot", "spicy", "protein", "health", "healthy", "food",
        "chocolate", "honey", "wellness", "gluten-free", "vegetarianism",
        "vegan", "food", "foods"],
    # tools
    7: ["survival", "gear", "tool", "tools", "flash", "bag",],
    # luxuries
    8: ["necklace", "earrings", "jewelry", "ring", "gold", "luxury", "pendant", ],
    # entertainment
    9: ["cloth", "hoodies", "hoody",  "travel", "outdoor", "entertainment", "music",],
    # working
    10: ["office", "pen", "pens", "professional", "working", "work", "notebook", ],
}

def category_to_dict(cate):
    new_dict = {}
    for key,val in cate.items():
        for word in val:
            if word in new_dict:
                new_dict[word].append(int(key))
            else:
                new_dict[word] = [int(key)]
    return new_dict

def save_dict_to_file(kw_dct, filename = "keywords_dict.json"):
    with open(filename, "w") as fp:
        json.dump(kw_dct, fp)
    return {}

if __name__ == "__main__":
    save_dict_to_file(category_to_dict(KEYWORD_DICT))