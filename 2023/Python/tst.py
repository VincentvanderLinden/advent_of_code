x = 'xtwoone34two'

import re
x.rfind(re.findall(r'one|two|three|four|five|six|seven|eight|nine', x)[-1])