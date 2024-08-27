class JsonResSample:
    """
    json response you expect
    """

    # random/group/face-positive
    emoji = {
        "name": "hugging face",
        "category": "smileys and people",
        "group": "face positive",
        "htmlCode": ["&#129303;"],
        "unicode": ["U+1F917"]
    }

    # random/category/non-exist
    category_not_exist = {
        "message": "emojis with this category do not exist"
    }

    # all/group/animal-bird
    all_emoji = [
        {"name": "turkey", "category": "animals and nature", "group": "animal bird", "htmlCode": ["\u0026#129411;"],
         "unicode": ["U+1F983"]},
        {"name": "chicken", "category": "animals and nature", "group": "animal bird", "htmlCode": ["\u0026#128020;"],
         "unicode": ["U+1F414"]},
    ]
