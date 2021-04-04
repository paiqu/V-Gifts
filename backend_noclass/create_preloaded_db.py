'''

'''

import json
import database as db
import admin as ad

KEYWORDS_LST_haoran = [
    # tergets
    'men', 'man', 'women', 'woman', 'couple', 'mother', 'bride', 'groom', 'bridegroom',
    'father', 'love', 'friendship', 'friend', 'friends', 'girls',
    'girl', 'boys', 'boy', 'birthday', 'family', 
    # types
    'cloth', 'cotton', 'polyester', 'hoodies', 'hoody', 'food',
    'chocolate', 

]

KEYWORDS_LST_yifan = [
    # tergets
    'example',
    # types
    'example'

]

def add_product_to_db_special(file_name = 'database_manual.json'):
    temp = db.init_db()
    # file_name = 'database_manual.json'
    db.to_json(temp, file_name)
    lst = [
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            # more to add
        }
    ]
    # load products into db
    for prod in lst:
        db.add_prod(ad.new_product(prod['name'], prod['price'], prod['description'],\
                            None, prod['delivery_days'], prod['pic_link']), file_name)
    # show db
    db.pretty_print(db.load_json(file_name))

if __name__ == "__main__":
    add_product_to_db_special()

lst = [
        {
            'name': 'A N KINGPiiN Inspirational Bracelets for Women Inspirational Gift for Women Girls Men Motivational Birthday Cuff Bangle Friendship Personalized Mantra Jewelry Come Gift Box',
            'price': 12,
            'description': "Simple and elegant mantra cuff bracelet, minimalist style, personalized Birthday gift, Christmas gift, Mother's day gift. This bracelet is ADJUSTABLE and will fit most wrist sizes. High polished cuff bracelet, shinne surface, very smooth with rounded edges to avoid scratch your wrist, clear engraved easily reading. Comes with cute gift box, uplifting message engraved.",
            'delivery_days': 15,
            'pic_link': '/img/products/h001.jpg'
        },
        {
            'name': 'Rose Bear Women Gifts for Mom birthday girlfriend gifts for her , Rose Teddy Bear Rose Flowers Bear , Girls Valentines Bridal Wedding Anniversaries Birthday Graduation Gifts - Rose Bear with Box (red)',
            'price': 27,
            'description': "UNIQUE & EVERLASTING GIFT: rose Bear making this forever roses bears so special! gifts for mom,gifts for women,gifts for teen girls,gifts for her,rose bear teddy,rose flower,roses for delivery prime,rose bear teddy, rose teddy bear. rose bear Teddy bears are the kind of gift that brings a smile to any girl’s face just about any day. It doesn’t even have to be a special occasion to gift this beautiful teddy bear covered in white roses. If you want to make your girlfriend or wife feel special。rose flowers. THE PERFECT GIFT: Rose Teddy Bear arrives gift-ready in a fully assembled, crystal clear window box wrapped with premium satin ribbon。roses ,rose teddy bear ,rose bear with box ,rose bears ,flower teddy bear,rose box,rose bear teddy. HANDMADE & HIGH QUALITY: Rose Teddy Bear The 10 inch rose Bear is handcrafted with the best quality, life-like, never-bend artificial roses.The entire gift, including the wrap, is designed for durability. As a result, you will find that your gift can last a long time, in fact, it can last forever. You can use it to symbolize eternal love for your partner. rose teddy bear. DAZZLING & EYE CATCHING: Rose Bear Amaze the special someone in your life with this unforgettable rose teddy bear that from every angle. Perfect for Girlfriends, Weddings, Anniversaries, Birthdays, Graduations, Valentine’s Day,mother’s day,rose bears for valentines. rose teddy bear.",
            'delivery_days': 24,
            'pic_link': '/img/products/h002.jpg'
        },
        {
            'name': 'I Hope Your Day Is As Nice As Your Butt Keychain Boyfriend Girlfriend Gifts Keyring I Love You Wife Husband Gifts',
            'price': 7,
            'description': "Hook and Loop closure. Material: Alloy,Pendant Size:2.5*2.5cm,Ring Size:2.5*2.5cm(0.98*0.98inch);So cute and perfect gift. I hope your day is as nice as my your butt keychain;If you want to bring smile even laugh for the one you love, please don't miss the funny gag gift,it will be a big surprise. Funny boyfriend girlfriend gift,husband wife gift,couple lover gift in any accasion, promotion 2020.Good present for Valentine's Day,Thanksgiving Day and Christmas ect.; best birthday anniversary gifts for women men",
            'delivery_days': 7,
            'pic_link': '/img/products/h003.jpg'
        },
        {
            'name': 'KING & QUEEN Matching Couple Hoodie Set His & Hers Hoodies',
            'price': 65,
            'description': "50% Cotton, 50% Polyester. The perfect gift for couples. King & queen matching hoodies set. Great gift for valentine's day, wedding gifts, anniversary gifts, mom & dad gifts, his & hers gifts! Outstanding fabric quality! cozy hooded tops. The perfect match for fiance and fiancee , boyfriend & girlfriend - an absolute must have for couples! Cozy and warm matching couples sweatshirts - super comfy and super warm matching hoodies. Great for hubby & wifey Cute hoodie set fit for a king and a queen! official tstars merchandise",
            'delivery_days': 21,
            'pic_link': '/img/products/h004.jpg'
        },
        {
            'name': 'Mud Pie Sequin Bride Tote Bag',
            'price': 20,
            'description': "100% Jute. Imported. Laminated wipe-clean interior and interior pocket. Measures 16x 24x 9.",
            'delivery_days': 10,
            'pic_link': '/img/products/h005.jpg'
        },
        {
            'name': 'Thoughtfully Gifts, Rum Cocktail Infusion Gift Set, Flavors Include Mojito, Caribbean Twist and Strawberry Daiquiri, Pack of 3 (Contains NO Alcohol)',
            'price': 20,
            'description': None,
            'delivery_days': 18,
            'pic_link': '/img/products/h006.jpg'
        },
        {
            'name': 'Chocolate Gift Basket , Gourmet Snack Food Box in Keepsake Tin, Great for Birthday, Sympathy, Family Parties & Get Well - Bonnie & Pop',
            'price': 35,
            'description': "Great gift for families and corporate gifting alike. The right choice for multiple holidays like Christmas, Valentines Day, Easter, Hanukkah, Birthdays, Sympathy, Condolence, to say Thank You, I Love You, and everything in between. Don’t forget to add a gift message at checkout. Indulge in more than a delicious pound of assorted truffles. Including various White, Dark, and Milk Butter Pecan Patties, Cashew Clusters, Pretzel Clouds, Pecan Snappers, Sea Salt Caramels, English Toffee, Peppermint Patties, Bavarian Pretzels, Double Silk Truffles, Coconut Haystacks, and Peanut Clusters. Each chocolate arrives INDIVIDUALLY WRAPPED to promote hygiene safety, freshness and cleanliness for sharing. Keepsake tin is a remembrance long after the occasion and snacks are gone - send one to yourself.",
            'delivery_days': 5,
            'pic_link': '/img/products/h007.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
        {
            'name': 'sample',
            'price': 3,
            'description': None,
            'delivery_days': 15,
            'pic_link': '/img/products/001.jpg'
        },
    ]