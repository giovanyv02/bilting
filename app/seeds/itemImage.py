from app.models import db, ItemImage, environment, SCHEMA
from sqlalchemy.sql import text



def seed_itemImages():
    itemImage1 = ItemImage(
       item_id = 1, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966629883318373/item1.png?ex=6643d040&is=66427ec0&hm=b40449db0bd82bbc5bd13ee7a9fba6da5af20cd9b9170f785ad072389d1859aa&'
    )
    itemImage2 = ItemImage(
       item_id = 2, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966630189510717/item2.png?ex=6643d040&is=66427ec0&hm=2346074a06d38149447425674890ed473a9d543a3d35ba09cf3449edccfc154d&'

    )
    itemImage3 = ItemImage(
        item_id = 3, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966631418433709/item3.png?ex=6643d041&is=66427ec1&hm=030a60841b74c97cf689516b3b33989d0af551a1de1395e6bf4e67dffb00e030&'

    )
    itemImage4 = ItemImage(
        item_id = 4, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966631703654541/item4.png?ex=6643d041&is=66427ec1&hm=777b1c3862668f0371be3ab6dcc758acae3f0638ef7a94194c207694ca9670da&'

    )
    itemImage5 = ItemImage(
          item_id = 5, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966632018215023/item5.png?ex=6643d041&is=66427ec1&hm=da252351dc9e8fa64108bd0ee24db6b81ef59fa3f97666b5b3e1b3826c38f040&'

    )
    itemImage6 = ItemImage(
          item_id = 6, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1130966631129022605/item6.png?ex=6643d041&is=66427ec1&hm=fad89c0880507386e46f2ecadc1b37d91c14fabc99804a4d5f8ea4bfd4c38732&'

    )
    itemImage7 = ItemImage(
        item_id = 7, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694877327593572/football6.png?ex=6643824f&is=664230cf&hm=18d641665c77e8f2e430f3a33eed46ff1fe34c95223752c2fae2f4e1a6d36ab7&'
    )
    itemImage8 = ItemImage(
        item_id = 8, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694877608628316/football5.png?ex=6643824f&is=664230cf&hm=1e066097be8bfb29111e157428a78a559ffed089624646035cb3367075493880&'
    )
    itemImage9 = ItemImage(
        item_id = 9, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694878120316948/football4.png?ex=6643824f&is=664230cf&hm=a363fbd5052cc9d93a7fbd442d4d2529b471770b4e6a224b9ece471223a7bf59&'
    )
    itemImage10 = ItemImage(
        item_id = 10, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694878539743383/football3.png?ex=6643824f&is=664230cf&hm=cabb8f2074f576e8ee97570b6ada81570f3819ef13828df035bec05f8a049a89&'
    )
    itemImage11 = ItemImage(
        item_id = 11, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694878791422033/football2.png?ex=6643824f&is=664230cf&hm=96ccc8d35a29c5ce93f8eeeb5b234487c0e3ac79ea14e738ed56bfff5f1d5764&'
    )
    itemImage12 = ItemImage(
        item_id = 12, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879005315122/football1.png?ex=6643824f&is=664230cf&hm=f3a95da51fbea360a2618bc80a1b054ac2040d4b1a6f58aac940ccc774c8e647&'
    )
    itemImage13 = ItemImage(
        item_id = 13, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879240192000/basket8.png?ex=6643824f&is=664230cf&hm=779e59cd05a2552023a1a6ff8ac4e9fc7f3c3b32faeb8edab61a6e8d5912c28b&'
    )
    itemImage14 = ItemImage(
        item_id = 14, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879487660042/basket7.png?ex=6643824f&is=664230cf&hm=beecbd2c4d17fed6c3d942c626d7f9f50fc491bb4c19d81b127dc8f7c793b966&'
    )
    itemImage15 = ItemImage(
        item_id = 15, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879743508501/basket6.png?ex=6643824f&is=664230cf&hm=5040175ff0f05ebcc01670689b3528135c378cbfd356e4676e0519964cf7d044&'
    )
    itemImage16 = ItemImage(
        item_id = 16, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132694879986798613/basket5.png?ex=6643824f&is=664230cf&hm=bd2958fa5bd28f61a825aae449881db52a8ea1b290802fa99dd6175c330eeea2&'
    )
    itemImage17 = ItemImage(
        item_id = 17, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695002028441772/basket4.png?ex=6643826c&is=664230ec&hm=dd3ffba95db882f512dc7dffdb1551bee72a7f4d0c2c2f71f2ba143d776cf564&'
    )
    itemImage18 = ItemImage(
        item_id = 18, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695002376589412/basket3.png?ex=6643826d&is=664230ed&hm=94c66a507e728873f9c3e48a4e60a126bc3f38b557f5a5f1db2e48744ede785d&'
    )
    itemImage19 = ItemImage(
        item_id = 19, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695002645012621/basket2.png?ex=6643826d&is=664230ed&hm=43c87215226ec055d2e359dc43935c21e202652c99e5ac6508623677d8ee6082&'
    )
    itemImage20 = ItemImage(
        item_id = 20, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003064434718/basket1.png?ex=6643826d&is=664230ed&hm=e35e58cc8ba5fb386a77d7b6d0079f03e408615a52d8c48574fc3491ddfea392&'
    )
    itemImage21 = ItemImage(
        item_id = 21, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003286753320/golf4.png?ex=6643826d&is=664230ed&hm=53a442cd584c2d638061627ed1a7629fd9f16c7e927c4c9ada21e64513273841&'
    )
    itemImage22 = ItemImage(
        item_id = 22, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003521622026/golf3.png?ex=6643826d&is=664230ed&hm=c4453ee7058de0292ff8c9e6fe61ae83ec0bb1679de44190cc2bd795e3852721&'
    )
    itemImage23 = ItemImage(
        item_id = 23, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695003743912057/golf2.png?ex=6643826d&is=664230ed&hm=7a9517703e963004fe370c05cce10231e3199c300a34fcd8255aabc00fbf246d&'
    )
    itemImage24 = ItemImage(
        item_id = 24, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695004113031219/golf1.png?ex=6643826d&is=664230ed&hm=8210024dc2f0f185d463fa2ab7573409a8ebf7b2e0429debc3822c543aaef667&'
    )
    itemImage25 = ItemImage(
        item_id = 25, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695004444368946/soccer6.png?ex=6643826d&is=664230ed&hm=2669db440968c0ccc380e3a9ecb0123c5ccc7a12d154d7ff31707bcf0b9019e6&'
    )
    itemImage26 = ItemImage(
        item_id = 26, url = 'https://cdn.discordapp.com/attachments/1130957424296198224/1132695004696018995/soccer5.png?ex=6643826d&is=664230ed&hm=010ca2c1d2815d16d88631e7a67924685cab4ec699b2617ee518ac21803bf978&'
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
