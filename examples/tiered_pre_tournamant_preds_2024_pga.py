from datagolf.api import DgAPI
from lookups.pga_champ_2024 import TIERS
from datagolf.models import PreTournamentPredModel
from datagolf.utils import write_dict_data_to_csv


PRED_MODEL = 'baseline_history_fit'


if __name__ == '__main__':
    api = DgAPI()
    
    preds = api._request.pre_tournament_predictions()  # todo replace with api once supported
    #tier_1_ids = [player.dg_id for player in api.common.get_players(names=TIER_1)]
    output = {}
    
    for tier, values in TIERS.items():
        dg_ids = [player.dg_id for player in api.get_players(name=values)]
        output_preds = []
        for pred in preds[PRED_MODEL]:  # once supported by api use . notation
            if pred['dg_id'] in dg_ids:
                output_preds.append(pred)
        output[tier] = output_preds
        
    for tier, data in output.items():
        write_dict_data_to_csv(filename=f'examples/output/pre_tournament_preds_pga_{tier.lower()}.csv', data=data)

        