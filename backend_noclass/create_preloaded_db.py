'''

'''

import json
import database as db
import admin as ad

KEYWORDS_LST_haoran = [
    # targets
    'men', 'man', 'women', 'woman', 'couple', 'mother', 'bride', 'groom', 'bridegroom',
    'father', 'love', 'friendship', 'friend', 'friends', 'girls', 'lady', 'ladies',
    'girl', 'boys', 'boy', 'birthday', 'family', 'mother\'s', 'father\'s', 
    'men\'s', 'man\'s', 'women\'s', 'woman\'s',

    # types
    'cloth', 'cotton', 'polyester', 'hoodies', 'hoody', 'food',
    'chocolate', 'speaker', 'music', 'bluetooth', 'cooking', 'organic',
    'grilling', 'grill', 'cook', 'pork', 'beef', 'snack', 'sweet', 'hot',
    'spicy', 'protein', 'health', 'healthy', 'candle', 'honey', 'wellness',
    'bag', 'travel', 'cute', 'outdoor', 'gluten-free', 'luxury',
    'office', 'pen', 'pens', 'professional', 'gold', 'necklace',
    'ring', 'jewelry'


]

KEYWORDS_LST_yifan = [
    # targets
    'example',
    # types
    'example'

]

def add_product_to_db_special(prod_lst, file_name = 'database_manual.json'):
    temp = db.init_db()
    # file_name = 'database_manual.json'
    db.to_json(temp, file_name)
    # lst = [
    #     {
    #         'name': 'sample',
    #         'price': 3,
    #         'description': None,
    #         'delivery_days': 15,
    #         'pic_link': '/img/products/001.jpg'
    #     },
    #     {
    #         # more to add
    #     }
    # ]
    # load products into db
    for prod in lst:
        db.add_prod(ad.new_product(prod['name'], prod['price'], prod['description'],\
                            None, prod['delivery_days'], prod['pic_link']), file_name)
    # show db
    # db.pretty_print(db.load_json(file_name))

