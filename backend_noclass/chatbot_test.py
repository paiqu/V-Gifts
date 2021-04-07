import chatbot as ct 
import admin as ad

lst = [
    {
        'name': 'Rose Bear Women Gifts for Mom birthday girlfriend gifts for her , Rose Teddy Bear Rose Flowers Bear , Girls Valentines Bridal Wedding Anniversaries Birthday Graduation Gifts - Rose Bear with Box (red)',
        'price': 27,
        'description': "rose bear Teddy bears are the kind of gift that brings a smile to any girl's face just about any day. It doesn’t even have to be a special occasion to gift this beautiful teddy bear covered in white roses. If you want to make your girlfriend or wife feel special。rose flowers. THE PERFECT GIFT: Rose Teddy Bear arrives gift-ready in a fully assembled, crystal clear window box wrapped with premium satin ribbon. roses ,rose teddy bear ,rose bear with box ,rose bears ,flower teddy bear,rose box,rose bear teddy. Rose Bear Amaze the special someone in your life with this unforgettable rose teddy bear that from every angle. Perfect for Girlfriends, Weddings, Anniversaries, Birthdays, Graduations, Valentine\'s Day,mother\'s day,rose bears for valentines. rose teddy bear.",
        'delivery_days': 24,
        'pic_link': '/img/products/h002.jpg'
    },
]

for prod in lst:
    print(ad.new_product(prod['name'], prod['price'], prod['description'],\
                                None, prod['delivery_days'], prod['pic_link']))

