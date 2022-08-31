# sesucoin-blockchain (SESUCOIN)

![Alt sesucoin Logo](https://github.com/sesucoin-network/sesucoin-blockchain/raw/main/sesucoin-blockchain-gui/src/assets/img/sesucoin_circle.png)

Sesucoin (XSS) is a fast, efficient and ecological blockchain project designed mainly for the hotel industry.


## Useful Links

- [Sesucoin Website](https://www.sesucoin.eu) - Sesucoin official website
- [Sesucoin FAQ](https://www.sesucoin.eu/faq) - Frequently Asked Questions
- [Sesucoin Calculator](https://chiaforkscalculator.com/) - Estimate your sesucoin earnings.


## Social Links
- [Discord](https://discord.gg/7JcYy7BHcn) - Sesucoin Discord


## Ubuntu 22.04 Caution

If You decided to use Ubuntu 22.04, run these steps first to make sure You don't run into any python related problems when installing Sesucoin Blockchain.

```
# First install prerequisite package

   sudo apt install software-properties-common -y
  
# Add “deadsnakes” PPA

   sudo add-apt-repository ppa:deadsnakes/ppa -y

# Update system repositories to refresh package manager

   sudo apt-get update
   
# Install Python 3.9

   sudo apt-get install python3.9 -y
   
# Install Python 3.9-venv

   sudo apt-get install python3.9-venv -y
```

## How to Install

Sesucoin Executable are available from our [GitHub Releases Page](https://github.com/sesucoin-network/sesucoin-blockchain/releases). You can also build from source. An example case for Ubuntu source installation is provided below. Please [visit our wiki page](https://github.com/sesucoin-network/sesucoin-blockchain/wiki) for more details, and for source installation on operating systems.

```
# Update, install GIT, clone sesucoin repo

   sudo apt-get update
   sudo apt install git -y
   git clone https://github.com/sesucoin-network/sesucoin-blockchain.git
  
# Install sesucoin Blockchain

   cd sesucoin-blockchain
   sh install.sh
   . ./activate
   sesucoin init

# Install sesucoin GUI

   sh install-gui.sh
   cd sesucoin-blockchain-gui
   npm run electron &
```

If the sesucoin client is unable to find peers automatically, please connect to the following official peers:

- sesu.ddns.net / Port: 40444
- sesu-introducer.ddns.net / Port: 40444


## How to Stake

1. Query the staking addresses according to your farming plot list:

   ```
   $ sesucoin farm summary
   ...
   Staking addresses:
     xssd16da34epyvjv7095n7dywvax5xnsh22s8dsmugw30e9grke0t1yslt6gev (balance: 0, plots: 27)
   ...
   ```

2. Deposit coins to the staking address:

   ```
   $ sesucoin wallet send -t xssd16da34epyvjv7095n7dywvax5xnsh22s8dsmugw30e9grke0t1yslt6gev -a 1
   ```

   Wait for the transaction get confirmed, query staking balance again:

   ```
   $ sesucoin farm summary
   ...
   Staking addresses:
     xssd16da34epyvjv7095n7dywvax5xnsh22s8dsmugw30e9grke0t1yslt6gev (balance: 1, plots: 27)
   ...
   ```

3. Withdraw coins from the staking address:

   ```
   $ sesucoin wallet send_from -s xssd16da34epyvjv7095n7dywvax5xnsh22s8dsmugw30e9grke0t1yslt6gev -t $RECEIVER -n $NUMCOINS
   ```

   Do a transaction to transfer a number of coins from the staking address to any receive address.

   The value of each key will depend upon how the coins were deposited to the staking address.

   Make sure to choose the wallet that contains the plot farmer key.
