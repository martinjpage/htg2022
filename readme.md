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

