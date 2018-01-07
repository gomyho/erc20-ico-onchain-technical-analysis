# calculate holder number over time
# input: acc_holding_values_dict
#           key:    timestamp
#           value:  dict
#                   key:    account
#                   value:  amount
MINIMUM_TOKEN_AMOUNT_REQUIRED = 0.0

def track_holder_number_over_time(acc_holding_values_dict):
    holder_number_over_time = []
    for timestmap in acc_holding_values_dict:
        number = 1
        t_dict = acc_holding_values_dict[timestmap]
        for acc in t_dict:
            if t_dict[acc] >= MINIMUM_TOKEN_AMOUNT_REQUIRED:
                number += 1
        holder_number_over_time.append(number)
    return holder_number_over_time