if __name__ == "__main__":
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
                'description': "rose bear Teddy bears are the kind of gift that brings a smile to any girl's face just about any day. It doesn’t even have to be a special occasion to gift this beautiful teddy bear covered in white roses. If you want to make your girlfriend or wife feel special。rose flowers. THE PERFECT GIFT: Rose Teddy Bear arrives gift-ready in a fully assembled, crystal clear window box wrapped with premium satin ribbon. roses ,rose teddy bear ,rose bear with box ,rose bears ,flower teddy bear,rose box,rose bear teddy. Rose Bear Amaze the special someone in your life with this unforgettable rose teddy bear that from every angle. Perfect for Girlfriends, Weddings, Anniversaries, Birthdays, Graduations, Valentine\'s Day,mother\'s day,rose bears for valentines. rose teddy bear.",
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
                'name': 'Echo Dot (2nd Generation) - Smart speaker with Alexa - Black',
                'price': 21,
                'description': 'Echo Dot is a voice-controlled speaker that uses Alexa to play music, control smart home devices, make calls, answer questions, set timers and alarms, and more. Play music from Amazon Music, Apple Music, Spotify, Pandora, SiriusXM, TuneIn, and iHeartRadio. Call or message family and friends hands-free, or drop in from the Alexa App to your Echo device. Controls lights, locks, thermostats, and more with compatible connected devices. Use the built-in speaker, or for bigger sound, connect to speakers through Bluetooth or audio cable.',
                'delivery_days': 15,
                'pic_link': '/img/products/h008.jpg'
            },
            {
                'name': 'All-new Echo Dot (4th Gen, 2020 release) | Smart speaker with Alexa | Charcoal',
                'price': 35,
                'description': 'Meet the all-new Echo Dot - Our most popular smart speaker with Alexa. The sleek, compact design delivers crisp vocals and balanced bass for full sound. Voice control your entertainment - Stream songs from Amazon Music, Apple Music, Spotify, SiriusXM, and others. Play music, audiobooks, and podcasts throughout your home with multi-room music. Ready to help - Ask Alexa to tell a joke, play music, answer questions, play the news, check the weather, set alarms, and more. Control your smart home - Use your voice to turn on lights, adjust thermostats, and lock doors with compatible devices. Connect with others - Call almost anyone hands-free. ',
                'delivery_days': 15,
                'pic_link': '/img/products/h009.jpg'
            },
            {
                'name': 'SaltWorks Salts of the World Collection Gift Set, Premium Sea Salt, Set of 6, 39.8 Ounce',
                'price': 39,
                'description': 'PREMIUM SALT COLLECTION: From the beautiful turquoise waters off the coast of Mexico to France, this premium salt collection features six distinctly different flavors from around the world. THE PERFECT GIFT: Harvested from different regions of the world, this set of gourmet sea salts makes a great gift for someone special or yourself. SERIOUS ABOUT SALT: Perfect for cooking and grilling, SaltWorks offers a wide range of traditional salts, finishing salts, delicious smoked salts and organic peppercorns. COMMITTED TO QUALITY: SaltWorks is passionate about producing all-natural salts that are OU Kosher certified, organic compliant, non-GMO, chemical free, allergen free and gluten free',
                'delivery_days': 30,
                'pic_link': '/img/products/010.jpg'
            },
            {
                'name': 'Jack Links Jack Link\'s Beef Jerky, Sweet & Hot, 9 Oz (Pack of 2)',
                'price': 20,
                'description': 'GOOD SOURCE OF PROTEIN. MADE WITH 100% PREMIUM BEEF. FULL ON FLAVOR. PERFECT EVERYDAY SNACK.',
                'delivery_days': 2,
                'pic_link': '/img/products/h011.jpg'
            },
            {
                'name': 'Jack Link’s Premium Cuts Beef Steak, Teriyaki, Great Protein Snack with 9g of Protein and 9g of Carbs per Serving, Made with 100% Premium Beef, 1 Ounce (Pack of 12)',
                'price': 16,
                'description': "FULL OF FLAVOR. MADE WITH 100% PREMIUM BEEF. EXCELLENT SOURCE OF PROTEIN. READY-TO-EAT BIG PACKS.",
                'delivery_days': 2,
                'pic_link': '/img/products/h012.jpg'
            },
            {
                'name': 'Longevity Dehydrated Sea Grapes, 4.23 oz of 6 packs, - Umibudo Green Caviar, Lato Seaweed, Precious Gift From The Sea | Enhance Health, Weight Loss, Boosting Immune System.',
                'price': 20,
                'description': None,
                'delivery_days': 7,
                'pic_link': '/img/products/h013.jpg'
            },
            {
                'name': 'Bekind Good Vibes 6 Scented Candles Set - Scented Candles for Home, Relaxing Stress Relief, Aromatherapy - Natural Soy Wax and Fragrance - Gifts for Women, Mom, Best Friend, Wife, Birthday',
                'price': 23,
                'description': None,
                'delivery_days': 5,
                'pic_link': '/img/products/h014.jpg'
            },
            {
                'name': 'Aglary Scented Candles Gifts Sets for Women-Rose, Lavender, Jasmine and Ocean Breeze, Soy Wax Travel Tin Aromatherapy Candle Gift Set for Christmas, Birthday,Valentine’s Day',
                'price': 20,
                'description': None,
                'delivery_days': 5,
                'pic_link': '/img/products/h015.jpg'
            },
            {
                'name': 'Sweetest Taboo Deluxe Scented Candle, Luxury Hotel Inspired Big Candle with Hints of Decadent Citrus, Juicy Berries, and Floral Peony, Long Lasting 300 Hour Burn Time, 55oz Black',
                'price': 100,
                'description': None,
                'delivery_days': 5,
                'pic_link': '/img/products/h016.jpg'
            },
            {
                'name': 'VINCIGANT Black Candle Holders for Taper Candles with Handle, Retro Iron Candlestick Holders for Dhristmas, Home Decor, Holiday Centerpieces,Pack of 4',
                'price': 20,
                'description': None,
                'delivery_days': 5,
                'pic_link': '/img/products/h017.jpg'
            },
            {
                'name': 'Oflamn Duffle Bag Canvas Leather Weekender Overnight Travel Carry On Tote Bag with Shoe Compartment and Toiletry Bag (Blue White Dots)',
                'price': 60,
                'description': None,
                'delivery_days': 35,
                'pic_link': '/img/products/h018.jpg'
            },
            {
                'name': 'TURNER Certified Raw New Zealand Manuka Honey with UAF1000+ (8.8oz/250g) 1000x More Power, Greatest Gift to Support Everyday Wellness, Natural Probiotic, Prebiotic, Antioxidant Superfood, 1 Jar',
                'price': 40,
                'description': None,
                'delivery_days': 14,
                'pic_link': '/img/products/h019.jpg'
            },
            {
                'name': 'Cestina Women Ladies Big Canvas Cute Weekender Overnight Travel Tote Duffel Carry On Bag Gym Bag (Green)',
                'price': 36,
                'description': 'Made of durable and soft canvas, PU leather,smooth zippers,it is perferct for anyone looking for pack two to three days worth of clothing, towels, gifts, make up, hair accessories, etc. a weekender bag or a cute carry-on duffel. You can get this spacious bag as perfect gift for Girl friend, Mom, Wife for Mother\'s day, Valentine\'s day, Christmas, Birthday or other Festival. She will absolutely in love with it!',
                'delivery_days': 14,
                'pic_link': '/img/products/h020.jpg'
            },
            {
                'name': 'Weekender Bag, BAGSMART Carry On Bag Travel Duffle Bag Large Overnight Bag for Women, Dusty Pink',
                'price': 40,
                'description': "Compact Sizes- 17.7 x 7.9 x 11.8 inch, meets most international carry-on requirements; Large capacity is big enough to store all your personal items. Travel-friendly Design- opens down the middle like a suitcase for easy packing and TSA checkpoint; Back RFID blocking pocket to protect against unwanted scans. It makes a great choice to be used in various ways and places, suitable for travel, business trips, gym, commuting, outdoor activities, universities, offices, excursions.",
                'delivery_days': 14,
                'pic_link': '/img/products/h021.jpg'
            },
            {
                'name': 'FreshJax Handcrafted Organic Grilling Spice Gift Set for Pork: Sriracha Sea Salt, Rosy Cheeks BBQ Spice and Bold Bayou Cajun Seasoning (3 pack)',
                'price': 35,
                'description': "SRIRACHA will enthuse pork burgers, pork lettuce wraps, and roasted veggies with its spicy and sweet flavor. ROSY CHEEKS gives a tantalizing southern flavor to ribs, pulled pork and baked beans. BOLD BAYOU will take your taste buds on a tour of the Big Easy’s favorite Cajun pork stew recipes. CERTIFIED ORGANIC by Americert International, CERTIFIED KOSHER by Gesher K, Gluten-free, Non-GMO, Non-Irradiated, No Artificial Flavors.",
                'delivery_days': 3,
                'pic_link': '/img/products/h022.jpg'
            },
            {
                'name': 'Michael Kors Men\'s Slim Runway Stainless Steel Quartz Watch',
                'price': 144,
                'description': None,
                'delivery_days': 13,
                'pic_link': '/img/products/h023.jpg'
            },
            {
                'name': 'Mens Analog Digital LED 50M Waterproof Outdoor Sport Watch Military Multifunction Casual Dual Display 12H/24H Stopwatch Calendar Wrist Watch',
                'price': 26,
                'description': "Multi-function sports watch: with stopwatch, dual-time display, independent alarm, 12/24H time, calendar, LED backlight, waterproof, shockproof and other functions. These features make it the perfect choice for all kinds of outdoor sports and everyday use. High-quality materials: The soft PU rubber band makes it comfortable to wear, and the durable plastic casing and mineral glass mirrors are extremely resistant to pressure and can be used in any environment.",
                'delivery_days': 21,
                'pic_link': '/img/products/h024.jpg'
            },
            {
                'name': 'Black Lacquer Rollerball Pen Scriveiner - Stunning Luxury Pen with 24K Gold Finish, Schmidt Ink Refill, Best Roller Ball Pen Gift Set for Men & Women, Professional, Executive Office, Nice Pens',
                'price': 30,
                'description': "ENJOY THE FEEL OF A TRUE LUXURY PEN IN YOUR HAND – Stunning luxury rollerball pen by Scriveiner. Brass with jet-black lacquer finished in 24 karat gold. Premium quality and understated luxury from a boutique British brand.TRANSCRIBE YOUR THOUGHTS EFFORTLESSLY – We use the Schmidt liquid ink system from Germany which allows your pen to glide smoothly across any type of paper. This combines the ink feel of a fountain pen with the convenience of a ballpoint and gives a superior writing action to gel ink pens. Perfectly weighted and balanced for your writing comfort – this is a luxury pen designed for those who love to write every day.",
                'delivery_days': 21,
                'pic_link': '/img/products/h025.jpg'
            },
            {
                'name': 'Silver Chrome Fountain Pen Scriveiner - Stunning Luxury Pen with 24K Gold Finish, Schmidt 18K Gilded Nib (Medium), Best Pen Gift Set for Men & Women, Professional, Executive Office, Nice Pens',
                'price': 47,
                'description': "ENJOY THE FEEL OF A TRUE LUXURY PEN IN YOUR HAND – Stunning luxury rollerball pen by Scriveiner. Brass with jet-black lacquer finished in 24 karat gold. Premium quality and understated luxury from a boutique British brand.TRANSCRIBE YOUR THOUGHTS EFFORTLESSLY – We use the Schmidt liquid ink system from Germany which allows your pen to glide smoothly across any type of paper. This combines the ink feel of a fountain pen with the convenience of a ballpoint and gives a superior writing action to gel ink pens. Perfectly weighted and balanced for your writing comfort – this is a luxury pen designed for those who love to write every day.",
                'delivery_days': 21,
                'pic_link': '/img/products/h026.jpg'
            },
            {
                'name': '2.0 ct Brilliant Heart Cut Stunning Genuine Natural London Blue Topaz Ideal VVS1 D Solitaire Pendant Necklace With 16" Gold Chain Box Birthstone Solid 14k Yellow Gold Clara Pucci',
                'price': 316,
                'description': "Highest quality Genuine Clarity VVS1 Color D Ideal cut stunning Flawless Center Stones. Solid premium 14k stamped gold.",
                'delivery_days': 15,
                'pic_link': '/img/products/h027.jpg'
            },
            {
                'name': 'Jewelry Necklaces Hand Polished Link Necklaces 14k White Gold 13.4mm Hand-polished Rounded Curb Link Chain',
                'price': 32830,
                'description': "Solid Casted Polished 14K White gold Avail. in 10k yellow gold Avail. in 18k yellow gold Avail. in 14k yellow gold Special lengths avail. Heavy duty box Avail. in 10k white gold Avail. in 18k white gold Avail. in 14k rose gold",
                'delivery_days': 15,
                'pic_link': '/img/products/h028.jpg'
            },
            # {
            #     'name': 'sample',
            #     'price': 3,
            #     'description': None,
            #     'delivery_days': 15,
            #     'pic_link': '/img/products/001.jpg'
            # },
            
        ]
    
    add_product_to_db_special(lst)