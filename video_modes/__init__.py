from video_modes.no_effect_mode import NoEffectMode
from video_modes.australia_mode import AustraliaMode
from video_modes.nineteeneightyfour_mode import NineteeneightyfourMode

modes = [] # list of touples: ('display_name', class)

modes.append(('No Effect', NoEffectMode))
modes.append(('Australia', AustraliaMode))
modes.append(('1984', NineteeneightyfourMode))