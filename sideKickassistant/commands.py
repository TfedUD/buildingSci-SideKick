from sideKickassistant import database
import sys
from datetime import datetime
db = database.DatabaseManager('bigBrainSidekick.db')

# Refer to To Do list: create classes for the desired outputted to programs 
# To enable __repr__ create format 
class Cr8BaseTables:
# fairly sure separating the dicts via ; or , would be sufficient but.. when in doubt: bRuTeFoRcE
    def execute(self):
        db.create_table('insulation', {
            'id':'interger',
            'name':'text not null',
            'λ':'float',
            'density':'float',
            'specHeat':'float',
            'roughness':'float',
            'thermAbsorptance':'float',
            'solAbsorptance':'float',
            'visAbsorptance':'float',
            'porosity':'float',
            'WvapeDiffRes':'float',
            'builtInMoist':'float',
            'date_added':'text not null',
        })
        db.create_table('woodenMats', {
            'id':'interger',
            'name':'text not null',
            'λ':'float',
            'density':'float',
            'specHeat':'float',
            'roughness':'float',
            'thermAbsorptance':'float',
            'solAbsorptance':'float',
            'visAbsorptance':'float',
            'porosity':'float',
            'WvapeDiffRes':'float',
            'builtInMoist':'float',
            'date_added':'text not null',
        })
        db.create_table('masonry', {
            'id':'interger',
            'name':'text not null',
            'λ':'float',
            'density':'float',
            'specHeat':'float',
            'roughness':'float',
            'thermAbsorptance':'float',
            'solAbsorptance':'float',
            'visAbsorptance':'float',
            'porosity':'float',
            'WvapeDiffRes':'float',
            'builtInMoist':'float',
            'date_added':'text not null',
        })
        db.create_table('boards', {
            'id':'interger',
            'name':'text not null',
            'λ':'float',
            'density':'float',
            'specHeat':'float',
            'roughness':'float',
            'thermAbsorptance':'float',
            'solAbsorptance':'float',
            'visAbsorptance':'float',
            'porosity':'float',
            'WvapeDiffRes':'float',
            'builtInMoist':'float',
            'date_added':'text not null',
        })
        db.create_table('membranes', {
            'id':'interger',
            'name':'text not null',
            'λ':'float',
            'density':'float',
            'specHeat':'float',
            'porosity':'float',
            'WvapeDiffRes':'float',
            'builtInMoist':'float',
            'date_added':'text not null',
        })
        db.create_table('ventUnits', {
            'id':'interger',
            'name':'text not null',
            'recoveryEffi':'float',
            'elecEffi':'float',
            'humidReco':'float',
            'frostProtection':'interger',
        })

class AddStuff:
    # not confident on this one
    # use data[''] = func in future for the generic fillins for stuff (EP props like LBT)
    def execute(self, data, table_name):
        data['date_added'] = datetime.utcnow().isoformat()
        db.add(table_name, data)
        return 'data added'


class DeleteStuff:
    # I take that Back this SHOULD jive.. I hope
    def execute(self, table_name, data):
        db.delete(table_name, {'id':data})
        return 'data deleted'

class Quit:

    def execute(self):
        sys.exit()
