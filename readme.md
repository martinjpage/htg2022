# `smart_match.py`		User Manual for WattPeer

### NAME

`smart_match.py`: app to match buyers and suppliers of locally traded clean energy. 

### SYNOPSIS

 `smart_match.py [-h] {signup,update_settings,view_settings,supplier,buyer,history} `

### DESCRIPTION

Trade energy as a buyer or supplier by setting your minimum sell price as a supplier or maximum buy price as a buyer. Your smart meter will log sell orders when you have excess supply and match these to buy order in the orderbook. Matched orders will be executed through a smart contract that verifies the buyer's wallet and supplier's energy availability, executes the transaction, updates the orderbook and records the transaction on a ledger.   Partial matches are allowed so a supplier is allowed to meet only part of a buyers energy request, and vice versa. Preference is given to the buyer willing to pay the most. The buyer is matched with the most expensive supplier within the floor-ceiling range and the highest price between the sell price and buy price is selected.

### CORE OPTION

`signup`              Create user profile.
`update_settings`     Select a role as supplier or buyer, set a price and a date range.
`view_settings`       View your current role (supplier or buyer), price and active date range.
`supplier `          Perform a sell transaction as a supplier.
`buyer `              Perform a buy transaction as a buyer.
`history`             View block chain transaction history.

#### OPTIONS: signup

 `-h, --help`	 show this help message and exit
  `-un, --username` 	Input your username
  `-pw, --password`  	Input your password.
 ` -id, --meter_id`	Input your smart meter ID.
 `-l, --location {Italy}` 	Choose a location.

#### OPTIONS: update_settings

  `-h, --help`	show this help message and exit
  `-un , --username` 	Input your username
 ` -pw , --password`	 Input your password.
  `-r, --role {supplier,buyer}`	Choose to be a supplier or buyer.
  `-p, --price` 	Set your minimum sell price or maximum buy price (EUR)
  `-s, --start` 	Set the start date for transactions to run.
 `-e, --end`		Set the end date for transactions to run.

#### OPTIONS: view_settings

  `-h, --help`            show this help message and exit
  `-un, --username`	Input your username
  `-pw, --password`	Input your password.

#### OPTIONS: supplier

  `-h, --help`            show this help message and exit
` -un, --username`	Input your username
 ` -pw , --password`	Input your password.
 `-e , --energy`		Give the amount of energy you want to sell in kW.

#### OPTIONS: buyer

  `-h, --help`           show this help message and exit
  `-un, --username` 	Input your username
 `-pw, --password`		Input your password.
  `-e, --energy `		Give the amount of energy you want to buy in kW.

#### OPTIONS: history

  `-h, --help`            show this help message and exit
  `-un, --username` 	Input your username
  `-pw , --password` Input your password.

### SOFTWARE ARCHITECURE

![soft_arch](wiki\soft_arch.png)

### USAGE EXAMPLES

`> python .\smart_match.py **signup** --username martin --password martin123 --meter_id smartmartin --location Italy`

New user with id 'leonardo' and meter id 'smartmartin' added to user database.

`> python .\smart_match.py **signup** --username leonardo --password leo123 --meter_id smartleo --location Italy`

New user with id 'leonardo' and meter id 'smartleo' added to user database.

`> python .\smart_match.py **signup** --username leonardo --password leo123 --meter_id smartleo --location Italy`

ValueError: A user with name “leonardo" already exists.

`> python .\smart_match.py **signup** --username natalia --password nat123 --meter_id smartmartin --location Italy`

ValueError: A meter with meter id "smartmartin" already exists

`> python .\smart_match.py **update_settings** --username martin --password martin123 --role supplier --price 0.15`

Role (supplier), price (0.15), start (2022-03-20) and end (None) date updated for martin.

`> python .\smart_match.py **update_settings** --username leonardo --password leo123 --role buyer --price 0.17`

Role (buyer), price (0.17), start (2022-03-20) and end (None) date updated for leonardo.

`> python .\smart_match.py **view_settings** --username martin --password martin123`

username  password location   meter_id  role price start_date end_date

0  martin martin123  Italy smartmartin supplier  0.15 2022-03-20    NaN

`> python .\smart_match.py **view_settings** --username leonardo --password leo123`

|      | username | password | location | meter_id | role  | price | start_date | end_date |
| ---- | -------- | -------- | -------- | -------- | ----- | ----- | ---------- | -------- |
| 0    | leonardo | leo123   | Italy    | smartleo | buyer | 0.17  | 2022-03-20 | NaN      |

`> python .\smart_match.py **supplier** --username martin --password martin123 --energy 5`

New supplier offer from smartmartin added to orderbook.

Currently there are no buy offers in the orderbook. No match can be made at present.

`> python .\smart_match.py **buyer** --username leonardo --password leo123 --energy 3`

New supplier offer from smartmartin added to orderbook.

New buyer offer from smartleo added to orderbook.

smartmartin can meet the full energy request from smartleo of 3.0 kW. Transaction will occur at a unit price of 0.17 EUR.

Seller authenticated. Energy available.

Buyer authenticated. Money available.

smartmartin's energy balanced updated by -3.00 kW.

smartleo's energy balanced updated by 3.00 kW.

smartmartin's wallet balanced updated by 0.51 EUR.

smartleo's wallet balanced updated by -0.51 EUR.

Removing fulfilled orders from orderbook:

|      | meter_id | location | role  | energy | price | end_date |
| ---- | -------- | -------- | ----- | ------ | ----- | -------- |
| 1    | smartleo | Italy    | buyer | 0.0    | 0.17  | NaN      |

Recorded transaction between smartleo (buyer) and smartmartin (supplier) for 3.0 kWh at 0.17 EUR per kWh (total: 0.51 EUR).

Currently there are no buy offers in the orderbook. No match can be made at present.

`> python .\smart_match.py **history** --username martin --password martin123`

No buyer history.

Supplier History:

|      | buyer    | supplier    | price | energy | total_price | date       |
| ---- | -------- | ----------- | ----- | ------ | ----------- | ---------- |
| 0    | smartleo | smartmartin | 0.17  | 3.0    | 0.51        | 2022-03-20 |

`> python .\smart_match.py **history** --username leonardo --password leo123`

Buyer History:

|      | buyer    | supplier    | price | energy | total_price | date       |
| ---- | -------- | ----------- | ----- | ------ | ----------- | ---------- |
| 0    | smartleo | smartmartin | 0.17  | 3.0    | 0.51        | 2022-03-20 |

No seller history.
