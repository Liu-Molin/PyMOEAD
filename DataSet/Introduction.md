# Portfolio rebalancing
There are currently 7 data files.

These data files are the test problems used in the paper: M. Woodside-Oriakhi, C. Lucas and J.E. Beasley "Portfolio rebalancing with an investment horizon and transaction costs".
To appear in Omega, available from the third author at john.beasley@brunel.ac.uk

The test problems are the files: portreb1, portreb2, ..., portreb7

The format of these data files is: number of assets (N), maximum number of assets in portfolio (K), transaction cost limit (D), cash change (V)

for each asset i (i=1,...,N):

current price
current holding
fixed cost of buying any of this asset
fixed cost of selling any of this asset
variable cost per unit of asset bought
variable cost per unit of asset sold
minimum number of units of the asset we must buy if we carry out any buying of the asset
minimum number of units of the asset we must sell if we carry out any selling of the asset
maximum number of units of the asset we can buy if we carry out any buying of the asset
maximum number of units of the asset we can sell if we carry out any selling of the asset
for each asset i (i=1,...,N): 
mean return, standard deviation of return 

for all possible pairs of assets:
i, j, correlation between asset i and asset j

The largest file is portreb7 of size 30Mb (approximately) 
The entire set of files is of size 33Mb (approximately).