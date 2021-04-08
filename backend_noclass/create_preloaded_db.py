'''

'''

import json
import database as db
import admin as ad
import user as us
import webpage as wb

# KEYWORDS_LST_haoran = [
#     # targets
    
    

#     # types
#      'cotton', 'polyester', 'speaker', 'music', 'bluetooth', 
    
#     'necklace',
#     'jewelry'
# ]

# KEYWORDS_LST_yifan = [
#     # tergets
#     'fandom', 'religion', 'tennage', 'musicion', 
#     # types
#     'wine tumbler', 'mug', 'candle', 'cushion', 'glass', 
#     'cross', 'metal', 'star war',
#     'cookbook', 'book',  'gadget', 'brick', 
#     'water', 'player', 
# ]


def add_product_to_db_special(prod_lst, file_name = 'database_manual.json'):
    # temp = db.init_db()
    # file_name = 'database_manual.json'
    temp = db.load_json(file_name)
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
    for prod in prod_lst:
        db.add_prod(ad.new_product(prod['name'], prod['price'], prod['description'],\
                            None, prod['delivery_days'], prod['pic_link'], file_name), file_name)
    # show db
    # db.pretty_print(db.load_json(file_name))

if __name__ == "__main__":
    db.to_json(db.init_db(), 'database_manual.json')

    lst_hr = [
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
                'pic_link': '/img/products/h010.jpg'
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
    
    lst_yifan = [
        {
            'name': 'Gifts For Grandma - Grandma Birthday Gifts - Best Grandma Gifts For Grandmother, New Grandma, First Time Grandma, Gigi, Mimi, Grammy From Grandchildren, Granddaughter, Grandkids - 12 Oz Wine Tumbler',
            'price': 20,
            'description': "A LOVELY PRESENT - Paint a wide smile on your grandmother's face with this tumbler. Made with attention to detail, this durable wine tumbler offers value for your money. The topnotch quality of this tumbler makes it an impressive gift whatever the occasion. FUN, WITTY DESIGN - Poke fun and laugh with your nana with this wine tumbler! Perfect gifts ideal for grandmother, new grandma, first time grandma, gigi, mimi, grammy. DOUBLE WALL VACUUM INSULATION - We use double-wall insulation to help retain hot and cold liquid temperatures, which makes our wine tumbler also great for water, coffee, cola, beer, juice, tea, ice cream, cocktails and more BPA FREE AND DURABLE - These tumblers also come with a convenient reusable drink straw, straw cleaning brush, and BPA-free drink lid. Crafted with 18/8 food grade stainless steel these tumblers are durable, unbreakable, sweat proof, rust resistant and perfect for backyard barbecues, hanging out at the pool, or enjoying a hot day at the beach with friends. GIFTS FOR GRANDMA, GRANDMA BIRTHDAY GIFTS - Complete with a convenient gift giving box these drink cups make a fun and personal gift choice for birthdays, holidays, Christmas or just because.",
            'delivery_days': 5,
            'pic_link': '/img/products/y001.jpg'
        },
        {
            'name': "Gifts for Grandma - Grandma Gifts Set Includes Sterling Silver Necklace，Earrings, Pink Marble Jewelry Trays,Pink Marble Mug, Scented Candle and Flower – Best Mother's Day Birthday Gift Set",
            'price': 47,
            'description': "♥GRANDMA GIFTS SET PACK🎁-'Best Gandma Ever' Pink Marble Mug and a gold spoon, Pink Marble Jewelry Trays with 925 sterling silver necklace and a pair of Earrings,a scented candle and a bunch of carnations. Packaged with CUTE box and gift card. ♥MOTHERS DAY GIFTS FOR NANA-Perfect gift for the fabulous people in your life! Individually gift boxed that is sure to bring a smile. ♥BEST GRANDMA GIFT IDEAS-All the gifts are beautifully assorted, your grandma will love it. Heavy box with very cute and great presentation. ♥NANA GIFTS SET READY-Our gifts box is designed to provide the best experience. No need to repackage. ♥THE BEST VALUE-If any other issue, Please feel free to contact us for solution, we’ll reply you in 24 hours, we will try our 200% effort to make you 100% satisfy. SO HURRY UP! BUY NOW!",
            'delivery_days': 7,
            'pic_link': '/img/products/y002.jpg'
        },
        {
            'name': 'Best Gift Grandma I Love You More Than The Stars in The Sky You Mean The World to Me Blessing Cotton Linen Throw Pillow Case Cushion Cover Home Office Decorative Square 18',
            'price': 9,
            'description': "1：Best Gifts Grandma I Love You More Than The Stars In The Sky You Mean The World To Me Blessing. 2：Measures 18 inches square, 45 x 45 cm，1-2cm deviation is allowed, because of manual measurement. 3：This cushion cover has an invisible zipper, Safe to machine wash. Print just On ONE side. 4：Durable and environmentally friendly Cotton linen Materials.QTY:1 Piece (not include filler,only the pillowcase) weight:120g. 5：i have a factory ,I have a variety of styles, can provide custom",
            'delivery_days': 3,
            'pic_link': '/img/products/y003.jpg'
        },
        {
            'name': 'Gifts for Grandpa - "Grandpa Juice" - 11oz Funny Whiskey/Cocktail Glass- Idea From Daughter, Fathers Day, Papa, New, For Birthday, Grandson, Granddaughter, Grandkids',
            'price': 16,
            'description': "Gifts for Grandpa - 'Grandpa Juice' - 11oz Funny Whiskey/Cocktail Glass- Gift idea From Son, Daughter, New, For Birthday, Grandson, Granddaughter. THICK heavy base for a balanced grip QUALITY product made from the highest standard glass material in the U.S.A. MODERN/SLEEK cylindrical glass design. PERMANENT writing that will not fade or peel GUARANTEED",
            'delivery_days': 15,
            'pic_link': '/img/products/y004.jpg'
        },
        {
            'name': 'Lastsummer You are My Sunshine Music Box – Gift for Grandpa – 1 Set（Black）',
            'price': 13,
            'description': "NOVEL DESIGN: This Delicate Laser Engraved Music Box is made of Natural Wood, No harmful substance, Odorless, it will be the perfect gift for Birthday, Graduation, Anniversary, Holiday, Valentine’s Day, Christmas, New year, Thanksgiving Day, Black Friday, Father’s Day, Mother’s Day... PERFECT SIZE: The Music Box Measuring: 2.55'×2.16'×1.57' and 1 Music Box each package, you can easily hold this Cute and Tiny Music box in your Palm, It’s a great gift for your son, daughter, grandkids, niece, nephew, grandparent, aunt, uncle, mom, dad, sister, brother. EASY OPERATE: No Battery, all you have to do is Keep cranking the handle to play the Music and the beautiful melody 'You Are My Sunshine' will come out. MEMORABLE GIFT: The Clear and Meaningful Message was engraved on the music box: “I LOVE YOU More Than The Stars In The Sky, More Than The Trees In The Forest. Grandpa, You Mean The World To Me.”",
            'delivery_days': 7,
            'pic_link': '/img/products/y005.jpg'
        },
        {
            'name': 'Grandpa Handmade Glass Cross: Sentimental Gift for Grandpa',
            'price': 18,
            'description': "Uniquely handmade in the USA 4' Blue Glass Cross Loving Grandpa sentiment printed of 100# gloss paper for keeping. Packaged in 5.5'x5.5' White Gift Box with Clear Lid Great idea for Grandpa's birthday, Christmas, or any day you are thinking of him. Proudly display on ornament stand, knob, mirror or tree. Perfect for year round giving as a gift for grandpa from a grandson, granddaughter or grandchildren. All crosses are individually made and no two will be alike, just like Grandpas!",
            'delivery_days': 7,
            'pic_link': '/img/products/y006.jpg'
        },
        {
            'name': 'Fandom Emporium Millenium Falcon Ornament Gift Christmas Tree Winter Holiday Fandom Teen Adult Present Fan Pendant Durable',
            'price': 6,
            'description': "An absolutely gorgeous, beautifully crafted ornament, designed by us, for you! The holiday season is all about showing appreciation for what you love, displaying your love and care for the world, and what better way to do that than an ornament like this? While glass and ceramic ornaments are all lovely, they're also extremely fragile and breakable, leaving their lifetimes only as long as their handlers don't manage to trip while carrying them. That's why we make all our ornaments out of metal, leaving them durable and more than capable of handling being dropped a few times. They'll withstand the test of time, so you can have your peace of mind. This ornament makes for the perfect gift and a wonderful decoration. The super fan in your life- whether it's your sibling, parent, significant other, coworker, best friend, or even yourself- is sure to love it.",
            'delivery_days': 3,
            'pic_link': '/img/products/y007.jpg'
        },
        {
            'name': 'Universe of Fandoms TV Movies Show Original Design Quality Anime Cosplay Superhero flash ring Gifts for Men Woman',
            'price': 15,
            'description': "Great For Super hero TV Movies Show Original Design Quality Anime Cosplay Fans! We know you're a fan of Super hero TV Movies Show Original Design Quality Anime Cosplay, because we are too! And we absolutely love being able to show off our passion with flair and elegance. And when we struggled to find the right way to do so, we decided to just make the stuff ourself! That's why we're doing our best to help you flash your fandom pride with these gorgeous Ring! I deal Gift for Any Occasion! Struggling to find the perfect gift for a friend or loved one on a special day? Well worry not! These Ring are perfect for that fantastic fan in your life for every occasion Birthdays, Mother's Day, Valentine's Day, or even 'Just Because', it's always nice to receive a little special something, especially when the special something is something as special as one of these Ring! Quality Goods! All of our products are made while keeping you as our highest priority. That's why we make all our goods with a High Quality Alloy and gorgeous finish, all of it Hypoallergenic and Nickel Free! They'll last you years without tarnishing without any need for polishing or cleaning! Designed By Us,Packaged in a Free Gift Box! FREE SHIPPING!",
            'delivery_days': 3,
            'pic_link': '/img/products/y008.jpg'
        },
        {
            'name': 'Bitch Peas Journal Notebook: Funny Vegan Gift 100 Page College Ruled Diary Lined Journal Notebook Lined Notes Blank Paper Write Composition Back To School Gift Large (8.5 x 11 inch) ',
            'price': 9,
            'description': "Funny Vegan Christmas Gift Ideas for Men WomenBe kind to every kind and reject animal cruelty! Perfect gift idea for vegan Christmas present, Thanksgiving present, anniversary present or birthday present with funny vegan vegetarian humor saying or food pun. Protest and march for animal rights.If you believe animals are friends and not food, this is for you. Designed for cow lover, pig lover, fish lovers, pet lover, vegan or friend who wants to proudly show their passion for vegetarianism, dieting, fitness, veganism, healthy eating and diet.Perfect gift idea for vegan Christmas present, Thanksgiving present, anniversary present or birthday present with funny vegan vegetarian humor saying or food pun. Protest and march for animal rights. If you believe animals are friends not food, this one is for you. Designed for animal lovers, pet lover, vegan or friend who wants to proudly show their passion for vegetarianism, dieting, fitness, veganism, healthy eating and animal rights. Be kind to every kind and reject animal cruelty!",
            'delivery_days': 3,
            'pic_link': '/img/products/y009.jpg'
        },
        {
            'name': 'Ladytree S925 Sterling Silver Vegan Necklace Cubic Zirconia Green Symbol Necklace for Vegetarian Women,18 inches',
            'price': 29,
            'description': "Both 'V'and Green Leaf are the official symbol of vegetarianism.The modern vegan can compliment their ethical and vegan lifestyle with it and also a perfect conversation starter Share this necklace with all of you fierce vegans out there! Show your love and admiration for these vegan friends who celebrate and respect all animals live free right. Material:925 Sterling Silver with White Cubic Zirconia, Tarnish Resistant, Nickel-free, Lead-free, Cadmium-free; Plating: Rhodium; Finish: High Polish. It Won't Change Color Or Get Dark. Pendant size: 0.91*0.72*0.13 inch; Chain length: 18 inch; Total weight: 2.08 g. Exquisite Gift Wrap: Comes with the charm gift box, perfect for any gift giving occasion, great graduation gift, birthday gift, congratulation gift, vocation gift, anniversary gift, wedding gift, business gift, Thanksgiving gift, Halloween gift, Valentine's day gift, Mother's day gift, Easter day gift ,Christmas gift for vegetarian, teens, girls, women, grandma, mother, daughter, niece, granddaughter, wife, girlfriend, lover, business partner.Suitable for any occasion, easy to match any clothes. Our product has strict quality inspection. Should you have quality problems, please kindly contact us any time, we will be glad to find a resolution for you.",
            'delivery_days': 7,
            'pic_link': '/img/products/y010.jpg'
        },
        {
            'name': "Plenty: Vibrant Vegetable Recipes from London's Ottolenghi",
            'price': 8,
            'description': "A vegetarian cookbook from the author of Jerusalem A Cookbook  and other Ottolenghi cookbooks: A must-have collection of 120 vegetarian recipes from Yotam Ottolenghi featuring exciting flavors and fresh combinations that will become mainstays for readers and eaters looking for a brilliant take on vegetables. Mastering the art of French cooking the Yotam Ottolenghi way: One of the most exciting talents in the cooking world, Yotam Ottolenghi's food inspiration comes from his Cordon Bleu training, Mediterranean background, and his unapologetic love of ingredients. 'My approach can be the opposite to traditional French cooking, where everything is a little bit uniform and you work hard to process a sauce into the most fine and homogenous thing. I go the other way and use spices, herbs and other ingredients to create a sense of surprise.' Not a vegetarian himself, his approach to vegetable dishes is wholly original and innovative, based on freshness and seasonality, and drawn from the diverse food cultures represented in London. The Plenty cookbook: Plenty is the cookbook that launched Yotam Ottolenghi from a fabulous chef, London restaurant owner, and British newspaper columnist to an international food celebrity. In Plenty , Yotam puts a spotlight on vegetarian restaurant-caliber recipes that every home cook can make. A vibrant photo accompanies every recipe in this visually stunning Ottolenghi cookbook. Essential for meat-eaters and vegetarians alike! Plenty is an indispensable cookbook for every home library.",
            'delivery_days': 15,
            'pic_link': '/img/products/y011.jpg'
        },
        {
            'name': "elegantmedical HANDMADE 10MM Tiger Eye Beads ROSARY CROSS Catholic Necklace Men's Womens Religion GIFT BOX",
            'price': 46,
            'description': "Made in USA or Imported, elegantmedical HANDMADE 10MM Tiger Eye Beads ROSARY CROSS Catholic Necklace Men's Womens Religion GIFT BOX. Pardon cross size : 2.1' (5.5 cm) , mary and jesus medal : 2.0cm , material：Metal Plated Silver , FROM ITALY. ROSARY SIZE: 25' (65CM) Length from the cross to the end, the lenght of the rosary Necklace circumference: 78cm/30'-88cm/35'. 10MM Tiger Eye Jade BEADS",
            'delivery_days': 20,
            'pic_link': '/img/products/y012.jpg'
        },
        {
            'name': 'The Gift of Death, Second Edition & Literature in Secret (Religion and Postmodernism)',
            'price': 100,
            'description': "The Gift of Death, Jacques Derridas most sustained consideration of religion, explores questions first introduced in his bookGiven Time about the limits of the rational and responsible that one reaches in granting or accepting death, whether by sacrifice, murder, execution, or suicide. Derrida analyzes Czech philosopher Jan PatockasHeretical Essays in the Philosophy of History and develops and compares his ideas to the works of Heidegger, Lévinas, and Kierkegaard. One of Derridas major works,The Gift of Death resonates with much of his earlier writing, and this highly anticipated second edition is greatly enhanced by David Willss updated translation. This new edition also features the first-ever English translation of DerridasLiterature in Secret. In it, Derrida continues his discussion of the sacrifice of Isaac, which leads to bracing meditations on secrecy, forgiveness, literature, and democracy. He also offers a reading of KafkasLetter to His Father and uses the story of the flood in Genesis as an embarkation point for a consideration of divine sovereignty. An important contribution to the critical study of ethics that commends itself to philosophers, social scientists, scholars of religion . . . [and those] made curious by the controversy that so often attends Derrida.Booklist, on the first edition",
            'delivery_days': 15,
            'pic_link': '/img/products/y013.jpg'
        },
        {
            'name': 'Gifts for Men Dad, Survival Gear and Equipment 14 in 1, Fishing Hunting Christmas Birthday Valentines Day Gift Ideas for Him Husband Boyfriend Teenage Boy, Cool Gadget, Survival Kit Emergency Camping',
            'price': 50,
            'description': "Cool Unique Christmas Gifts: Does your dad love spending all the time in the outdoors he can? Get him a gift or few that will show him you care about his favorite activities! Look no further! This Survial Gear and Equipment is ideal for all outdoor hunter lovers. Must Have Camping Gear: 14 in 1 Emergency Survival Kit contains: Upgrade Survival Knife, Pocket Bellow, Wire Saw, Emergency Blanket, Flint stone Scraper, Flashlight, Credit Card Knife, Compass, Waterproof Box. Prepared for Any Emergency: This Camping Accessories is the perfect companion to help keep you safe and have peace of mind while you're Hiking, Camping, Hunting, Fishing, backpacking, travel or adventures. Dad Gifts Ideas: Cool Gadget for men, Birthdays Top Best gifts for him father best friend brother hunter and even who has everything. A stocking stuffer, Fishing Gift Hunting Accessories for teen boys scouts or family who interested in adventure. SERVICE: Your satisfaction is our top priority. If for any reason, father's day gifts for husband doesn't live up your expectations, contact us and we will solve it for you as soon as possible.",
            'delivery_days': 8,
            'pic_link': '/img/products/y014.jpg'
        },
        {
            'name': 'LEGO Star Wars at-at vs. Tauntaun Microfighters 75298 Building Kit; Awesome Buildable Toy Playset for Kids Featuring Luke Skywalker and at-at Driver Minifigures, New 2021 (205 Pieces)',
            'price': 77,
            'description': "Kids can recreate the Battle of Hoth from Star Wars: The Empire Strikes Back and role-play their own stories with these quick-build, LEGO brick AT-AT Walker and Tauntaun Microfighters This AT-AT vs. Tauntaun Microfighters (75298) set features 2 LEGO minifigures: Luke Skywalker, with a lightsaber, and an AT-AT Driver Each has a stud shooter and an electrobinoculars element The Tauntaun and the posable AT-AT each have a seat for a LEGO minifigure, and the set combines brilliantly with the Millennium Falcon Microfighter (75295) for extra battle action This awesome 205-piece construction toy makes the best birthday present, holiday gift or unexpected treat for kids aged 6 and up to introduce them to the fun, creative LEGO Star Wars universe. The Tauntaun measures over 2.5 in. (7 cm) high, 3.5 in. (9 cm) long and 2 in. (5 cm) wide. Along with the AT-AT and LEGO minifigures, the set fits in a child's backpack for play on their travels",
            'delivery_days': 15,
            'pic_link': '/img/products/y016.jpg'
        },
        {
            'name': 'TROJOY Sprinkler for Kids and Toddler, Sprinklers for Yard Kids Outdoor Water Toys Gifts for 3 4 5 Year Old Boys Girls Backyard Splash Water Play Outside Summer Activities - High-Attach to Garden Hose',
            'price': 20,
            'description': "COOL YOUR KIDS & YARD OFF - No better place to enjoy summer water fun than your own water park! This crazy turtle sprinkler is constructed from durable materials for outdoor use and attaches easily to a hose. Splashing fun for the entire family, as well an adorable way to water your lawn. An extra hose connector included for your convenience. SAFE WATER SPLASH TOY - Thanks for the many outlets design, the water pressure coming out of the rubber tubes and the spinning dome on the turtle’s back is perfectly safe for your children and your pets. Great performance for an extra wide spraying range. Spray height and strength can go high or low by adjusting your water pressure. EXCITING SCREEN-FREE OUTDOOR ACTIVITY - Outdoor water toys for kids have never been so exciting. All for one and fun for all! Twirls and Whirls are created as the water is released via the spinning back of the turtle as well as the attached wiggle tubes. All tubes always work together--especially when they are squirting you with water! GREAT GIFT FOR AGES 3 4 5 6 - It will be an absolute blast for kids aged 3+ to receive this cool and energetic, fun game for outside activities! Perfect addition to your next birthday party or gathering of friends and family. Made of Eco-friendly ABS material & CPC certified which guarantees it will last for years! HAPPINESS GUARANTEE - The water sprinkler encourages outdoor active play, helps develop coordination, and teaches nurturing and responsibility. We design every toy to the highest quality standards, and to nurture minds and hearts. If your child is not inspired, please reach our customer service and we'll make it right.",
            'delivery_days': 7,
            'pic_link': '/img/products/y017.jpg'
        },
        {
            'name': 'Kalimba Thumb Piano, 17 Key Kalimba Finger Piano with Protective Box, Tune Hammer, Study Instruction, Portable Mbira instruments for Adults, Gifts for Musicians Beginners Kids',
            'price': 20,
            'description': "Handmade with high quality mahogany and ore steel bars, gives you an excellent using experience. The keys are engraved with letters and notes, 17 keys / notes: 1(D), 2(B), 3(G), 4(E), 5(C5), 6(A), 7(F), 8(D), 9(C4), 10(E), 11(G), 12(B), 13(D), 14(F), 15(A), 16(C6), 17(E). All seventeen keys / tines sound perfect, suitable for a very wide range of music: pop, folk, rock, African, classical, carols. Make it a gift choice for both beginners and enthusiast. A manual book helps you play and tune this finger piano easily. If you are not 100 persent satisfied with this product, we offer a 30-day money back. Also, permanent customer service for you.",
            'delivery_days': 9,
            'pic_link': '/img/products/y018.jpg'
        },
        {
            'name': "Victrola's 4-in-1 Highland Bluetooth Record Player with 3-Speed Turntable with FM Radio, Farmhouse Walnut (VTA-330B-FNT)",
            'price': 100,
            'description': "Belt driven, 3-speed turntable (33 1/3, 45, 78 RPM) plays all of your favorite vinyl records. Classic FM radio with analog tuner and 'around the dial' LED lighting. Wirelessly stream music from your Bluetooth enabled device, up to 33 feet away. Features 3. 5mm Aux-In and RCA output connection. Built-in stereo speakers. Included components: Manual, Power Adaptor. Power source type: Corded Electric",
            'delivery_days': 20,
            'pic_link': '/img/products/y019.jpg'
        },
        {
            'name': "Mad Design/ Lunchifier, Amplifier Print Insulated Lunch Bag Cooler Tote, Gift for Men, Women, Kids, Musicians, Rock 'n Roll Electric Guitar Lovers and Rockstars",
            'price': 25,
            'description': "Unique Look: Music Lovers of all ages will appreciate this cool unisex guitar amplifier printed design. Generous size: Made deeper than most lunch bags to accommodate 6 canned drinks or larger lunches. Multi Use Bag: A great everyday school lunch bag for kids, or for adults to take their lunch to work, or as a cooler tote for cold drinks on a long trip. Features: Double zippers, top handle and adjustable, detachable shoulder strap for easy carrying and opening options. Size: Approximately dimensions: 9.5 in(H) x 7.5 in(W) x 4.5 in(D) Spot clean only, do not machine wash.",
            'delivery_days': 5,
            'pic_link': '/img/products/y020.jpg'
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
        }
    ]

    add_product_to_db_special(lst_hr)
    add_product_to_db_special(lst_yifan)
    sample_user = us.new_user('u_test_1', 'u_test_1', 'u_test_1', 'password', 'email@em.com', \
            'u_test_1', 'u_test_1', 'u_test_1', 'database_manual.json')
    db.add_user(sample_user, 'database_manual.json')
    vec = [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0]
    us.setup_interest(sample_user['id'], vec, 'database_manual.json')
    us.add_product_to_cart(sample_user['id'], 1, 2, 'database_manual.json')
    us.add_product_to_cart(sample_user['id'], 3, 4, 'database_manual.json')
    us.add_product_to_cart(sample_user['id'], 5, 6, 'database_manual.json')
    us.add_product_to_cart(sample_user['id'], 3, 4, 'database_manual.json')
    us.purchase(sample_user['id'], [[1,2], [3,8]], 'database_manual.json')
    all_prod = wb.keyword_searcher("", 'database_manual.json')
    print(wb.keyword_searcher("honey", 'database_manual.json'))
    print(wb.prod_filter_type(all_prod, [], [50, 9999999], 'database_manual.json'))
    # print(wb.prod_recommendation(sample_user['id'], all_prod, 'database_manual.json'))
    print(wb.search_filter_recommendation("", ctgry = [], price_rg = [0, 99999999], 
            user_id = sample_user['id'], page = -1, db_name = 'database_manual.json'))
    print(wb.search_filter_recommendation("", ctgry = [], price_rg = [0, 99999999], 
            user_id = sample_user['id'], page = 2, db_name = 'database_manual.json'))
    # temp = db.load_json('database_manual.json')
    # db.pretty_print(temp)