# File Name: world000
# World Name: 3rd Floor of Hospital
# Description: This is the starting area for the game. 
#              In this area, the player will learn to pickup/use items and find medicine for their wounds.

{
 's0':Scene('Your-Hospital-Room-3F', 
            'You awaken in a creepy hospital room filled with dusty, broken equipment.\n"How long had you been out for since the accident? \nWhere am I? Where is everyone?", your thoughts race.\n"I\'ve got to get out of here and get back to my family. They must be worried sick,"',
            {   'north':{   'move':None,
                            'look':'A grimy window, covered in dirt...or is that dried blood, you don\'t look too closely.\nThe cityscape outside is full of rubble, smoke, and erily quiet.'},
                'south':{   'move':'s1',
                            'look':'The only door in the room.'},
                'east':{    'move':None,
                            'look':None},
                'west':{    'move':None,
                            'look':None}},
            {'stick':Item(('stick', 'a heavy, sharp stick', 1, 0.01, 1, 0.25, 1, 1, 10))},
            {}
        )
,'s1':Scene('West-Hallway-3F', 
            'You enter a hallway. The air is dingy and stale. Lights flicker overhead, beds are strewn everywhere, total chaos.',
            {   'north':{   'move':'s0',
                            'look':'A door leads back to your room.'},
                'south':{   'move':None,
                            'look':'A bulletin board urges patients to wash their hands.'},
                'east':{    'move':'s3',
                            'look':'The empty hallway stretches on.'},
                'west':{    'move':'s2',
                            'look':'A zombie shuffles slowly around in circles in the hallway.'}},
            {},
            {}
        )
,'s2':Scene('East-Hallway-3F', 
            'You enter another hallway. A zombie shuffles around the hallway listlessly.\nIt seems to sniff the air, as if detecting your scent. It spots you and begins lurching toward you, moaning.',
            {   'north':{   'move':None,
                            'look':None},
                'south':{   'move':None,
                            'look':None},
                'east':{    'move':'s1',
                            'look':'An empty hallway.'},
                'west':{    'move':None,
                            'look':None}},
            {},
            {}
        )
,'s3':Scene('Reception-Desk-3F', 
            'You arrive at the nurses\' station. Charts litter the nurses\' desk, a body is slumped over in a chair.',
            {   'north':{   'move':None,
                            'look':None},
                'south':{   'move':None,
                            'look':None},
                'east':{    'move':'s4',
                            'look':'A sign for the elevator hangs crookedly from the ceiling.'},
                'west':{    'move':'s1',
                            'look':'A lone figure can be seen moving in the distance down the hall.'}},
            {'medicine':Item(('medicine', 'small dose of basic anti-bacterial medicine.', 1, 1, 1, 1.5, 1, 1, 0))},
            {}
        )
,'s4':Scene('Waiting-Area-3F', 
            'You enter a waiting area. Chairs and old magazines lie on coffee tables.',
            {   'north':{   'move':'death',
                            'look':'A smear of blood streaks the wall in front of an out-of-order elevator. A bony hand gropes from the gap in the doors.\nA low, gutteral moaning sound can be heard coming from within.'},
                'south':{   'move':None,
                            'look':None},
                'east':{    'move':'map_001_s0',
                            'look':'A door to the starwell lie in front of you.'},
                'west':{    'move':'s3',
                            'look':'The nurses\' station lies down the hall.'}},
            {},
            {}
        )
}