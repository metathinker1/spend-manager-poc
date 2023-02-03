from datetime import datetime
import pandas as pd
import logging

date_format = '%m/%d/%y'

''' Assumptions
- One file_path per account in MoneyWell'''
def import_moneywell_transaction_details_file(file_path):
    # TODO: Get the TransactionAccountId from the file_path
    with open(file_path) as fp:
        is_first_line = True
        transactions_list = []
        transactions = pd.DataFrame(columns=['Payee','Memo','Date','Type','Reference','Amount','Currency'])
        for line in fp:
            logging.info(line)
            parts = line.strip().split('\t')    # re.split(r'\t+', line.rstrip('\t'))
            logging.info(len(parts))
            if is_first_line:
                '''Skip header'''
                is_first_line = False
            else:
                if len(parts[1])+len(parts[2])+len(parts[3])+len(parts[4]) > 0:
                    parts[2] = datetime.strptime(parts[2], date_format)
                    parts[5] = float(parts[5])
                    transactions.loc[len(transactions)+1] = parts
                else:
                    transactions['Category'] = parts[0]
                    transactions_list.append(transactions)
                    transactions = pd.DataFrame(
                        columns=['Payee', 'Memo', 'Date', 'Type', 'Reference', 'Amount', 'Currency'])
        return pd.concat(transactions_list)


if __name__ == '__main__':
    file_path = 'TE_20191201_1211.txt'     # '201707_Detail.txt'
    imported_transactions = import_moneywell_transaction_details_file(file_path)
    print(f'imported_transactions: {len(imported_transactions)}, {imported_transactions.columns}, {imported_transactions.head(5)}')

