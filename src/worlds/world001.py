# File Name: world001
# World Name: 2nd Floor of Hospital
# Description: This will be the area in which the player will train in the combat system by encountering a hostile zombie and fighting it.
# Item cheat sheet: (name(str), descrip(str), carry(bit), breakable(int), health(int), weight(int), droppable(bit), equipable(bit), attack_dmg(int))
{
 's0':Scene('Waiting-Area-2F', 
            'You stumble out of the stairwell and onto the second floor.\n',
            {   'north':{   'move':None,
                            'look':None},
                'south':{   'move':None,
                            'look':None},
                'east':{    'move':None,
                            'look':None},
                'west':{    'move':'map_000_s4',
                            'look':'A stairwell leading up to the third floor.'}},
            {'syringe':Item(('syringe', 'A solid looking, bone marrow extraction needle.', 1, 0.4, 1, 0.5, 1, 1, 20))},
            {}
        )
}