from app.models import db, ItemImage, environment, SCHEMA
from sqlalchemy.sql import text



def seed_itemImages():
    itemImage1 = ItemImage(
       item_id = 1, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966629883318373/item1.png?ex=65e78740&is=65d51240&hm=7a449462b4c55e96114c561a77761b25da84ae9d9ca5357fd0a8c5c333202244&'
    )
    itemImage2 = ItemImage(
       item_id = 2, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966630189510717/item2.png?ex=65e78740&is=65d51240&hm=2ada3101ed6881979027c06613e01b0405a18d1f35f4e767a6467599aeb0107e&'

    )
    itemImage3 = ItemImage(
        item_id = 3, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966631418433709/item3.png?ex=65e78741&is=65d51241&hm=555dadf6c78bc241c1508e51864e8c44109a91df54ae7c039a8c2926f7ad842f&'

    )
    itemImage4 = ItemImage(
        item_id = 4, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966631703654541/item4.png?ex=65e78741&is=65d51241&hm=8de150da5d0d48ac58c561df6980274b208ea87e8ecd5f104928e009b68c7baf&'

    )
    itemImage5 = ItemImage(
          item_id = 5, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966632018215023/item5.png?ex=65e78741&is=65d51241&hm=5586f3839bd711b6f69c6f7b96a274511da047fd304f7cf831b0bbc22562857f&'

    )
    itemImage6 = ItemImage(
          item_id = 6, url = 'https://media.discordapp.net/attachments/1130957424296198224/1130966631129022605/item6.png?ex=65e78741&is=65d51241&hm=aaf0490d07e6aeb1e460f50d0dcd284adaf71687dc7a62eba8c1493ced1d59b0&=&format=webp&quality=lossless&width=480&height=484'

    )
    itemImage7 = ItemImage(
        item_id = 7, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694877327593572/football6.png?ex=65edd0cf&is=65db5bcf&hm=d1897fd05957056325002f198b88ac23b79e427776dafa2bf1940e730bdc4329&'
    )
    itemImage8 = ItemImage(
        item_id = 8, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694877608628316/football5.png?ex=65edd0cf&is=65db5bcf&hm=0c4c276b53122fcb0c75a044ca5f4a25246faa5212089c4af6f546d582169407&'
    )
    itemImage9 = ItemImage(
        item_id = 9, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694878120316948/football4.png?ex=65edd0cf&is=65db5bcf&hm=7bcd20b29e718be072edb20b0e5664d1968d3de6a5112498546df2116fb4914c&'
    )
    itemImage10 = ItemImage(
        item_id = 10, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694878539743383/football3.png?ex=65edd0cf&is=65db5bcf&hm=867fbfb9d0560d9cdb0e6db089ab39190a0816d93eb60f0e8d2cf62833140234&'
    )
    itemImage11 = ItemImage(
        item_id = 11, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694878791422033/football2.png?ex=65edd0cf&is=65db5bcf&hm=1d5cce508fddcb60975396e7e7d8e6cb1696cbc1c81b787be5d508c917be44a1&'
    )
    itemImage12 = ItemImage(
        item_id = 12, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879005315122/football1.png?ex=65edd0cf&is=65db5bcf&hm=5e67a6929829f9d3bce0446dfefecc173098a37912c16f1f9a9ff9ac60be9708&'
    )
    itemImage13 = ItemImage(
        item_id = 13, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879240192000/basket8.png?ex=65edd0cf&is=65db5bcf&hm=55241da4a7f20cf011759e1cac14468d9a21e26717f3a776981f2ae04052d4fd&'
    )
    itemImage14 = ItemImage(
        item_id = 14, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879487660042/basket7.png?ex=65edd0cf&is=65db5bcf&hm=e79f792efb5852d9449d07f5b8f73bbb767331620da17d03e1b6100684764a3f&'
    )
    itemImage15 = ItemImage(
        item_id = 15, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879743508501/basket6.png?ex=65edd0cf&is=65db5bcf&hm=d8d693b302c06a3848fcbecc5b37ca878e7cd6ee67882a74b5d77e2f2c3fce23&'
    )
    itemImage16 = ItemImage(
        item_id = 16, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879986798613/basket5.png?ex=65edd0cf&is=65db5bcf&hm=332b2a82a480a71a72dbf431d09941c27efb704f10a127d895b4726210dec377&'
    )
    itemImage17 = ItemImage(
        item_id = 17, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695002028441772/basket4.png?ex=65edd0ec&is=65db5bec&hm=ce792f33b9ca505c869accdb3df9228e17b1b01a3754d455246d224931ac10e0&'
    )
    itemImage18 = ItemImage(
        item_id = 18, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695002376589412/basket3.png?ex=65edd0ed&is=65db5bed&hm=e04a66c569fb835a36be9a51e32f0be4f7702d4eb2bdfd1eede682c67f1d1536&'
    )
    itemImage19 = ItemImage(
        item_id = 19, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695002645012621/basket2.png?ex=65edd0ed&is=65db5bed&hm=9df74c07fa39752d5ee05cb51a2f9ce23cb55edb37ec0647fa401be2f268137b&'
    )
    itemImage20 = ItemImage(
        item_id = 20, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003064434718/basket1.png?ex=65edd0ed&is=65db5bed&hm=c51c749565794ea8c6376d588b883ac0590979bbe81aac76da5ed07e0b94be5a&'
    )
    itemImage21 = ItemImage(
        item_id = 21, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003286753320/golf4.png?ex=65edd0ed&is=65db5bed&hm=d0e9a4c2dccf8ec738eb335ee1dac3acbf52498c0bdf12f871e17b7893440eda&'
    )
    itemImage22 = ItemImage(
        item_id = 22, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003521622026/golf3.png?ex=65edd0ed&is=65db5bed&hm=48a9df60598a7856dc3ffa121665d33a99a87c10b377a486e3eb9119e05ecbc6&'
    )
    itemImage23 = ItemImage(
        item_id = 23, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003743912057/golf2.png?ex=65edd0ed&is=65db5bed&hm=dfc0b03c82c3d2ec4390094e443ab0070f7eaf177062a88d0d054a148061e2f4&'
    )
    itemImage24 = ItemImage(
        item_id = 24, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695004113031219/golf1.png?ex=65edd0ed&is=65db5bed&hm=57828eb1e61e55eaac9a6b17f5dca56dc92a8200a9e2a9e6d9a3b40a771a56b5&'
    )
    itemImage25 = ItemImage(
        item_id = 25, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695004444368946/soccer6.png?ex=65edd0ed&is=65db5bed&hm=4acd078d7fdaefe1e44d7a02e7f35f5e3339ab120cd72729e8b242c7faccb17a&'
    )
    itemImage26 = ItemImage(
        item_id = 26, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695004696018995/soccer5.png?ex=65edd0ed&is=65db5bed&hm=32f14ff56c73127fcf8749454eb44390800bc3e3b74ab5c567884d805f87379c&'
    )

    db.session.add(itemImage1)
    db.session.add(itemImage2)
    db.session.add(itemImage3)
    db.session.add(itemImage4)
    db.session.add(itemImage5)
    db.session.add(itemImage6)
    db.session.add(itemImage7)
    db.session.add(itemImage8)
    db.session.add(itemImage9)
    db.session.add(itemImage10)
    db.session.add(itemImage11)
    db.session.add(itemImage12)
    db.session.add(itemImage13)
    db.session.add(itemImage14)
    db.session.add(itemImage15)
    db.session.add(itemImage16)
    db.session.add(itemImage17)
    db.session.add(itemImage18)
    db.session.add(itemImage19)
    db.session.add(itemImage20)
    db.session.add(itemImage21)
    db.session.add(itemImage22)
    db.session.add(itemImage23)
    db.session.add(itemImage24)
    db.session.add(itemImage25)
    db.session.add(itemImage26)
    db.session.commit()



def undo_itemImages():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.itemImages RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM itemImages"))

    db.session.commit()
