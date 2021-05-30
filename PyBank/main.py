{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months: 86\n",
      "Net Profit/Loss: $38382578\n",
      "Average P/L Change: $7803.476744186047\n",
      "Greatest Increase in P/L: Feb-2012 ($1926159)\n",
      "Greatest Decrease in P/L: Sep-2013 ($-2196167)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Dependencies\n",
    "import os\n",
    "import csv\n",
    "\n",
    "#  Pull in csv/ output text file\n",
    "budget_path = os.path.join(os.getcwd(), 'resources','budget.csv')\n",
    "\n",
    "pybank_output = os.path.join(os.getcwd(), 'analysis', 'pybank_output.txt')\n",
    "\n",
    "# Variables\n",
    "total_months = 0\n",
    "prev_pl = 0\n",
    "month_of_change = []\n",
    "pl_change_list = []\n",
    "greatest_increase = [\"\", 0]\n",
    "greatest_decrease = [\"\", 9999999999999999999]\n",
    "total_pl = 0\n",
    "\n",
    "# Read the csv & create dictionaries\n",
    "with open(budget_path) as pl_data:\n",
    "    reader = csv.DictReader(pl_data)\n",
    "\n",
    "    for row in reader:\n",
    "\n",
    "        # Total Months & total p/l\n",
    "        total_months = total_months + 1\n",
    "        total_pl = total_pl + int(row[\"Profit/Losses\"])\n",
    "\n",
    "        # Profit/Losses change month-to-month\n",
    "        pl_change = int(row[\"Profit/Losses\"]) - prev_pl\n",
    "        prev_pl = int(row[\"Profit/Losses\"])\n",
    "        pl_change_list = pl_change_list + [pl_change]\n",
    "        month_of_change = month_of_change + [row[\"Date\"]]\n",
    "\n",
    "        # Greatest increase\n",
    "        if (pl_change > greatest_increase[1]):\n",
    "            greatest_increase[0] = row[\"Date\"]\n",
    "            greatest_increase[1] = pl_change\n",
    "\n",
    "        # Greatest decrease\n",
    "        if (pl_change < greatest_decrease[1]):\n",
    "            greatest_decrease[0] = row[\"Date\"]\n",
    "            greatest_decrease[1] = pl_change\n",
    "\n",
    "# Average P/L Change\n",
    "pl_avg = sum(pl_change_list) / len(pl_change_list)\n",
    "\n",
    "# Financial analysis summary\n",
    "fa = (\n",
    "    f\"\\nFinancial Analysis\\n\"\n",
    "    f\"----------------------------\\n\"\n",
    "    f\"Total Months: {total_months}\\n\"\n",
    "    f\"Net Profit/Loss: ${total_pl}\\n\"\n",
    "    f\"Average P/L Change: ${pl_avg}\\n\"\n",
    "    f\"Greatest Increase in P/L: {greatest_increase[0]} (${greatest_increase[1]})\\n\"\n",
    "    f\"Greatest Decrease in P/L: {greatest_decrease[0]} (${greatest_decrease[1]})\\n\")\n",
    "\n",
    "# Print financial analysis\n",
    "print(fa)\n",
    "\n",
    "# Export the results to text file\n",
    "with open(pybank_output, \"w\") as txt_file:\n",
    "    txt_file.write(fa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
