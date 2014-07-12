# File Name: world0
# World Name: 3rd Floor of Hospital
# Description: This is the starting area for the game.

{
 's0':Scene('Your-Hospital-Room-3F', 
 			'creepy room with broken equipment.',
 			{	'north':{	'move':None,
 							'look':'A grimy window, covered in dirt...or is that dried blood, you don\'t look too closely.\nThe cityscape outside is full of rubble, smoke, and erily quiet.'},
 				'south':{	'move':'s1',
 							'look':'The only door in the room.'},
 				'east':{	'move':None,
 							'look':None},
 				'west':{	'move':None,
 							'look':None}},
 			{'stick':'a heavy, sharp stick'},
 			{}
 		)
,'s1':Scene('West-Hallway-3F', 
			'hallway. The air is dingy and stale. Lights flicker overhead, beds are strewn everywhere, total chaos.',
			{	'north':{	'move':'s0',
							'look':'A door leads back to your room.'},
				'south':{	'move':None,
							'look':'A bulletin board urges patients to wash their hands.'},
				'east':{	'move':'s3',
							'look':'The empty hallway streches on.'},
				'west':{	'move':'s2',
							'look':'A zombie shuffles slowly around in circles in the hallway.'}},
			{},
			{}
		)
,'s2':Scene('East-Hallway-3F', 
			'another hallway. A zombie shuffles around the hallway listlessly.\nIt seems to sniff the air, as if detecting your scent. It spots you and begins lurching toward you, moaning.',
			{	'north':{	'move':None,
							'look':None},
				'south':{	'move':None,
							'look':None},
				'east':{	'move':'s1',
							'look':'An empty hallway.'},
				'west':{	'move':None,
							'look':None}},
			{},
			{'Zombie'}
		)
,'s3':Scene('Reception-Desk-3F', 
			'nurses\' station. Charts litter the nurses\' desk, a body is slumped over in a chair.',
			{	'north':{	'move':None,
							'look':None},
				'south':{	'move':None,
							'look':None},
				'east':{	'move':'s4',
							'look':'A sign for the elevator hangs crookedly from the ceiling.'},
				'west':{	'move':'s1',
							'look':'A lone figure can be seen moving in the distance down the hall.'}},
			{},
			{}
		)
,'s4':Scene('Waiting-Area-3F', 
			'waiting area. Chairs and old magazines lie on coffee tables.',
			{	'north':{	'move':'death',
							'look':'A smear of blood streaks the wall in front of an out-of-order elevator. A bony hand gropes from the gap in the doors.\nA low, gutteral moaning sound can be heard coming from within.'},
				'south':{	'move':None,
							'look':None},
				'east':{	'move':'map_001',
							'look':'A door to the starwell lie in front of you.'},
				'west':{	'move':'s3',
							'look':'The nurses\' station lies down the hall.'}},
			{},
			{}
		)
}